# standard
# third party
# custom
from sunwaee.logger import logger
from sunwaee.gen.agents.anthropic import *
from sunwaee.gen.agents.deepseek import *
from sunwaee.gen.agents.google import *
from sunwaee.gen.agents.openai import *
from sunwaee.gen.agents.xai import *

AGENTS = {
    a.name: a
    for a in ANTHROPIC_AGENTS
    + DEEPSEEK_AGENTS
    + GOOGLE_AGENTS
    + OPENAI_AGENTS
    + XAI_AGENTS
}

logger.info(f"AVAILABLE AGENTS: {AGENTS.keys()}")
