# search_agent.py
from google.adk.tools import google_search

from agent_factory import create_agent

instruction = (
    "You assist in preparing for job interviews. For the given search term, research it "
    "and produce a concise summary of the most relevant findings about the company. "
    "Summaries should be 2-3 short paragraphs and under 300 words. Capture only essential "
    "facts, themes, and notable insights. Prioritize information useful for creating "
    "informed interview questions. Be succinct; fragments are fine. Do not add commentary "
    "or analysis beyond the extracted findings."
)


search_agent = create_agent(
    name="SearchAgent",
    instruction=instruction,
    tools=[google_search]
)