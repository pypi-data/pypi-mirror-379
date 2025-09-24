# standard
# third party
# custom
from sunwaee.gen._api._router import aegen_router
from sunwaee.gen import Provider
from sunwaee.gen import PROVIDERS


@aegen_router.get("/providers", response_model=list[Provider])
async def list_available_providers():
    """List available providers (e.g. 'anthropic', 'openai'...)"""
    return [p for p in PROVIDERS.values()]
