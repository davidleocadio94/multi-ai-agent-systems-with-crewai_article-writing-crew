"""Gradio interface for the Article Writing Crew."""

import gradio as gr
from src.crew import run_crew


def generate_article(topic: str, progress=gr.Progress()) -> str:
    """Generate an article on the given topic using the multi-agent crew."""
    if not topic.strip():
        return "Please enter a topic to write about."

    try:
        progress(0, desc="Starting multi-agent crew...")
        progress(0.1, desc="Content Planner: Researching trends and creating outline...")

        # Run the crew (this is where the actual work happens)
        result = run_crew(topic)

        progress(1.0, desc="Article complete!")
        return result
    except Exception as e:
        return f"Error generating article: {str(e)}"


# Create Gradio interface
with gr.Blocks(title="Article Writing Crew", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Article Writing Crew

        A multi-agent system that collaborates to create professional blog articles.

        **How it works:**
        1. **Content Planner** - Researches trends and creates an outline
        2. **Content Writer** - Writes the article based on the plan
        3. **Editor** - Polishes the final piece

        Enter a topic below and watch the agents collaborate!

        *Note: Generation takes 1-3 minutes as multiple AI agents work together.*
        """
    )

    with gr.Row():
        topic_input = gr.Textbox(
            label="Topic",
            placeholder="e.g., Artificial Intelligence, Climate Change, Remote Work",
            scale=4
        )
        submit_btn = gr.Button("Generate Article", variant="primary", scale=1)

    output = gr.Markdown(label="Generated Article")

    # Example topics
    gr.Examples(
        examples=[
            ["Artificial Intelligence in Healthcare"],
            ["The Future of Remote Work"],
            ["Sustainable Technology Trends"],
            ["Cybersecurity Best Practices"],
        ],
        inputs=topic_input,
    )

    submit_btn.click(
        fn=generate_article,
        inputs=topic_input,
        outputs=output,
    )

    topic_input.submit(
        fn=generate_article,
        inputs=topic_input,
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch()
