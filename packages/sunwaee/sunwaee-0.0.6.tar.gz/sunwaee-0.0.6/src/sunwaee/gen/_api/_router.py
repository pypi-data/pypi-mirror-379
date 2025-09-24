# standard
# third party
import fastapi

# custom

aegen_router = fastapi.APIRouter(prefix="/gen", tags=["gen"])

from . import completion
from . import agents
from . import models
from . import providers
