"""
Database queries for UserAgent operations.
"""

import httpx
from datetime import datetime, timezone
from uuid import UUID, uuid4
import hashlib

from shared.database import (
    UserAgent,
    AgentInstance,
    AgentStatus,
    APIKey,
    Message,
)
from shared.database.billing_operations import check_agent_limit
from shared.webhook_schemas import (
    format_webhook_request,
    validate_webhook_config,
    validate_runtime_fields,
    get_runtime_field_names,
)
from sqlalchemy import and_, func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session, joinedload

from ..models import UserAgentRequest, WebhookTriggerResponse
from .queries import _format_instance, _get_instance_message_stats
from ..auth.jwt_utils import create_api_key_jwt


def create_user_agent(
    db: Session, user_id: UUID, request: UserAgentRequest
) -> dict | None:
    """Create a new user agent configuration"""

    # Check if non-deleted agent with same name already exists for this user
    existing = (
        db.query(UserAgent)
        .filter(
            and_(
                UserAgent.user_id == user_id,
                UserAgent.name == request.name,
                UserAgent.is_deleted.is_(False),
            )
        )
        .first()
    )

    if existing:
        return None

    user_agent = UserAgent(
        user_id=user_id,
        name=request.name,
        webhook_type=request.webhook_type,
        webhook_config=request.webhook_config,
        is_active=request.is_active,
    )

    db.add(user_agent)
    db.commit()
    db.refresh(user_agent)

    return _format_user_agent(user_agent, db)


def get_user_agents(db: Session, user_id: UUID) -> list[dict]:
    """Get all non-deleted user agents for a specific user"""

    user_agents = (
        db.query(UserAgent)
        .filter(and_(UserAgent.user_id == user_id, UserAgent.is_deleted.is_(False)))
        .all()
    )

    return [_format_user_agent(agent, db) for agent in user_agents]


def update_user_agent(
    db: Session, agent_id: UUID, user_id: UUID, request: UserAgentRequest
) -> dict | None:
    """Update an existing user agent configuration"""

    user_agent = (
        db.query(UserAgent)
        .filter(
            and_(
                UserAgent.id == agent_id,
                UserAgent.user_id == user_id,
                UserAgent.is_deleted.is_(False),
            )
        )
        .first()
    )

    if not user_agent:
        return None

    user_agent.name = request.name
    user_agent.webhook_type = request.webhook_type
    user_agent.webhook_config = request.webhook_config
    user_agent.is_active = request.is_active
    user_agent.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(user_agent)

    return _format_user_agent(user_agent, db)


