# standard
# third party
# custom
from sunwaee.logger import logger
from sunwaee.gen.providers.anthropic import *
from sunwaee.gen.providers.deepseek import *
from sunwaee.gen.providers.google import *
from sunwaee.gen.providers.openai import *
from sunwaee.gen.providers.xai import *

PROVIDERS = {
    p.name: p
    for p in [
        ANTHROPIC,
        DEEPSEEK,
        GOOGLE,
        OPENAI,
        XAI,
    ]
}

logger.info(f"AVAILABLE PROVIDERS: {PROVIDERS.keys()}")
