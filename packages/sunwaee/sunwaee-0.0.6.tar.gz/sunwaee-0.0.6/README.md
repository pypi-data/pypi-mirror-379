# SUNWÆE

The almost-everything package/command-line interface.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![Tests](https://img.shields.io/badge/tests-107%20passed-brightgreen.svg)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](tests/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## OVERVIEW

### Æ-GEN

All LLMs, one response format - available through SDK or self-hosted API (see `sunwaee gen serve` command). Includes usage, cost and performance metrics like reasoning duration and throughput (see [response format](#response)).

> æ-gen doesn't use provider-specific libraries (e.g. openai, anthropic, google...) and parses the raw HTTP responses (including server-sent event streams) directly from the providers using provider-specific adapters.

## INSTALLATION

1. For regular usage:

```bash
pip install sunwaee
```

2. For dev usage (contributors):

```bash
pip install sunwaee[dev]
```

## GEN

All LLMs, one response format - available through SDK or self-hosted API (see `sunwaee gen serve` command). Includes usage, cost and performance metrics like reasoning duration and throughput (see [response format](#response)).

> æ-gen doesn't use provider-specific libraries (e.g. openai, anthropic, google...) and parses the raw HTTP responses (including server-sent event streams) directly from the providers using provider-specific logic called `adapters`.

What æ-gen does under the hood:

1. validates messages according to the openai format (see [MODELS](#models))
2. validates tools according to the openai format (see [MODELS](#models))
3. use provider-specific logic (`adapters`) to build provider-specific payload.
4. use provider-specific logic (`adapters`) to parse provider-specific response.
5. compute additional metrics related to performance, cost, usage... and return a [block](#response)

> Reasoning tokens are not available for certain agents despite supporting reasoning (e.g. `openai/gpt-5`, `google/gemini-2.5-pro`...). When that's the case, a block with `reasoning="reasoning started, but reasoning tokens are not avaiable for this model..."` will be returned, indicating reasoning has started.

### USAGE

1. SDK

```python
import asyncio
import sunwaee.gen as aegen

# list available resources
print(aegen.AGENTS)
print(aegen.MODELS)
print(aegen.PROVIDERS)

messages = [
    {"role": "system": "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the latest news about AI?"}
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    }
]

async def main():

    # NOTE we use `async for` for both the regular and streaming completion
    async for block in aegen.async_completion(
        "openai/gpt-5",
        messages=messages,
        tools=tools,
        streaming=False
    ):
        if block["reasoning"]:
            print(f"🤔 Reasoning: {block['reasoning']}")
        if block["content"]:
            print(f"💬 Content: {block['content']}")
        if block["tool_calls"]:
            print(f"🔧 Tool calls: {len(block['tool_calls'])}")

asyncio.run(main())
```

2. API

```sh
# list
sunwaee gen list models
sunwaee gen list providers
sunwaee gen list agents

# serve
sunwaee gen serve

curl -X 'POST' \
  'http://localhost:8000/gen/completion' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <api_key>' \
  -H 'Content-Type: application/json' \
  -d '{
  "agent": "openai/gpt-5-nano",
  "messages": [{"role": "user", "content": "hi"}],
  "tools": [],
  "streaming": false
}'
```

### MODELS

#### MESSAGES

```python
[
    {
        "role": "system|user|assistant|tool",
        "content": "Here's a response.", # str
        "tool_call_id": "tc_123", # str
        "tool_calls": [
            {
            "id": "tc_123", # str
            "type": "function",
            "function": {
                "name": "get_weather", # str
                "arguments": "{\"city\": \"Paris\"}" # str
                }
            }
        ]
    }
]
```

> **`tool` messages must contain `tool_call_id`.**

#### TOOLS

```python
[
    {
        "type": "function", # str
        "function": {
            "name": "get_weather", # str
            "description": "Get a weather in a given city.", # str
            "parameters": {
                "type": "object", # str
                "properties": {
                    "city": {
                        "type": "string", # str
                        "description": "The city (e.g. Paris, London...)" # str
                    }
                },
                "required": ["city"] # list[str]
            }
        }
    }
]
```

#### RESPONSE

```python
{
  "model": {
    "name": "string",
    "display_name": "string",
    "origin": "string",
    "version": "string"
  },
  "provider": {
    "name": "string",
    "url": "string"
  },
  "error": {
    "status": 0
    "message": "string",
  },
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0
  },
  "cost": {
    "prompt_cost": 0,
    "completion_cost": 0,
    "total_cost": 0
  },
  "performance": {
    "latency": 0,
    "reasoning_duration": 0,
    "content_duration": 0,
    "total_duration": 0,
    "throughput": 0
  },
  "reasoning": "string",
  "content": "string",
  "tool_calls": [],
  "raw": "string",
  "streaming": false
}
```