async def trigger_webhook_agent(
    db: Session,
    user_agent: UserAgent,
    user_id: UUID,
    user_request_data: dict,
) -> WebhookTriggerResponse:
    """Trigger a webhook agent by calling the webhook URL"""

    # Check if webhook is configured
    if not user_agent.webhook_type or not user_agent.webhook_config:
        return WebhookTriggerResponse(
            success=False,
            message="Webhook not configured",
            error="No webhook configuration found for this agent",
        )

    # Validate runtime fields early
    runtime_field_names = get_runtime_field_names(user_agent.webhook_type)
    user_request = {
        field: value
        for field, value in user_request_data.items()
        if field in runtime_field_names
    }

    is_valid, error_msg = validate_runtime_fields(user_agent.webhook_type, user_request)
    if not is_valid:
        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Invalid runtime parameters",
            error=error_msg,
        )

    # Check if user has capacity to create a new instance
    try:
        check_agent_limit(user_id, db, increment=1)
    except Exception as e:
        # Return error response if limit exceeded
        return WebhookTriggerResponse(
            success=False,
            message="Agent limit exceeded",
            error=str(e),
        )

    agent_instance_id = uuid4()

    api_key_name = f"{user_agent.name} Key"

    existing_key = (
        db.query(APIKey)
        .filter(
            and_(
                APIKey.user_id == user_id,
                APIKey.name == api_key_name,
                APIKey.is_active,
            )
        )
        .first()
    )

    if existing_key:
        omnara_api_key = existing_key.api_key
    else:
        jwt_token = create_api_key_jwt(
            user_id=str(user_id),
            expires_in_days=None,
        )

        api_key = APIKey(
            user_id=user_id,
            name=api_key_name,
            api_key_hash=hashlib.sha256(jwt_token.encode()).hexdigest(),
            api_key=jwt_token,
            expires_at=None,
        )
        db.add(api_key)
        db.commit()

        omnara_api_key = jwt_token

    # Prepare backend-generated fields
    backend_fields = {
        "agent_instance_id": str(agent_instance_id),
        "agent_type": user_agent.name,
        "omnara_api_key": omnara_api_key,
    }

    # Get webhook configuration
    webhook_type = user_agent.webhook_type
    webhook_config = user_agent.webhook_config

    # Validate configuration
    is_valid, error_msg = validate_webhook_config(webhook_type, webhook_config)
    if not is_valid:
        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Invalid webhook configuration",
            error=error_msg,
        )

    # Format the webhook request
    try:
        final_url, headers, formatted_payload = format_webhook_request(
            webhook_type_id=webhook_type,
            webhook_config=webhook_config,
            user_request=user_request,
            backend_fields=backend_fields,
        )
    except ValueError as e:
        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Failed to format webhook request",
            error=str(e),
        )

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                final_url,
                json=formatted_payload,
                headers=headers,
            )
            response.raise_for_status()

            stmt = insert(AgentInstance).values(
                id=agent_instance_id,
                user_agent_id=user_agent.id,
                user_id=user_id,
                status=AgentStatus.ACTIVE,
            )
            stmt = stmt.on_conflict_do_nothing(index_elements=["id"])

            db.execute(stmt)
            db.commit()

            return WebhookTriggerResponse(
                success=True,
                agent_instance_id=str(agent_instance_id),
                message="Webhook triggered successfully",
            )

    except httpx.ConnectError as e:
        error_str = str(e)
        # Check for URL format errors and provide clearer message
        if "Request URL is missing" in error_str:
            error_msg = error_str.replace("Request URL", "Webhook URL")
        else:
            error_msg = f"Unable to connect to webhook URL. Check URL is correct and webhook is running: {error_str}"

        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Unable to connect to webhook URL",
            error=error_msg,
        )
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            error_msg = "Authentication failed. Please check your webhook API key."
        elif e.response.status_code == 403:
            error_msg = "Access forbidden. Please verify your webhook API key has the correct permissions."
        elif e.response.status_code >= 500:
            if e.response.status_code == 530:
                # 530 is often used by proxy/tunnel services
                error_msg = "HTTP 530: Proxy/tunnel error. Check URL or try restarting tunnel service."
            else:
                error_msg = f"HTTP {e.response.status_code}: Webhook service error. Check if webhook is running or try restarting it."
        else:
            error_msg = (
                f"Webhook returned error status {e.response.status_code}: {str(e)}"
            )

        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Webhook request failed",
            error=error_msg,
        )
    except httpx.TimeoutException:
        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Webhook request timed out",
            error="Webhook timeout (30s). Check if service is running and URL is correct.",
        )
    except (httpx.RequestError, httpx.InvalidURL) as e:
        error_str = str(e)
        # Check for URL format errors and provide clearer message
        if "Request URL is missing" in error_str or "Invalid URL" in error_str:
            error_msg = error_str.replace("Request URL", "Webhook URL").replace(
                "request URL", "webhook URL"
            )
        else:
            error_msg = f"Request error: {error_str}"

        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Failed to trigger webhook",
            error=error_msg,
        )
    except Exception as e:
        return WebhookTriggerResponse(
            success=False,
            agent_instance_id=None,
            message="Unexpected error occurred",
            error=str(e),
        )


