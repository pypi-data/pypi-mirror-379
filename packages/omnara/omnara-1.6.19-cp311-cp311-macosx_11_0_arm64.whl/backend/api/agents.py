from enum import Enum
from uuid import UUID
import json
from typing import AsyncGenerator
import asyncio

from fastapi import APIRouter, Depends, HTTPException, Request, BackgroundTasks
from fastapi.responses import StreamingResponse
from shared.database.models import User
from shared.database.session import get_db, SessionLocal
from shared.database.enums import AgentStatus
from sqlalchemy.orm import Session
import asyncpg

from ..auth.dependencies import get_current_user
from ..auth.supabase_client import get_supabase_anon_client
from ..db import (
    get_agent_instance_detail,
    get_agent_type_instances,
    get_agent_summary,
    get_all_agent_instances,
    get_all_agent_types_with_instances,
    mark_instance_completed,
    delete_agent_instance,
    update_agent_instance_name,
    get_message_by_id,
    get_instance_messages,
    get_instance_git_diff,
    get_instance_shares,
    add_instance_share,
    remove_instance_share,
)
from ..models import (
    AgentInstanceDetail,
    AgentInstanceResponse,
    AgentTypeOverview,
    MessageResponse,
    UserMessageRequest,
    InstanceShareCreateRequest,
    InstanceShareResponse,
)
from servers.shared.db import update_session_title_if_needed
from ..db.queries import create_user_message_with_access

router = APIRouter(tags=["agents"])


@router.get("/agent-types", response_model=list[AgentTypeOverview])
def list_agent_types(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all agent types with their instances for the current user"""
    agent_types = get_all_agent_types_with_instances(db, current_user.id)
    return agent_types


class AgentInstanceScope(str, Enum):
    ME = "me"
    SHARED = "shared"
    ALL = "all"


@router.get("/agent-instances", response_model=list[AgentInstanceResponse])
def list_all_agent_instances(
    limit: int | None = None,
    scope: AgentInstanceScope = AgentInstanceScope.ME,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get agent instances visible to the current user"""
    instances = get_all_agent_instances(
        db, current_user.id, limit=limit, scope=scope.value
    )
    return instances


@router.get("/agent-summary")
def get_all_agent_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get lightweight summary of agent counts for dashboard KPIs"""
    summary = get_agent_summary(db, current_user.id)
    return summary


@router.get(
    "/agent-types/{type_id}/instances", response_model=list[AgentInstanceResponse]
)
def get_type_instances(
    type_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all instances for a specific agent type for the current user"""
    result = get_agent_type_instances(db, type_id, current_user.id)
    if result is None:
        raise HTTPException(status_code=404, detail="Agent type not found")
    return result


@router.get("/agent-instances/{instance_id}", response_model=AgentInstanceDetail)
def get_instance_detail(
    instance_id: UUID,
    message_limit: int = 50,
    before_message_id: UUID | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get detailed information about a specific agent instance for the current user with cursor-based message pagination"""
    result = get_agent_instance_detail(
        db,
        instance_id,
        current_user.id,
        message_limit=message_limit,
        before_message_id=before_message_id,
    )
    if not result:
        raise HTTPException(status_code=404, detail="Agent instance not found")
    return result


@router.get("/agent-instances/{instance_id}/messages")
def get_instance_messages_paginated(
    instance_id: UUID,
    limit: int = 50,
    before_message_id: UUID | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get paginated messages for an agent instance using cursor-based pagination"""
    messages = get_instance_messages(
        db,
        instance_id,
        current_user.id,
        limit=limit,
        before_message_id=before_message_id,
    )
    if messages is None:
        raise HTTPException(status_code=404, detail="Agent instance not found")
    # Return just the messages array
    return messages


@router.get(
    "/agent-instances/{instance_id}/access",
    response_model=list[InstanceShareResponse],
)
def list_instance_access(
    instance_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List users who have access to this agent instance"""
    try:
        return get_instance_shares(db, instance_id, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e)) from e


@router.post(
    "/agent-instances/{instance_id}/access",
    response_model=InstanceShareResponse,
)
def add_instance_access(
    instance_id: UUID,
    request: InstanceShareCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Grant access to an agent instance for another user"""
    try:
        share = add_instance_share(
            db,
            instance_id=instance_id,
            user_id=current_user.id,
            email=request.email,
            access_level=request.access,
        )
        db.commit()
        return share
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e)) from e
    except PermissionError as e:
        db.rollback()
        raise HTTPException(status_code=403, detail=str(e)) from e


@router.delete("/agent-instances/{instance_id}/access/{access_id}")
def remove_instance_access(
    instance_id: UUID,
    access_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Revoke shared access from a user"""
    try:
        remove_instance_share(db, instance_id, current_user.id, access_id)
        db.commit()
        return {"status": "success"}
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=404, detail=str(e)) from e
    except PermissionError as e:
        db.rollback()
        raise HTTPException(status_code=403, detail=str(e)) from e


@router.post("/agent-instances/{instance_id}/messages", response_model=MessageResponse)
def create_user_message_endpoint(
    instance_id: UUID,
    request: UserMessageRequest,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Send a message to an agent instance (answers questions or provides feedback)"""
    try:
        message = create_user_message_with_access(
            db=db,
            instance_id=instance_id,
            user=current_user,
            content=request.content,
            mark_as_read=False,
        )

        db.commit()

        def update_title_with_session():
            db_session = SessionLocal()
            try:
                update_session_title_if_needed(
                    db=db_session,
                    instance_id=instance_id,
                    user_message=request.content,
                )
            finally:
                db_session.close()

        background_tasks.add_task(update_title_with_session)

        return message
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=404, detail=str(e)) from e
    except PermissionError as e:
        db.rollback()
        raise HTTPException(status_code=403, detail=str(e)) from e
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}"
        ) from e


