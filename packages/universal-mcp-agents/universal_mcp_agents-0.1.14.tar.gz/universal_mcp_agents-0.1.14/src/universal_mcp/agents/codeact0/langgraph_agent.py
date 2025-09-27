import asyncio

from langgraph.checkpoint.memory import MemorySaver
from rich import print
from universal_mcp.agentr.registry import AgentrRegistry

from universal_mcp.agents.codeact0.agent import CodeActAgent
from universal_mcp.agents.utils import messages_to_list
async def agent():
    agent_obj = CodeActAgent(
            name="CodeAct Agent",
            instructions="Be very concise in your answers.",
            model="anthropic:claude-4-sonnet-20250514",
            tools={"google_calendar": ["get_upcoming_events"], "exa" : ["search_with_filters"]},
            registry=AgentrRegistry()
        )
    return await agent_obj._build_graph()