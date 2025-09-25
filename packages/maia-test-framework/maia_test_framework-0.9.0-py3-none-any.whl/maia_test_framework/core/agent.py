# maia_test_framework/core/agent.py
import json
import re
from typing import List
from maia_test_framework.core.message import Message, AgentResponse
from maia_test_framework.providers.base import BaseProvider
from maia_test_framework.core.tools.base import BaseTool
from maia_test_framework.core.mcp.base import BaseMCPServer

class Agent:
    def __init__(self, name: str, provider: BaseProvider, system_message: str = "", ignore_trigger_prompt: str = "", tools: List[BaseTool] = None, mcp_servers: List[BaseMCPServer] = None):
        self.name = name
        self.provider = provider
        self.system_message = system_message
        self.ignore_trigger_prompt = ignore_trigger_prompt
        self.tools = tools or []
        self.mcp_servers = mcp_servers or []

    async def _format_tools_prompt(self):
        tool_schemas = []

        # Local tools
        if self.tools:
            tool_schemas.extend([tool.get_schema() for tool in self.tools])

        # MCP server tools
        if self.mcp_servers:
            for server in self.mcp_servers:
                server_schemas = await server.get_all_tool_schemas()
                tool_schemas.extend(server_schemas)

        if not tool_schemas:
            return ""
        
        prompt = """
You have access to the following tools. To use a tool, you must respond with a JSON object with the following structure:
{
    "tool_call": {
        "name": "<tool_name>",
        "parameters": {
            "<parameter_name>": "<parameter_value>"
        }
    }
}

Here are the available tools:
"""
        prompt += json.dumps(tool_schemas, indent=2)
        return prompt

    async def generate_response(self, history: List[Message]) -> AgentResponse:
        tools_prompt = await self._format_tools_prompt()
        system_message = self.system_message + tools_prompt
        
        response = await self.provider.base_generate(
            history=history,
            system_message=system_message,
            ignore_trigger_prompt=self.ignore_trigger_prompt
        )

        def extract_tool_call(text):
            # Normalize smart quotes, casing of "json"
            text = text.replace("’", "'").replace("“", '"').replace("”", '"')
            
            # Capture everything inside the fenced ```json ... ```
            fenced = re.search(r"```(?:json|JSON)(.*?)```", text, re.DOTALL)
            if fenced:
                candidate = fenced.group(1).strip()
            else:
                # Fallback: capture object containing "tool_call"
                match = re.search(r'\{[\s\S]*"tool_call"[\s\S]*\}', text)
                candidate = match.group(0).strip() if match else None
            
            if not candidate:
                return None
            
            try:
                return json.loads(candidate)
            except json.JSONDecodeError as e:
                print("JSON parse error:", e)
                print("Extracted string:\n", candidate)
                return None


        try:
            response_data = extract_tool_call(response.content)
            if response_data and "tool_call" in response_data:
                tool_call = response_data["tool_call"]
                tool_name = tool_call["name"]
                tool_params = tool_call["parameters"]

                tool_result = None
                tool_found = False
                tool_source = None  # 'local' or 'mcp'
                source_server = None

                # 1. Search local tools
                tool_to_use = next((tool for tool in self.tools if tool.name == tool_name), None)
                if tool_to_use:
                    tool_result = await tool_to_use.execute(**tool_params)
                    tool_found = True
                    tool_source = 'local'
                
                # 2. If not found, search MCP servers
                if not tool_found and self.mcp_servers:
                    for server in self.mcp_servers:
                        if await server.has_tool(tool_name):
                            tool_result = await server.execute_tool(tool_name, **tool_params)
                            tool_found = True
                            tool_source = 'mcp'
                            source_server = server
                            break

                if tool_found:
                    if tool_source == 'local':
                        history.append(Message(sender=self.name, sender_type="agent", receiver=tool_call["name"], receiver_type="tool", content=response.content))
                        history.append(Message(sender=tool_call["name"], sender_type="tool", receiver=self.name, receiver_type="agent", content=json.dumps({"tool_output": tool_result})))
                    elif tool_source == 'mcp' and source_server:
                        history.append(Message(
                            sender=self.name,
                            sender_type="agent",
                            receiver=source_server.name,
                            receiver_type="mcp_server",
                            content=response.content,
                            metadata={"tool_name": tool_call["name"]}
                        ))
                        history.append(Message(
                            sender=source_server.name,
                            sender_type="mcp_server",
                            receiver=self.name, 
                            receiver_type="agent",
                            content=json.dumps({"tool_output": tool_result}),
                            metadata={"tool_name": tool_call["name"]}
                        ))

                    # Second call to LLM with tool result
                    return await self.provider.base_generate(
                        history=history,
                        system_message=system_message,
                        ignore_trigger_prompt=self.ignore_trigger_prompt
                    )
        except (json.JSONDecodeError, KeyError):
            # Not a tool call, return original response
            pass

        return response
