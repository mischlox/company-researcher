# questions_agent.py
from pydantic import BaseModel, Field
from agent_factory import create_agent

class InterviewQuestions(BaseModel):
    markdown_questions: str = Field(
        description="A markdown-formatted list of high-impact interview questions with brief reasoning."
    )

num_questions = 5
instruction = (
    "You generate high-impact interview questions based on raw research summaries about a company. "
    f"Produce exactly {num_questions} questions.\n"
    "You will be given several short summaries, each from a separate web search.\n"
    "Create sharp, specific questions that show deep preparation and insight that one could ask in an interview. Avoid generic questions."
    "Each question should make it clear that the candidate studied the company in detail. Give each question a caption.\n"
    "Output strictly in markdown format. Use a numbered list. For each question, include a short "
    "italicized explanation underneath it prefixed with 'Reasoning:'."
)

questions_agent = create_agent(
    name="QuestionsAgent",
    instruction=instruction,
    output_schema=InterviewQuestions
    )