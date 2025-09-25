from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseMCPServer(ABC):
    """Base class for all MCP servers"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def get_all_tool_schemas(self) -> List[Dict[str, Any]]:
        """Return the schemas of all tools available on the server."""
        pass

    @abstractmethod
    async def execute_tool(self, tool_name: str, **kwargs) -> Any:
        """Execute a tool by name with given parameters."""
        pass

    @abstractmethod
    async def has_tool(self, tool_name: str) -> bool:
        """Check if a tool exists on the server."""
        pass
