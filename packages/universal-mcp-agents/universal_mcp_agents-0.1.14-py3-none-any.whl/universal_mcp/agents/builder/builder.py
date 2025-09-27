import json

from langchain_core.messages import HumanMessage
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.graph import END, START, StateGraph
from loguru import logger
from universal_mcp.tools.registry import ToolRegistry
from universal_mcp.types import ToolConfig
from langgraph.types import Command

from universal_mcp.agents.base import BaseAgent
from universal_mcp.agents.builder.prompts import (
    NEW_AGENT_PROMPT,
    MODIFY_AGENT_PROMPT,
)
from universal_mcp.agents.builder.state import Agent, BuilderState
from universal_mcp.agents.llm import load_chat_model
from universal_mcp.agents.shared.tool_node import build_tool_node_graph
from universal_mcp.agents.builder.helper import (
    _extract_tools_from_history,
    _clean_conversation_history,
    _merge_tool_configs,
)


class BuilderAgent(BaseAgent):
    def __init__(
        self,
        name: str,
        instructions: str,
        model: str,
        registry: ToolRegistry,
        memory: BaseCheckpointSaver | None = None,
        **kwargs,
    ):
        super().__init__(
            name=name,
            instructions=instructions,
            model=model,
            memory=memory,
            **kwargs,
        )
        self.registry = registry
        self.llm = load_chat_model(model, thinking=False)

    async def invoke(
        self,
        thread_id: str,
        user_input: dict,
    ):
        """
        Overrides BaseAgent.invoke to build or modify an agent.
        This is the primary entry point for the Builder Agent.
        """
        keys = ("userInput", "agent", "tools", "messages")
        userInput, agent_data, tools, messages = (user_input.get(k) for k in keys)
        agent = Agent(**agent_data) if agent_data else None

        await self.ainit()
        graph = self._graph

        initial_state = BuilderState(
            user_task=userInput,
            generated_agent=agent,
            tool_config=tools,
            messages=[],
        )

        if messages:
            initial_state["messages"] = [HumanMessage(content=json.dumps(messages))]
        elif not userInput and not agent:
             raise ValueError("Either 'user_input' or 'messages' must be provided for a new agent.")


        run_metadata = { "agent_name": self.name, "is_background_run": False }

        config = {
            "configurable": {"thread_id": thread_id},
            "metadata": run_metadata,
            "run_id": thread_id,
            "run_name" : self.name
        }

        final_state = await graph.ainvoke(initial_state, config=config)
        return final_state

    def _entry_point_router(self, state: BuilderState):
        """
        Determines the entry point of the graph based on the initial state.
        """
        if state.get("generated_agent"):
            logger.info("Routing to: modify_agent.")
            return "modify_agent"
        else:
            logger.info("Routing to: create_agent.")
            return "create_agent"

    async def _create_agent(self, state: BuilderState):
        """Generates a new agent profile from scratch."""
        if not state.get("user_task") and not state["messages"]:
            raise ValueError("To create a new agent, provide either a 'user_task' or 'messages'.")
        
        user_task = state.get("user_task") or "Not provided"
        conversation_history = []

        if state["messages"]:
            content_str = state["messages"][-1].content
            raw_history = json.loads(content_str)
            conversation_history = _clean_conversation_history(raw_history)

        prompt = NEW_AGENT_PROMPT.format(
            user_task=user_task,
            conversation_history=json.dumps(conversation_history, indent=2),
        )

        structured_llm = self.llm.with_structured_output(Agent)
        generated_agent = await structured_llm.ainvoke(prompt)
        
        logger.info(f"Successfully created new agent '{generated_agent.name}'.")

        return Command(
            update={"generated_agent": generated_agent},
            goto="create_or_update_tool_config",
        )

    async def _modify_agent(self, state: BuilderState):
        """Modifies an existing agent based on new user feedback and/or conversation."""
        existing_agent = state["generated_agent"]
        
        if not state.get("user_task") and not state["messages"]:
            raise ValueError("To modify an agent, provide either a 'user_task' or 'messages'.")
        
        modification_request = state.get("user_task") or "No direct modification request provided."
        
        conversation_history = []
        if state["messages"]:
            content_str = state["messages"][-1].content
            raw_history = json.loads(content_str)
            conversation_history = _clean_conversation_history(raw_history)

        prompt = MODIFY_AGENT_PROMPT.format(
            existing_instructions=existing_agent.instructions,
            modification_request=modification_request,
            conversation_history=json.dumps(conversation_history, indent=2),
        )

        structured_llm = self.llm.with_structured_output(Agent)
        modified_agent = await structured_llm.ainvoke(prompt)

        logger.info(f"Successfully modified agent '{modified_agent.name}'.")
        
        return Command(
            update={"generated_agent": modified_agent},
            goto="create_or_update_tool_config"
        )

    async def _get_tool_config_for_task(self, task: str) -> ToolConfig:
        """Helper method to find and configure tools for a given task string."""
        if not task:
            return {}
        tool_finder_graph = build_tool_node_graph(self.llm, self.registry)
        final_state = await tool_finder_graph.ainvoke({"original_task": task})
        return final_state.get("execution_plan") or {}

    async def _create_or_update_tool_config(self, state: BuilderState):
        """
        Creates or updates the tool configuration by synthesizing tools from multiple sources:
        1.  Existing tool config (if any).
        2.  Tools extracted from conversation history.
        3.  Tools inferred from the agent's primary instructions.
        4.  Tools inferred from the user's direct input/task.
        """
        # 1. Get the existing configuration, if it exists
        final_tool_config = state.get("tool_config") or {}
        
        # 2. Extract tools directly from the conversation history
        if state["messages"]:
            content_str = state["messages"][-1].content
            raw_history = json.loads(content_str)
            history_tool_config = _extract_tools_from_history(raw_history)
            final_tool_config = _merge_tool_configs(final_tool_config, history_tool_config)

        # 3. Find tools based on the agent's synthesized instructions (even if modifying)
        instructions_task = state["generated_agent"].instructions
        instructions_tool_config = await self._get_tool_config_for_task(instructions_task)
        final_tool_config = _merge_tool_configs(final_tool_config, instructions_tool_config)
        
        # 4. Find tools based on the direct user input (when creating a new agent)
        user_task = state.get("user_task")
        if user_task:
            user_task_tool_config = await self._get_tool_config_for_task(user_task)
            final_tool_config = _merge_tool_configs(final_tool_config, user_task_tool_config)

        logger.info(f"Final synthesized tool configuration: {final_tool_config}")

        return Command(
            update={"tool_config": final_tool_config},
            goto=END,
        )

    async def _build_graph(self):
        """Builds the conversational agent graph."""
        builder = StateGraph(BuilderState)

        builder.add_node("create_agent", self._create_agent)
        builder.add_node("modify_agent", self._modify_agent)
        builder.add_node("create_or_update_tool_config", self._create_or_update_tool_config)

        builder.add_conditional_edges(
            START,
            self._entry_point_router,
        )

        return builder.compile(checkpointer=self.memory)