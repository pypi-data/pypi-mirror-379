# standard
# third party
# custom
from sunwaee.logger import logger
from sunwaee.gen.models.anthropic import *
from sunwaee.gen.models.deepseek import *
from sunwaee.gen.models.google import *
from sunwaee.gen.models.openai import *
from sunwaee.gen.models.xai import *

MODELS = {
    m.name: m
    for m in ANTHROPIC_MODELS
    + DEEPSEEK_MODELS
    + GOOGLE_MODELS
    + OPENAI_MODELS
    + XAI_MODELS
}

logger.info(f"AVAILABLE MODELS: {MODELS.keys()}")
