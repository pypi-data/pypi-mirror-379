from typing import Any, Dict, List
from maia_test_framework.core.mcp.base import BaseMCPServer
from maia_test_framework.core.tools.base import BaseTool

class StubbedMCPServer(BaseMCPServer):
    """A stubbed MCP server that wraps a list of BaseTool objects."""

    def __init__(self, name: str, tools: List[BaseTool]):
        super().__init__(name)
        self._tools = {tool.name: tool for tool in tools}

    async def get_all_tool_schemas(self) -> List[Dict[str, Any]]:
        """Return the schemas of all tools available on the server."""
        return [tool.get_schema() for tool in self._tools.values()]

    async def execute_tool(self, tool_name: str, **kwargs) -> Any:
        """Execute a tool by name with given parameters."""
        if tool_name not in self._tools:
            raise ValueError(f"Tool '{tool_name}' not found on this MCP server.")
        tool = self._tools[tool_name]
        return await tool.execute(**kwargs)

    async def has_tool(self, tool_name: str) -> bool:
        """Check if a tool exists on the server."""
        return tool_name in self._tools
