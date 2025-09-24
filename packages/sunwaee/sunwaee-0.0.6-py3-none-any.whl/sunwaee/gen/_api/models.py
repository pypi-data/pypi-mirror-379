# standard
# third party
# custom
from sunwaee.gen._api._router import aegen_router
from sunwaee.gen import Model
from sunwaee.gen import MODELS


@aegen_router.get("/models", response_model=list[Model])
async def list_available_models():
    """List available models (e.g. 'claude-4-sonnet', 'gpt-5'...)"""
    return [m for m in MODELS.values()]
