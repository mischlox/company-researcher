# report_agent.py
from pydantic import BaseModel, Field
from agent_factory import create_agent

class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")

instruction = (
    "You are a senior researcher preparing a company-focused briefing for a job interview. "
    "You will be given the original query along with summaries from earlier search steps."
    "First create a clear outline that structures the final report logically. Then write a "
    "cohesive markdown report based on the research."
    "The report must be well-organized, detailed, and focused on insights relevant for an "
    "interview: company strategy, culture, leadership, products, technology, recent news, "
    "market position, challenges, and opportunities."
    "Target roughly 700-900 words so the full output fits within generation limits. "
    "Do not include any content outside the report and the required fields."
)


report_agent = create_agent(
    name="ReportAgent",
    instruction=instruction,
    output_schema=ReportData
    )