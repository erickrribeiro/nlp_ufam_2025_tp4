from typing import List
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource

def web_knowledge_source(file_paths: List[str]) -> CrewDoclingSource:
    return CrewDoclingSource(file_paths=file_paths)
    
faq_knowledge_source = web_knowledge_source(
    file_paths=[
        "https://medium.com/@lucascarrasquillaparra/chat-with-your-documents-tool-rag-vector-dbs-cosine-sim-claude-api-implementation-2312cf14c67a",
        "https://python.langchain.com/docs/tutorials/rag/",
        "https://medium.com/@nyshnt/a-practical-guide-to-building-a-retrieval-augmented-generation-rag-application-for-uploading-and-e72caae3ff90"
    ]
)