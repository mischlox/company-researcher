# planner_agent.py
from pydantic import BaseModel, Field
from agent_factory import create_agent

class SearchItem(BaseModel):
    reason: str = Field(description="The reason why this search is important to the query.")
    query: str = Field(description="The actual search that is used for the research.")

class SearchPlan(BaseModel):
    searches: list[SearchItem] = Field(description="List of web searches to perform to do the best research about the company that is possible.")
    
    
num_searches = 3
instruction = (
    "You are a helpful research assistand and you help prepare for job interviews by generating search queries about a company."
    "Create search terms that reveal the company's strategy, culture, products, recent news, technical initiatives, and competitive landscape."
    "Focus on terms that surface information useful for forming thoughtful interview questions."
    f"Output exactly {num_searches} high-value search queries."
)


planner_agent = create_agent(
    name="PlannerAgent",
    instruction=instruction,
    output_schema=SearchPlan
    )