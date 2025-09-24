"""Tests for agent endpoints."""

from datetime import datetime, timezone
from uuid import uuid4

from shared.database.models import (
    User,
    UserAgent,
    AgentInstance,
    UserInstanceAccess,
)
from shared.database.enums import AgentStatus, InstanceAccessLevel
from backend.main import app
from backend.auth.dependencies import get_current_user, get_optional_current_user


class TestAgentEndpoints:
    """Test agent management endpoints."""

    def test_list_agent_types(
        self, authenticated_client, test_user_agent, test_agent_instance
    ):
        """Test listing agent types with instances."""
        response = authenticated_client.get("/api/v1/agent-types")
        assert response.status_code == 200
        data = response.json()

        assert len(data) == 1
        agent_type = data[0]
        assert agent_type["id"] == str(test_user_agent.id)
        assert agent_type["name"] == "claude code"
        assert len(agent_type["recent_instances"]) == 1
        assert agent_type["recent_instances"][0]["id"] == str(test_agent_instance.id)

    def test_list_agent_types_multiple_users(
        self, authenticated_client, test_db, test_user_agent
    ):
        """Test that users only see their own agent types."""
        # Create another user with agent
        other_user = User(
            id=uuid4(),
            email="other@example.com",
            display_name="Other User",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(other_user)

        other_user_agent = UserAgent(
            id=uuid4(),
            user_id=other_user.id,
            name="cursor",
            is_active=True,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(other_user_agent)
        test_db.commit()

        response = authenticated_client.get("/api/v1/agent-types")
        assert response.status_code == 200
        data = response.json()

        # Should only see own agent type
        assert len(data) == 1
        assert data[0]["name"] == "claude code"

    def test_list_agent_types_with_pending_questions(
        self, authenticated_client, test_db, test_user, test_user_agent
    ):
        """Test agent types listing with pending questions (catches timezone issues)."""
        # Create an agent instance
        instance = AgentInstance(
            id=uuid4(),
            user_agent_id=test_user_agent.id,
            user_id=test_user.id,
            status=AgentStatus.AWAITING_INPUT,
            started_at=datetime.now(timezone.utc),
        )
        test_db.add(instance)

        # Create a message with requires_user_input=True to simulate a question
        from shared.database import Message, SenderType

        question_msg = Message(
            id=uuid4(),
            agent_instance_id=instance.id,
            sender_type=SenderType.AGENT,
            content="Test question?",
            requires_user_input=True,
            created_at=datetime.now(timezone.utc),
        )
        test_db.add(question_msg)
        test_db.commit()

        # This should not raise a timezone error
        response = authenticated_client.get("/api/v1/agent-types")
        assert response.status_code == 200
        data = response.json()

        assert len(data) == 1
        agent_type = data[0]
        assert len(agent_type["recent_instances"]) == 1

        # Check that the instance has AWAITING_INPUT status
        instance_data = agent_type["recent_instances"][0]
        assert instance_data["status"] == "AWAITING_INPUT"
        assert instance_data["latest_message"] == "Test question?"

    def test_list_all_agent_instances(self, authenticated_client, test_agent_instance):
        """Test listing all agent instances."""
        response = authenticated_client.get("/api/v1/agent-instances")
        assert response.status_code == 200
        data = response.json()

        assert len(data) == 1
        instance = data[0]
        assert instance["id"] == str(test_agent_instance.id)
        assert instance["status"] == "ACTIVE"

    def test_list_shared_agent_instances(
        self, authenticated_client, test_db, test_user, test_agent_instance
    ):
        """Test listing agent instances shared with the user."""
        owner = User(
            id=uuid4(),
            email="owner@example.com",
            display_name="Owner User",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(owner)

        owner_agent = UserAgent(
            id=uuid4(),
            user_id=owner.id,
            name="shared agent",
            is_active=True,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(owner_agent)

        shared_instance = AgentInstance(
            id=uuid4(),
            user_agent_id=owner_agent.id,
            user_id=owner.id,
            status=AgentStatus.COMPLETED,
            started_at=datetime.now(timezone.utc),
        )
        test_db.add(shared_instance)
        test_db.flush()

        access = UserInstanceAccess(
            agent_instance_id=shared_instance.id,
            shared_email=test_user.email,
            user_id=test_user.id,
            access=InstanceAccessLevel.READ,
            granted_by_user_id=owner.id,
        )
        test_db.add(access)
        test_db.commit()

        response = authenticated_client.get("/api/v1/agent-instances?scope=shared")
        assert response.status_code == 200
        data = response.json()

        assert len(data) == 1
        assert data[0]["id"] == str(shared_instance.id)

        # Ensure own instances aren't included when requesting shared scope
        ids = {item["id"] for item in data}
        assert str(test_agent_instance.id) not in ids

    def test_list_all_scope_includes_owned_and_shared(
        self, authenticated_client, test_db, test_user, test_agent_instance
    ):
        """Test that the 'all' scope includes both owned and shared instances."""
        owner = User(
            id=uuid4(),
            email="another-owner@example.com",
            display_name="Another Owner",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(owner)

        owner_agent = UserAgent(
            id=uuid4(),
            user_id=owner.id,
            name="analysis agent",
            is_active=True,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(owner_agent)

        shared_instance = AgentInstance(
            id=uuid4(),
            user_agent_id=owner_agent.id,
            user_id=owner.id,
            status=AgentStatus.ACTIVE,
            started_at=datetime.now(timezone.utc),
        )
        test_db.add(shared_instance)
        test_db.flush()

        access = UserInstanceAccess(
            agent_instance_id=shared_instance.id,
            shared_email=test_user.email,
            user_id=test_user.id,
            access=InstanceAccessLevel.WRITE,
            granted_by_user_id=owner.id,
        )
        test_db.add(access)
        test_db.commit()

        response = authenticated_client.get("/api/v1/agent-instances?scope=all")
        assert response.status_code == 200
        data = response.json()

        ids = {item["id"] for item in data}
        assert str(test_agent_instance.id) in ids
        assert str(shared_instance.id) in ids

    def test_get_instance_detail_shared_access(
        self, client, test_db, test_agent_instance, test_user
    ):
        """Shared users with read access can view instance detail."""
        other_user = User(
            id=uuid4(),
            email="shared@example.com",
            display_name="Shared User",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(other_user)
        test_db.flush()

        share = UserInstanceAccess(
            agent_instance_id=test_agent_instance.id,
            shared_email=other_user.email,
            user_id=other_user.id,
            access=InstanceAccessLevel.READ,
            granted_by_user_id=test_user.id,
        )
        test_db.add(share)
        test_db.commit()

        def override_user():
            return other_user

        app.dependency_overrides[get_current_user] = override_user
        app.dependency_overrides[get_optional_current_user] = override_user

        try:
            response = client.get(f"/api/v1/agent-instances/{test_agent_instance.id}")
        finally:
            app.dependency_overrides.pop(get_current_user, None)
            app.dependency_overrides.pop(get_optional_current_user, None)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == str(test_agent_instance.id)
        assert data["access_level"] == "READ"

    def test_get_instance_messages_shared_access(
        self, client, test_db, test_agent_instance, test_user
    ):
        """Shared users can read messages for an instance."""
        other_user = User(
            id=uuid4(),
            email="shared-messages@example.com",
            display_name="Shared Messages",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        test_db.add(other_user)
        test_db.flush()

        access = UserInstanceAccess(
            agent_instance_id=test_agent_instance.id,
            shared_email=other_user.email,
            user_id=other_user.id,
            access=InstanceAccessLevel.READ,
            granted_by_user_id=test_user.id,
        )
        test_db.add(access)
        test_db.commit()

        def override_user_messages():
            return other_user

        app.dependency_overrides[get_current_user] = override_user_messages
        app.dependency_overrides[get_optional_current_user] = override_user_messages

        try:
            response = client.get(
                f"/api/v1/agent-instances/{test_agent_instance.id}/messages"
            )
        finally:
            app.dependency_overrides.pop(get_current_user, None)
            app.dependency_overrides.pop(get_optional_current_user, None)

        assert response.status_code == 200
        assert response.json() == []

    def test_list_instance_access_includes_owner(
        self, authenticated_client, test_db, test_agent_instance
    ):
        """Listing access returns the owner entry."""
        response = authenticated_client.get(
            f"/api/v1/agent-instances/{test_agent_instance.id}/access"
        )
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        owner_entry = data[0]
        assert owner_entry["is_owner"] is True
        assert owner_entry["access"] == "WRITE"

    def test_add_and_remove_instance_share(
        self, authenticated_client, test_db, test_agent_instance, test_user
    ):
        """Owner can add and remove shared users."""
        payload = {"email": "new-share@example.com", "access": "READ"}
        response = authenticated_client.post(
            f"/api/v1/agent-instances/{test_agent_instance.id}/access",
            json=payload,
        )
        assert response.status_code == 200
        share_data = response.json()
        assert share_data["email"] == payload["email"]
        assert share_data["access"] == "READ"
        assert share_data["is_owner"] is False

        share_id = share_data["id"]

        # Refresh the list and ensure share is present alongside owner
        list_response = authenticated_client.get(
            f"/api/v1/agent-instances/{test_agent_instance.id}/access"
        )
        assert list_response.status_code == 200
        entries = list_response.json()
        assert any(entry["id"] == share_id for entry in entries)

        delete_response = authenticated_client.delete(
            f"/api/v1/agent-instances/{test_agent_instance.id}/access/{share_id}"
        )
        assert delete_response.status_code == 200

        # Ensure share is actually removed
        remaining = authenticated_client.get(
            f"/api/v1/agent-instances/{test_agent_instance.id}/access"
        )
        assert remaining.status_code == 200
        assert all(entry["id"] != share_id for entry in remaining.json())
        assert (
            test_db.query(UserInstanceAccess)
            .filter(UserInstanceAccess.agent_instance_id == test_agent_instance.id)
            .count()
            == 0
        )

    def test_list_agent_instances_with_limit(
        self, authenticated_client, test_db, test_user, test_user_agent
    ):
        """Test listing agent instances with limit."""
        # Create multiple instances
        for i in range(5):
            instance = AgentInstance(
                id=uuid4(),
                user_agent_id=test_user_agent.id,
                user_id=test_user.id,
                status=AgentStatus.COMPLETED,
                started_at=datetime.now(timezone.utc),
            )
            test_db.add(instance)
        test_db.commit()

        response = authenticated_client.get("/api/v1/agent-instances?limit=3")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3

    def test_get_agent_summary(
        self,
        authenticated_client,
        test_db,
        test_user,
        test_user_agent,
        test_agent_instance,
    ):
        """Test getting agent summary."""
        # Add more instances with different statuses
        completed_instance = AgentInstance(
            id=uuid4(),
            user_agent_id=test_user_agent.id,
            user_id=test_user.id,
            status=AgentStatus.COMPLETED,
            started_at=datetime.now(timezone.utc),
            ended_at=datetime.now(timezone.utc),
        )
        test_db.add(completed_instance)

        # Add a message with requires_user_input to the active instance
        from shared.database import Message, SenderType

        question_msg = Message(
            id=uuid4(),
            agent_instance_id=test_agent_instance.id,
            sender_type=SenderType.AGENT,
            content="Test question?",
            requires_user_input=True,
            created_at=datetime.now(timezone.utc),
        )
        test_db.add(question_msg)
        test_agent_instance.status = AgentStatus.AWAITING_INPUT
        test_db.commit()

        response = authenticated_client.get("/api/v1/agent-summary")
        assert response.status_code == 200
        data = response.json()

        assert data["total_instances"] == 2
        assert data["active_instances"] == 0  # AWAITING_INPUT doesn't count as active
        assert data["completed_instances"] == 1
        assert "agent_types" in data
        assert len(data["agent_types"]) == 1

    def test_get_type_instances(
        self, authenticated_client, test_user_agent, test_agent_instance
    ):
        """Test getting instances for a specific agent type."""
        response = authenticated_client.get(
            f"/api/v1/agent-types/{test_user_agent.id}/instances"
        )
        assert response.status_code == 200
        data = response.json()

        assert len(data) == 1
        assert data[0]["id"] == str(test_agent_instance.id)

    def test_get_type_instances_not_found(self, authenticated_client):
        """Test getting instances for non-existent agent type."""
        fake_id = uuid4()
        response = authenticated_client.get(f"/api/v1/agent-types/{fake_id}/instances")
        assert response.status_code == 404
        assert response.json()["detail"] == "Agent type not found"

    def test_get_instance_detail(
        self, authenticated_client, test_db, test_agent_instance
    ):
        """Test getting detailed agent instance information."""
        # Add messages to simulate conversation
        from shared.database import Message, SenderType

        msg1 = Message(
            id=uuid4(),
            agent_instance_id=test_agent_instance.id,
            sender_type=SenderType.AGENT,
            content="First step completed",
            requires_user_input=False,
            created_at=datetime.now(timezone.utc),
        )
        msg2 = Message(
            id=uuid4(),
            agent_instance_id=test_agent_instance.id,
            sender_type=SenderType.AGENT,
            content="Need input?",
            requires_user_input=True,
            created_at=datetime.now(timezone.utc),
        )
        msg3 = Message(
            id=uuid4(),
            agent_instance_id=test_agent_instance.id,
            sender_type=SenderType.USER,
            content="Great work!",
            requires_user_input=False,
            created_at=datetime.now(timezone.utc),
        )

        test_db.add_all([msg1, msg2, msg3])
        test_db.commit()

        response = authenticated_client.get(
            f"/api/v1/agent-instances/{test_agent_instance.id}"
        )
        assert response.status_code == 200
        data = response.json()

        assert data["id"] == str(test_agent_instance.id)
        assert "messages" in data
        assert len(data["messages"]) == 3
        assert data["messages"][0]["content"] == "First step completed"
        assert data["messages"][0]["sender_type"] == "AGENT"
        assert data["messages"][1]["content"] == "Need input?"
        assert data["messages"][1]["requires_user_input"] is True
        assert data["messages"][2]["content"] == "Great work!"
        assert data["messages"][2]["sender_type"] == "USER"

    def test_get_instance_detail_not_found(self, authenticated_client):
        """Test getting non-existent instance detail."""
        fake_id = uuid4()
        response = authenticated_client.get(f"/api/v1/agent-instances/{fake_id}")
        assert response.status_code == 404
        assert response.json()["detail"] == "Agent instance not found"

    def test_add_user_feedback(
        self, authenticated_client, test_db, test_agent_instance
    ):
        """Test adding user feedback to an agent instance."""
        feedback_text = "Please use TypeScript for this component"
        response = authenticated_client.post(
            f"/api/v1/agent-instances/{test_agent_instance.id}/messages",
            json={"content": feedback_text},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["content"] == feedback_text
        assert data["sender_type"] == "USER"
        assert "id" in data
        assert "created_at" in data
        assert data["requires_user_input"] is False

        # Verify in database
        from shared.database import Message, SenderType

        message = (
            test_db.query(Message)
            .filter_by(
                agent_instance_id=test_agent_instance.id, sender_type=SenderType.USER
            )
            .first()
        )
        assert message is not None
        assert message.content == feedback_text
        assert message.sender_type == SenderType.USER

    def test_add_feedback_to_nonexistent_instance(self, authenticated_client):
        """Test adding feedback to non-existent instance."""
        fake_id = uuid4()
        response = authenticated_client.post(
            f"/api/v1/agent-instances/{fake_id}/messages",
            json={"content": "Test feedback"},
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "Agent instance not found"

    def test_instance_status_changes_with_messages(
        self, authenticated_client, test_db, test_agent_instance
    ):
        """Test that instance status changes based on message flow."""
        from shared.database import Message, SenderType

        # Initially instance should be ACTIVE
        assert test_agent_instance.status == AgentStatus.ACTIVE

        # Agent sends a message requiring user input
        question_msg = Message(
            id=uuid4(),
            agent_instance_id=test_agent_instance.id,
            sender_type=SenderType.AGENT,
            content="Should I use TypeScript or JavaScript?",
            requires_user_input=True,
            created_at=datetime.now(timezone.utc),
        )
        test_db.add(question_msg)
        test_db.commit()

        # Status should change to AWAITING_INPUT (this would be done by the agent)
        test_agent_instance.status = AgentStatus.AWAITING_INPUT
        test_db.commit()

        # User responds
        response = authenticated_client.post(
            f"/api/v1/agent-instances/{test_agent_instance.id}/messages",
            json={"content": "Use TypeScript for better type safety"},
        )
        assert response.status_code == 200

        # Check that status changed back to ACTIVE
        test_db.refresh(test_agent_instance)
        assert test_agent_instance.status == AgentStatus.ACTIVE

    def test_message_creates_status_update_notification(
        self, authenticated_client, test_db, test_agent_instance
    ):
        """Test that sending messages triggers appropriate notifications."""
        # This would test the notification system if implemented
        # For now, just verify message creation works
        response = authenticated_client.post(
            f"/api/v1/agent-instances/{test_agent_instance.id}/messages",
            json={"content": "Test message for notifications"},
        )
        assert response.status_code == 200

        # Verify message was created
        from shared.database import Message

        messages = (
            test_db.query(Message)
            .filter_by(agent_instance_id=test_agent_instance.id)
            .all()
        )
        assert len(messages) >= 1
        assert any(msg.content == "Test message for notifications" for msg in messages)

    def test_agent_instance_latest_message_tracking(
        self, authenticated_client, test_db, test_agent_instance
    ):
        """Test that latest_message is properly tracked in instance listing."""
        from shared.database import Message, SenderType
        import time

        # Create messages with different timestamps
        msg1 = Message(
            id=uuid4(),
            agent_instance_id=test_agent_instance.id,
            sender_type=SenderType.AGENT,
            content="First message",
            requires_user_input=False,
            created_at=datetime.now(timezone.utc),
        )
        test_db.add(msg1)
        test_db.commit()

        # Small delay to ensure different timestamps
        time.sleep(0.1)

        msg2 = Message(
            id=uuid4(),
            agent_instance_id=test_agent_instance.id,
            sender_type=SenderType.USER,
            content="Latest message",
            requires_user_input=False,
            created_at=datetime.now(timezone.utc),
        )
        test_db.add(msg2)
        test_db.commit()

        # Get instance list
        response = authenticated_client.get("/api/v1/agent-instances")
        assert response.status_code == 200
        data = response.json()

        assert len(data) == 1
        instance = data[0]
        assert instance["latest_message"] == "Latest message"
        assert instance["chat_length"] == 2
