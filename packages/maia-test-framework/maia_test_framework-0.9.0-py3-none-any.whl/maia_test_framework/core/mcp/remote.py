import aiohttp
import asyncio
import uuid
from typing import Any, Dict, List, Optional

from maia_test_framework.core.mcp.base import BaseMCPServer

class RemoteMCPServer(BaseMCPServer):
    def __init__(self, name: str, base_url: str, token: Optional[str] = None, protocol_version: str = "2025-06-18"):
        super().__init__(name)
        self.base_url = base_url.rstrip('/')
        self._headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if token:
            self._headers["Authorization"] = f"Bearer {token}"
            self._headers["x-mcp-proxy-auth"] = f"Bearer {token}"

        self._protocol_version = protocol_version
        self._session_id = str(uuid.uuid4())
        self._schemas: Optional[List[Dict[str, Any]]] = None
        self._tool_names: Optional[set] = None
        self._session: Optional[aiohttp.ClientSession] = None
        self._id_counter = 1
        self._init_lock = asyncio.Lock()
        self._initialized = False

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(headers=self._headers)
        return self._session

    async def _send_rpc(self, method: str, params: Optional[Dict[str, Any]] = None, is_notification: bool = False) -> Optional[Dict[str, Any]]:
        session = await self._get_session()
        payload: Dict[str, Any] = {
            "jsonrpc": "2.0",
            "method": method,
        }
        if params:
            payload["params"] = params

        if not is_notification:
            request_id = self._id_counter
            self._id_counter += 1
            payload["id"] = request_id
        
        url = f"{self.base_url}/message?sessionId={self._session_id}"

        async with session.post(url, json=payload) as response:
            response.raise_for_status()
            if not is_notification:
                response_data = await response.json()
                if response_data.get("id") != request_id:
                    raise ConnectionError("Invalid JSON-RPC response ID.")
                if "error" in response_data:
                    raise ConnectionError(f"JSON-RPC error: {response_data['error']}")
                return response_data.get("result")
        return None

    async def _do_initialize(self):
        init_params = {
            "protocolVersion": self._protocol_version,
            "capabilities": {},
            "clientInfo": {
                "name": "maia-test-framework",
            }
        }
        await self._send_rpc("initialize", init_params)

        await self._send_rpc("notifications/initialized", is_notification=True)

        tools_response = await self._send_rpc("tools/list")
        if tools_response and "tools" in tools_response:
            self._schemas = tools_response["tools"]
            self._tool_names = {schema['name'] for schema in self._schemas}
        else:
            self._schemas = []
            self._tool_names = set()
        
        self._initialized = True

    async def initialize(self):
        """
        Performs the MCP initialization handshake and fetches tool schemas.
        """
        async with self._init_lock:
            if self._initialized:
                return
            await self._do_initialize()

    async def get_all_tool_schemas(self) -> List[Dict[str, Any]]:
        """Returns the cached list of tool schemas."""
        if not self._initialized:
            await self.initialize()
        return self._schemas or []

    async def has_tool(self, tool_name: str) -> bool:
        """Checks if a tool name exists in the cached set."""
        if not self._initialized:
            await self.initialize()
        return tool_name in (self._tool_names or set())

    async def execute_tool(self, tool_name: str, **kwargs) -> Any:
        """Executes a tool remotely via a JSON-RPC 'tools/call' request."""
        if not await self.has_tool(tool_name):
            raise ValueError(f"Tool '{tool_name}' not found on remote MCP server.")

        params = {
            "name": tool_name,
            "arguments": kwargs
        }
        result = await self._send_rpc("tools/call", params)
        
        if result and "content" in result and isinstance(result["content"], list) and len(result["content"]) > 0:
            first_content = result["content"][0]
            if first_content.get("type") == "text" and "text" in first_content:
                return first_content["text"]

        return result

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()