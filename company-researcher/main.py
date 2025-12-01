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
    # with gr.Blocks(theme=gr.themes.Glass(primary_hue="sky")) as ui:
    #     gr.Markdown("# Deep Research")
    #     query_textbox = gr.Textbox(label="Enter topic to research", placeholder="Type your query here...", interactive=True)
    #     run_button = gr.Button("Run Research", variant="primary", elem_id="run-button")

    #     report_output = gr.Markdown(label="Report", value="Waiting for query...")

    #     # Link the button and enter key to the async generator
    #     run_button.click(fn=run, inputs=query_textbox, outputs=report_output)
    #     query_textbox.submit(fn=run, inputs=query_textbox, outputs=report_output)
    # ui.launch(inbrowser=True)
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
