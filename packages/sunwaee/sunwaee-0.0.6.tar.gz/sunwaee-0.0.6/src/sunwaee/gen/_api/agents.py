# standard
# third party
# custom
from sunwaee.gen._api._router import aegen_router
from sunwaee.gen import Agent
from sunwaee.gen import AGENTS


@aegen_router.get("/agents", response_model=list[Agent])
async def list_available_agents():
    """List available agents with naming format `provider/model` (e.g. 'anthropic/claude-4-sonnet', 'openai/gpt-5'...)"""
    return [a for a in AGENTS.values()]
