from re import A


NEW_AGENT_PROMPT = """
....

"""


MODIFY_AGENT_PROMPT = """
....
"""


def generate_agent(
    user_input=None, messages: list[dict] | None = None, agent: Agent | None = None, tools: ToolConfig | None = None
):
    if agent:
        new_agent = _modify_agent(user_input, messages, agent)
    else:
        new_agent = _generate_agent(user_input, messages)

    return new_agent


async def _modify_agent(
    user_input,
    messages,
    agent,
):
    prompt = MODIFY_AGENT_PROMPT
    prompt += f"\n\nUser Input: {user_input}"
    prompt += f"\n\nMessages: {messages}"
    prompt += f"\n\nAgent: {agent.model_dump_json(indent=2)}"
    agent = await model.with_structured_output(Agent).ainvoke(prompt)
    return agent


async def _generate_agent(user_input, messages):
    prompt = NEW_AGENT_PROMPT
    prompt += f"\n\nUser Input: {user_input}"
    prompt += f"\n\nMessages: {messages}"
    agent = await model.with_structured_output(Agent).ainvoke(prompt)
    return agent


def _extract_tools_from_history(messages):
    return [messages["name"] for message in messages if message["type"] == "tool"]


def _tool_config_to_list(tool_config: ToolConfig):
    return []


async def _generate_tools(user_input, messages, tool_config: ToolConfig | None = None):
    used_tools = _extract_tools_from_history(messages)
    tool_config = _merge_tool_configs(tool_config, used_tools)
    if user_input:
        new_tool_config = _generate_tools_from_user_input(user_input, messages, tool_config)
    merged_tool_config = _merge_tool_configs(tool_config, new_tool_config)
    return merged_tool_config
