from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from src.nlp_01_2025.config.agents import planner, writer, editor
from src.nlp_01_2025.config.tasks import plan, write, edit

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
    
    @task
    def plan_task(self) -> Task:
        return plan

    @task
    def write_task(self) -> Task:
        return write

    @task
    def edit_task(self) -> Task:
        return edit
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
