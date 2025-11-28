# agent_factory.py
import os
from google.adk.agents import Agent

GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")
if not GEMINI_MODEL_NAME:
    raise ValueError("GEMINI_MODEL_NAME must be set.")

def create_agent(name, instruction, output_schema = None, tools = None) -> Agent:
    if not GEMINI_MODEL_NAME:
        raise ValueError("GEMINI_MODEL_NAME must be set.") 
    return Agent(name=name, model=GEMINI_MODEL_NAME, instruction=instruction, output_schema=output_schema, tools=tools or [])