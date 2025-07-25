from typing import Optional
from crewai import Crew, Process
from crewai.knowledge.source.base_knowledge_source import BaseKnowledgeSource
from crewai.llms.base_llm import BaseLLM
from crewai.project import CrewBase, crew

from src.nlp_ufam.config import agents as A
from src.nlp_ufam.config import tasks as T

@CrewBase
class Nlp012025():
    """Nlp012025 crew"""
    llm: BaseLLM
    web_knowledge_sources: BaseKnowledgeSource
    pdf_knowledge_sources: Optional[BaseKnowledgeSource] = None
    
    @crew
    def crew(self) -> Crew:
        # Agent planner
        content_planner =  A.build_planning_agent(self.llm)
        if self.web_knowledge_sources:
            content_planner.knowledge_sources.append(self.web_knowledge_sources)
        if self.pdf_knowledge_sources:
            content_planner.knowledge_sources.append(self.pdf_knowledge_sources)

        # Agent writer
        content_writer = A.build_writing_agent(self.llm)
        if self.web_knowledge_sources:
            content_writer.knowledge_sources.append(self.web_knowledge_sources)
        if self.pdf_knowledge_sources:
            content_writer.knowledge_sources.append(self.pdf_knowledge_sources)

        # Agent editor
        content_editor = A.build_editing_agent(self.llm, knowledge_sources=[])
        
        # Tasks
        plan_task = T.build_planning_task(content_planner)
        write_task = T.build_writing_task(content_writer)
        edit_task = T.build_editing_task(content_editor)
        return Crew(
            agents=[content_planner, content_writer, content_editor],
            tasks=[plan_task, write_task, edit_task],
            process=Process.sequential,
            verbose=True,
        )
