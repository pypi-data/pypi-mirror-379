# standard
# third party
# custom
from sunwaee.gen import agents
from sunwaee.gen import models
from sunwaee.gen import providers

from sunwaee.gen.agents._registry import AGENTS
from sunwaee.gen.models._registry import MODELS
from sunwaee.gen.providers._registry import PROVIDERS

from sunwaee.gen.agent import Agent
from sunwaee.gen.message import Message
from sunwaee.gen.model import Model
from sunwaee.gen.provider import Provider
from sunwaee.gen.tool import Tool


async def async_completion(
    agent: str | Agent,
    messages: list[dict],
    tools: list[dict] | None = None,
    streaming: bool = False,
    api_key: str | None = None,
):
    if isinstance(agent, str):
        if agent not in AGENTS:
            available_agents = list(AGENTS.keys())
            raise ValueError(
                f"Agent '{agent}' not found. Available agents: {available_agents}"
            )
        agent_obj = AGENTS[agent]
    else:
        agent_obj = agent

    # NOTE validate messages, including roles,
    # tool calls and tool results
    _ = Message.from_list(messages)

    # NOTE validate tools
    _ = Tool.from_list(tools) if tools else None

    async for block in agent_obj.async_completion(
        messages=messages,
        tools=tools,
        streaming=streaming,
        api_key=api_key,
    ):
        yield block


__all__ = [
    "AGENTS",
    "MODELS",
    "PROVIDERS",
    "Agent",
    "Model",
    "Provider",
    "agents",
    "models",
    "providers",
    "async_completion",
]