@router.get("/agent-instances/{instance_id}/messages/stream")
async def stream_messages(
    request: Request,
    instance_id: UUID,
    token: str | None = None,
):
    """Stream new messages for an agent instance using Server-Sent Events"""
    if not token:
        raise HTTPException(status_code=401, detail="Token required for SSE")

    try:
        supabase = get_supabase_anon_client()
        user_response = supabase.auth.get_user(token)

        if not user_response or not user_response.user:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = UUID(user_response.user.id)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")

    with SessionLocal() as db:
        instance = get_agent_instance_detail(db, instance_id, user_id)
        if not instance:
            raise HTTPException(status_code=404, detail="Agent instance not found")

    async def message_generator() -> AsyncGenerator[str, None]:
        # Import settings here to avoid circular imports
        from shared.config.settings import settings

        # Create connection to PostgreSQL for LISTEN/NOTIFY
        conn = await asyncpg.connect(settings.database_url)
        try:
            # Listen to the channel for this instance
            channel_name = f"message_channel_{instance_id}"

            # Execute LISTEN command (quote channel name for UUIDs with hyphens)
            await conn.execute(f'LISTEN "{channel_name}"')

            # Create a queue to receive notifications
            notification_queue = asyncio.Queue()

            # Define callback to put notifications in queue
            def notification_callback(connection, pid, channel, payload):
                asyncio.create_task(notification_queue.put(payload))

            # Add listener with callback
            await conn.add_listener(channel_name, notification_callback)

            # Send initial connection event
            yield f"event: connected\ndata: {json.dumps({'instance_id': str(instance_id)})}\n\n"

            while True:
                # Check if client disconnected
                if await request.is_disconnected():
                    break

                try:
                    # Wait for notification with timeout for heartbeat
                    payload = await asyncio.wait_for(
                        notification_queue.get(), timeout=30.0
                    )

                    # Parse the JSON payload
                    data = json.loads(payload)

                    # Check event type and handle accordingly
                    event_type = data.get("event_type")

                    if event_type == "status_update":
                        # Status updates already have all needed data
                        yield f"event: status_update\ndata: {json.dumps(data)}\n\n"

                    elif event_type == "message_insert":
                        message_id = data.get("id")
                        if not message_id:
                            continue

                        with SessionLocal() as db:
                            message_data = get_message_by_id(
                                db, UUID(message_id), user_id
                            )
                        if message_data:
                            data.update(message_data)

                        yield f"event: message\ndata: {json.dumps(data)}\n\n"

                    elif event_type == "message_update":
                        message_id = data.get("id")
                        if not message_id:
                            continue

                        with SessionLocal() as db:
                            message_data = get_message_by_id(
                                db, UUID(message_id), user_id
                            )
                        if message_data:
                            old_requires_user_input = data.get(
                                "old_requires_user_input"
                            )
                            data.update(message_data)
                            if old_requires_user_input is not None:
                                data["old_requires_user_input"] = (
                                    old_requires_user_input
                                )

                        yield f"event: message_update\ndata: {json.dumps(data)}\n\n"

                    elif event_type == "git_diff_update":
                        instance_id_str = data.get("instance_id")
                        if not instance_id_str:
                            continue

                        with SessionLocal() as db:
                            diff_data = get_instance_git_diff(
                                db, UUID(instance_id_str), user_id
                            )
                        if diff_data:
                            data["git_diff"] = diff_data["git_diff"]

                        yield f"event: git_diff_update\ndata: {json.dumps(data)}\n\n"

                    elif event_type == "agent_heartbeat":
                        # Forward agent heartbeat updates (last_heartbeat_at changes)
                        # Expect payload to include: instance_id, last_heartbeat_at
                        yield f"event: agent_heartbeat\ndata: {json.dumps(data)}\n\n"

                except asyncio.TimeoutError:
                    # Send heartbeat to keep connection alive
                    yield f"event: heartbeat\ndata: {json.dumps({'timestamp': asyncio.get_event_loop().time()})}\n\n"

                except Exception as e:
                    # Send error event
                    yield f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"
                    break

        finally:
            # Clean up listener and connection
            await conn.remove_listener(channel_name, notification_callback)
            await conn.close()

    return StreamingResponse(
        message_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # Disable Nginx buffering
        },
    )


@router.put(
    "/agent-instances/{instance_id}/status",
    response_model=AgentInstanceResponse,
)
def update_agent_status(
    instance_id: UUID,
    status_update: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update an agent instance status for the current user"""
    # For now, we only support marking as completed
    if status_update.get("status") == AgentStatus.COMPLETED:
        result = mark_instance_completed(db, instance_id, current_user.id)
        if not result:
            raise HTTPException(status_code=404, detail="Agent instance not found")
        return result
    else:
        raise HTTPException(status_code=400, detail="Status update not supported")


@router.delete("/agent-instances/{instance_id}")
def delete_agent_instance_endpoint(
    instance_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete an agent instance"""
    result = delete_agent_instance(db, instance_id, current_user.id)
    if not result:
        raise HTTPException(status_code=404, detail="Agent instance not found")
    return {"message": "Agent instance deleted successfully"}


@router.patch("/agent-instances/{instance_id}", response_model=AgentInstanceResponse)
def update_agent_instance_endpoint(
    instance_id: UUID,
    update_data: dict,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update agent instance (currently only supports name)"""
    if "name" not in update_data:
        raise HTTPException(status_code=400, detail="Only name updates are supported")

    result = update_agent_instance_name(
        db, instance_id, current_user.id, update_data["name"]
    )
    if not result:
        raise HTTPException(status_code=404, detail="Agent instance not found")

    return result
