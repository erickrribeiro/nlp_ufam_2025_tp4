from crewai import Task
from src.nlp_01_2025.config.agents import planner, editor


research = Task(
    description=(
        "Conduct a thorough research about {topic}. "
        "Make sure you find any interesting and relevant information given the current year is {current_year}."
    ),
    expected_output=(
        "A list with 10 bullet points of the most relevant information about {topic}."
    ),
    agent=planner,
    verbose=True
)

reporting = Task(
    description=(
        "Review the context you got and expand each topic into a full section for a report. "
        "Make sure the report is detailed and contains any and all relevant information."
    ),
    expected_output=(
        "A fully fledged report with the main topics, each with a full section of information. "
        "Formatted as markdown without '```'."
    ),
    agent=editor,
    markdown=True,
    output_file='report.md',
    verbose=True,
)