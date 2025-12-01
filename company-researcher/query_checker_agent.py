from google.adk.tools import google_search
from google.adk.tools import agent_tool
from pydantic import BaseModel, Field
from agent_factory import create_agent

class InputValidation(BaseModel):
    reason: str = Field(description="Why the input is invalid, or empty when valid.")
    valid: bool = Field(description="True only if the search finds an exact company match.")

instruction = (
    "Your task is to determine whether the user query refers to an actual company.\n\n"

    "ABSOLUTE RULE:\n"
    "You must NOT assume relevance from context or text similarity.\n"
    "You are only allowed to consider a company VALID if the search results contain\n"
    "a company name whose normalized text CONTAINS the exact normalized root token\n"
    "of the user query.\n\n"

    "Definition of normalized root token:\n"
    "- lowercased\n"
    "- stripped of punctuation\n"
    "- first strong word in the query (e.g. 'bosch' from 'bosch schwäbisch gmünd')\n\n"

    "VALID example:\n"
    "Query: 'Bosch Schwäbisch Gmünd' → root token: 'bosch' → matches 'Robert Bosch GmbH'\n\n"

    "INVALID example:\n"
    "Query: 'eurosmarkt' → root token: 'eurosmarkt' → found: 'Euronext', 'Euro-S-Markt' → NO MATCH.\n"
    "Therefore INVALID.\n"
    "Do NOT infer, guess, or assume the user meant something else.\n\n"

    "Uncertainty rule:\n"
    "If there is ANY doubt about whether the found company name matches the user's root token,\n"
    "mark the query INVALID and ask the user to clarify.\n\n"

    "When INVALID:\n"
    "- List possible close matches from search results (ONLY if they share some characters).\n"
    "- Ask user: 'Did you mean one of these?'\n"
    "- Provide one example of a valid query.\n"
)

search_agent = create_agent(
    name="CompanyNameSearchAgent",
    instruction=(
        "You perform ONLY Google searches. "
        "Given a raw query string, always run google_search with that exact query. "
        "Return ONLY the raw search results. No reasoning, no interpretation."
    ),
    tools=[google_search],
)



query_checker_agent = create_agent(
    name="QueryCheckerAgent",
    instruction=instruction,
    tools=[agent_tool.AgentTool(agent=search_agent)],
    output_schema=InputValidation
)
