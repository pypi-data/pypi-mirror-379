import asyncio
from typing import Any, Dict, List, Optional

from mcp.client.session import ClientSession
from mcp.client.sse import sse_client

from maia_test_framework.core.mcp.base import BaseMCPServer

class SSEMCPServer(BaseMCPServer):
    """
    An MCP server that communicates over streamable HTTP, using the `mcp` client library for SSE.
    """

    def __init__(self, name: str, base_url: str, token: Optional[str] = None, protocol_version: str = "2025-06-18"):
        super().__init__(name)
        self.base_url = base_url.rstrip('/')
        self._headers: Dict[str, str] = {}
        if token:
            self._headers["Authorization"] = f"Bearer {token}"

        # The protocol_version is likely handled by the mcp library itself.
        self._protocol_version = protocol_version
        
        self._init_lock = asyncio.Lock()
        self._initialized = False
        
        self._mcp_session: Optional[ClientSession] = None
        self._sse_cm = None
        self._session_cm = None
        
        self._schemas: Optional[List[Dict[str, Any]]] = None

    async def initialize(self):
        async with self._init_lock:
            if self._initialized:
                return

            self._sse_cm = sse_client(self.base_url, headers=self._headers)
            read_stream, write_stream = await self._sse_cm.__aenter__()
            
            self._session_cm = ClientSession(read_stream, write_stream)
            self._mcp_session = await self._session_cm.__aenter__()

            await self._mcp_session.initialize()
            self._initialized = True

    async def close(self):
        if self._session_cm:
            await self._session_cm.__aexit__(None, None, None)
        if self._sse_cm:
            await self._sse_cm.__aexit__(None, None, None)
        self._initialized = False
        self._mcp_session = None

    async def get_all_tool_schemas(self) -> List[Dict[str, Any]]:
        if not self._initialized or not self._mcp_session:
            await self.initialize()
        
        if self._schemas is None:
            if not self._mcp_session:
                raise ConnectionError("MCP session not initialized.")
            tools_response = await self._mcp_session.list_tools()
            self._schemas = [tool.model_dump() for tool in tools_response.tools]
        
        return self._schemas

    async def has_tool(self, tool_name: str) -> bool:
        schemas = await self.get_all_tool_schemas()
        return any(schema['name'] == tool_name for schema in schemas)

    async def execute_tool(self, tool_name: str, **kwargs) -> Any:
        if not self._initialized or not self._mcp_session:
            await self.initialize()
        
        if not self._mcp_session:
            raise ConnectionError("MCP session not initialized.")

        result = await self._mcp_session.call_tool(name=tool_name, arguments=kwargs)
        
        if result and hasattr(result, 'content') and isinstance(result.content, list) and len(result.content) > 0:
            first_content = result.content[0]
            if hasattr(first_content, 'type') and first_content.type == 'text' and hasattr(first_content, 'text'):
                return first_content.text
        
        return result


