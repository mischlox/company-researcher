# main.py
import gradio as gr
from dotenv import load_dotenv
load_dotenv(override=True)

from company_researcher import CompanyResearcher

async def run(query, history):
    """Async generator for streaming research updates."""
    async for update in CompanyResearcher().run(query):
        yield update

def main():

    with gr.Blocks(fill_height=True) as ui:
        gr.ChatInterface(
            run,
            title="Company Research Agent",
            examples=["Google Inc.", "Tell me about Apple", "Bosch Schwäbisch Gmünd"],
            show_progress="full",
            )
    ui.launch(inbrowser=True)


if __name__ == "__main__":
    main()
