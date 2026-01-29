"""CrewAI Article Writing Crew - Multi-Agent Content Creation System"""

from crewai import Agent, Task, Crew
import os


def create_agents():
    """Create the content creation agents."""

    planner = Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory=(
            "You're working on planning a blog article about {topic}. "
            "You focus on researching the latest trends, identifying key players, "
            "and collecting information that helps the audience learn and make "
            "informed decisions."
        ),
        allow_delegation=False,
        verbose=True
    )

    writer = Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate opinion piece about {topic}",
        backstory=(
            "You're working on writing an opinion piece about {topic}. "
            "You work with the Content Planner's outline and provide objective "
            "insights backed by thorough research."
        ),
        allow_delegation=False,
        verbose=True
    )

    editor = Agent(
        role="Editor",
        goal="Edit blog post to align with organization's writing style",
        backstory=(
            "You receive blog posts from the Content Writer and review them "
            "for journalistic best practices, balanced viewpoints, and to "
            "avoid controversial topics."
        ),
        allow_delegation=False,
        verbose=True
    )

    return planner, writer, editor


def create_tasks(planner, writer, editor):
    """Create the content creation tasks."""

    plan_task = Task(
        description=(
            "1. Research the latest trends on {topic} "
            "2. Identify the target audience "
            "3. Develop a comprehensive content outline "
            "4. Include relevant SEO keywords for {topic}"
        ),
        expected_output=(
            "Comprehensive content plan with outline, "
            "audience analysis, SEO keywords, and resources"
        ),
        agent=planner
    )

    write_task = Task(
        description=(
            "1. Use the content plan to craft a compelling blog post on {topic} "
            "2. Incorporate SEO keywords naturally throughout the text "
            "3. Create an engaging structure with intro, body, and conclusion"
        ),
        expected_output=(
            "Well-written blog post in markdown format, "
            "each section with 2-3 paragraphs"
        ),
        agent=writer
    )

    edit_task = Task(
        description="Proofread the blog post for grammar and alignment with brand voice",
        expected_output="Polished blog post ready for publication",
        agent=editor
    )

    return plan_task, write_task, edit_task


def create_crew():
    """Create and return the article writing crew."""
    planner, writer, editor = create_agents()
    plan_task, write_task, edit_task = create_tasks(planner, writer, editor)

    crew = Crew(
        agents=[planner, writer, editor],
        tasks=[plan_task, write_task, edit_task],
        verbose=True
    )

    return crew


def run_crew(topic: str) -> str:
    """Run the crew with the given topic and return the result."""
    os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

    crew = create_crew()
    result = crew.kickoff(inputs={"topic": topic})

    # Handle both string and CrewOutput object results
    if hasattr(result, 'raw'):
        return result.raw
    return str(result)
