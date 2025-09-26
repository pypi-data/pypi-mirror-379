from vector_bridge import VectorBridgeClient
from vector_bridge.schema.chat import Chat, ChatsList
from vector_bridge.schema.errors.chat import raise_for_chat_detail


class ChatClient:
    """Client for chat management endpoints."""

    def __init__(self, client: VectorBridgeClient):
        self.client = client

    def fetch_chats_for_my_organization(
        self, integration_name: str | None = None, limit: int = 50, offset: int = 0
    ) -> ChatsList:
        """
        Retrieve a list of chat sessions associated with the organization.

        Args:
            integration_name: The name of the integration
            limit: Number of chat records to return
            offset: Starting point for fetching records

        Returns:
            ChatsList with chats and pagination info
        """
        if integration_name is None:
            integration_name = self.client.integration_name

        url = f"{self.client.base_url}/v1/chats"
        params = {
            "integration_name": integration_name,
            "limit": limit,
            "offset": offset,
        }
        headers = self.client._get_auth_headers()
        response = self.client.session.get(url, headers=headers, params=params)
        result = self.client._handle_response(response=response, error_callable=raise_for_chat_detail)
        return ChatsList.model_validate(result)

    def fetch_my_chats(self, integration_name: str | None = None, limit: int = 50, offset: int = 0) -> ChatsList:
        """
        Retrieve a list of chat sessions for the current user.

        Args:
            integration_name: The name of the integration
            limit: Number of chat records to return
            offset: Starting point for fetching records

        Returns:
            ChatsList with chats and pagination info
        """
        if integration_name is None:
            integration_name = self.client.integration_name

        url = f"{self.client.base_url}/v1/chats/me"
        params = {
            "integration_name": integration_name,
            "limit": limit,
            "offset": offset,
        }
        headers = self.client._get_auth_headers()
        response = self.client.session.get(url, headers=headers, params=params)
        result = self.client._handle_response(response=response, error_callable=raise_for_chat_detail)
        return ChatsList.model_validate(result)

    def delete_chat(self, chat_id: str, integration_name: str | None = None) -> None:
        """
        Delete a chat session between the organization and a specific user.

        Args:
            chat_id: The unique identifier of the user
            integration_name: The name of the integration
        """
        if integration_name is None:
            integration_name = self.client.integration_name

        url = f"{self.client.base_url}/v1/chat/delete/{chat_id}"
        params = {"integration_name": integration_name}
        headers = self.client._get_auth_headers()
        response = self.client.session.delete(url, headers=headers, params=params)
        if response.status_code != 204:
            self.client._handle_response(response=response, error_callable=raise_for_chat_detail)

    def create_chat(self, chat_id: str, title: str = "New Chat", integration_name: str | None = None) -> Chat:
        """
        Create a new chat session between the organization and a specific user.

        Args:
            chat_id: Unique identifier of the user
            title: Title for the new chat
            integration_name: Name of the integration

        Returns:
            Chat: The newly created chat session
        """
        if integration_name is None:
            integration_name = self.client.integration_name

        url = f"{self.client.base_url}/v1/chat/create/{chat_id}"
        params = {
            "integration_name": integration_name,
            "title": title,
        }
        headers = self.client._get_auth_headers()
        response = self.client.session.post(url, headers=headers, params=params)
        result = self.client._handle_response(response=response, error_callable=raise_for_chat_detail)
        return Chat.model_validate(result)
