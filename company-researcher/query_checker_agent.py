from pydantic import BaseModel, Field
from agent_factory import create_agent

class InputValidation(BaseModel):
    reason: str = Field(description="Explains why the input is invalid, or remains empty when the input is valid.")
    valid: bool = Field(description="Indicates whether the input consists solely of a single company name.")

instruction = ("You are the main input hanndling agent of a company research tool. Your ONLY task is to check whether the input"
               "is only about company research about a single company. No comparisons or anything related to something else than the company."
               "If the search is invalid, return a reason for the user why this is the case with a helpful explanation  what this"
               "tool is about and an example query that could work.")

query_checker_agent = create_agent(
    name="QueryCheckerAgent",
    instruction=instruction,
    output_schema=InputValidation
    )