def get_user_agent_instances(db: Session, agent_id: UUID, user_id: UUID) -> list | None:
    """Get all instances for a specific user agent"""

    # Verify the user agent exists, belongs to the user, and is not deleted
    user_agent = (
        db.query(UserAgent)
        .filter(
            and_(
                UserAgent.id == agent_id,
                UserAgent.user_id == user_id,
                UserAgent.is_deleted.is_(False),
            )
        )
        .first()
    )

    if not user_agent:
        return None

    # Get all instances for this user agent with relationships loaded
    instances = (
        db.query(AgentInstance)
        .options(
            joinedload(AgentInstance.user_agent),
        )
        .filter(AgentInstance.user_agent_id == agent_id)
        .order_by(AgentInstance.started_at.desc())
        .all()
    )

    # Get all instance IDs for bulk message stats query
    instance_ids = [instance.id for instance in instances]

    # Get message stats for all instances in one efficient query
    message_stats = _get_instance_message_stats(db, instance_ids)

    # Format instances using the same helper function used by other endpoints
    return [_format_instance(instance, message_stats) for instance in instances]


def delete_user_agent(db: Session, agent_id: UUID, user_id: UUID) -> bool:
    """Soft delete a user agent and mark its instances as deleted, while removing messages"""

    # First verify the user agent exists, belongs to the user, and is not already deleted
    user_agent = (
        db.query(UserAgent)
        .filter(
            and_(
                UserAgent.id == agent_id,
                UserAgent.user_id == user_id,
                UserAgent.is_deleted.is_(False),
            )
        )
        .first()
    )

    if not user_agent:
        return False

    # Get all agent instances for this user agent
    agent_instances = (
        db.query(AgentInstance).filter(AgentInstance.user_agent_id == agent_id).all()
    )

    # For each agent instance, delete all messages (for privacy/storage)
    for instance in agent_instances:
        db.query(Message).filter(Message.agent_instance_id == instance.id).delete()

    # Mark all agent instances as DELETED
    db.query(AgentInstance).filter(AgentInstance.user_agent_id == agent_id).update(
        {"status": AgentStatus.DELETED}
    )

    # Soft delete the user agent
    user_agent.is_deleted = True
    user_agent.updated_at = datetime.now(timezone.utc)

    db.commit()

    return True


def _format_user_agent(user_agent: UserAgent, db: Session) -> dict:
    """Helper function to format a user agent with instance counts"""

    # Get instance counts
    instance_count = (
        db.query(func.count(AgentInstance.id))
        .filter(AgentInstance.user_agent_id == user_agent.id)
        .scalar()
    )

    active_instance_count = (
        db.query(func.count(AgentInstance.id))
        .filter(
            and_(
                AgentInstance.user_agent_id == user_agent.id,
                AgentInstance.status == AgentStatus.ACTIVE,
            )
        )
        .scalar()
    )

    waiting_instance_count = (
        db.query(func.count(AgentInstance.id))
        .filter(
            and_(
                AgentInstance.user_agent_id == user_agent.id,
                AgentInstance.status == AgentStatus.AWAITING_INPUT,
            )
        )
        .scalar()
    )

    completed_instance_count = (
        db.query(func.count(AgentInstance.id))
        .filter(
            and_(
                AgentInstance.user_agent_id == user_agent.id,
                AgentInstance.status == AgentStatus.COMPLETED,
            )
        )
        .scalar()
    )

    error_instance_count = (
        db.query(func.count(AgentInstance.id))
        .filter(
            and_(
                AgentInstance.user_agent_id == user_agent.id,
                AgentInstance.status.in_([AgentStatus.FAILED, AgentStatus.KILLED]),
            )
        )
        .scalar()
    )

    return {
        "id": str(user_agent.id),
        "name": user_agent.name,
        "webhook_type": user_agent.webhook_type,
        "webhook_config": user_agent.webhook_config,
        "is_active": user_agent.is_active,
        "created_at": user_agent.created_at,
        "updated_at": user_agent.updated_at,
        "instance_count": instance_count or 0,
        "active_instance_count": active_instance_count or 0,
        "waiting_instance_count": waiting_instance_count or 0,
        "completed_instance_count": completed_instance_count or 0,
        "error_instance_count": error_instance_count or 0,
    }
