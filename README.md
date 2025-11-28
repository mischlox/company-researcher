# Company Research Agent

The `company-researcher` project is a tool designed to assist in preparing for job interviews by conducting deep research on companies. It automates the process of generating search queries, performing web searches, and compiling detailed reports and interview questions based on the findings. 

The project leverages the Google ADK (Agent Development Kit).

## TODO

- [ ] Improve UI
- [ ] Add guardrails, so only searches for companies are allowed
- [ ] Make the LLM ask further questions if anything is still unclear
- [ ] Deploy demo to huggingface

## Features

- **Search Planning**: Generates search queries to uncover insights about a company's strategy, culture, products, and more.
- **Automated Web Searches**: Executes searches and summarizes the most relevant findings.
- **Report Generation**: Creates a detailed markdown report with insights tailored for job interviews.
- **Interview Questions**: Produces interview questions based on the research.
- **Interactive UI**: Includes a Gradio-based interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mischlox/company-researcher.git
   cd company-researcher
   ```

2. Set up the Python environment using `uv`:
   ```bash
   uv create
   uv install
   ```

3. Configure environment variables:
   Create a `.env` file in the root directory with the following content:
   ```properties
   GOOGLE_API_KEY=your_google_api_key
   GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
   GEMINI_MODEL_NAME=gemini-2.5-flash
   ```

## Usage

1. Launch the application:
   ```bash
   python company-researcher/main.py
   ```

2. Open the Gradio interface in your browser and enter a topic to research.

## Project Structure

- `company_researcher.py`: Main logic for orchestrating the research process.
- `planner_agent.py`: Generates search queries.
- `search_agent.py`: Performs web searches and summarizes findings.
- `report_agent.py`: Creates detailed reports.
- `questions_agent.py`: Generates interview questions.
- `main.py`: Entry point with Gradio UI.

## Notes

This is my first project using Google ADK, and I created it as a practice exercise to explore its capabilities. The project is not intended for production use but serves as a learning experience.

## Dependencies

- Python 3.12+
- Google ADK
- Gradio
- MLflow
- Pydantic
