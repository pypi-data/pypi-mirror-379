import os

import dspy

openai_lm = dspy.LM(
    model="openai/gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"], max_tokens=4000
)

local_lm = dspy.LM(model="ollama/llama3.1:8b", api_key="", max_tokens=4000)
