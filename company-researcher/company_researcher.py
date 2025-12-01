# company_researcher.py
import asyncio
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types
from query_checker_agent import query_checker_agent, InputValidation
from planner_agent import planner_agent, SearchPlan
from search_agent import search_agent
from report_agent import report_agent, ReportData
from questions_agent import questions_agent
import uuid



class CompanyResearcher:
    
    def __init__(self, app_name="CompanyResearchAgent", user_id="research_tool_user"):
        self.app_name = app_name
        self.user_id = user_id
        self.session_service = InMemorySessionService()
        # Turn on auto tracing for Gemini


    async def run_query(self, agent, input, session_id=None):
        session_id = session_id or str(uuid.uuid4())
        session = await self.session_service.create_session(app_name=self.app_name, user_id=self.user_id, session_id=session_id)
        runner = Runner(agent=agent, app_name=self.app_name, session_service=self.session_service)
        content = types.Content(role='user', parts=[types.Part(text=input)])
        events = runner.run_async(user_id=self.user_id, session_id=session_id, new_message=content)
        async for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text
                # print("Agent Response: ", final_response)
        if agent.output_schema:
            return agent.output_schema.model_validate_json(final_response)

        return final_response
    
    async def run(self, query: str):
        try:
            print("Starting research ...")
            input_validation = await self.check_query(query)
            if not input_validation.valid:
                yield input_validation.reason
                return
            
            search_plan = await self.plan_searches(query)
            yield "Searches planned, starting to search ..."
            search_results = await self.perform_searches(search_plan)
            yield "Searches completed, writing report ..."
            report = await self.write_report(query, search_results)
            print(report)
            yield report
        except Exception as e:
            print(f"Error during run(): {e}")
            yield "An error occurred while processing your query. Please try again."

    async def check_query(self, query: str) -> InputValidation:
        return await self.run_query(query_checker_agent, query)
    
    async def plan_searches(self, query: str) -> SearchPlan:
        return await self.run_query(planner_agent, query)

    
    async def perform_searches(self, search_plan: SearchPlan) -> list[str]:
        tasks = []
        for search in search_plan.searches:
            input = f"Query: {search.query} Reason for search: {search.reason}"
            tasks.append(asyncio.create_task(self.run_query(search_agent, input)))
        results = await asyncio.gather(*tasks)
        return results
        
    
    async def write_report(self, original_query, search_results: list[str]) -> ReportData:
        input = f"Original query: {original_query} search results: {search_results}"
        report_task = asyncio.create_task(
            self.run_query(report_agent, input)
        )
        questions_task = asyncio.create_task(
            self.run_query(questions_agent, input)
        )
        report_result, questions_result = await asyncio.gather(
            report_task,
            questions_task
        )
        
        combined_markdown = (
            report_result.markdown_report
            + "\n\n---\n\n"
            + "## Interview Questions\n\n"
            + questions_result.markdown_questions           
        )
        return combined_markdown

        
    async def create_pdf(self, report: ReportData) -> None:
        pass