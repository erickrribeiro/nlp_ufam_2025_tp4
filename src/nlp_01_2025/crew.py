from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from src.nlp_01_2025.config.agents import planner, writer, editor
from src.nlp_01_2025.config.tasks import research, reporting
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Nlp012025():
    """Nlp012025 crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def content_planner(self) -> Agent:
        return planner

    @agent
    def content_writer(self) -> Agent:
        return writer

    @agent
    def content_editor(self) -> Agent:
        return editor
    
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return research

    @task
    def reporting_task(self) -> Task:
        return reporting

    @crew
    def crew(self) -> Crew:
        """Creates the Nlp012025 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
