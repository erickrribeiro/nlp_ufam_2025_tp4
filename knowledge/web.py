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

nextjs_knowledge_source = web_knowledge_source(
    file_paths=[
        "https://nextjs.org/docs/getting-started",
        "https://nextjs.org/docs/app/building-your-application/routing",
        "https://nextjs.org/docs/app/building-your-application/data-fetching",
    ]
)

word_embeddings_knowledge_source = web_knowledge_source(
    file_paths=[
        "https://medium.com/turing-talks/word-embedding-fazendo-o-computador-entender-o-significado-das-palavras-92fe22745057",
        "https://medium.com/@harsh.vardhan7695/a-comprehensive-guide-to-word-embeddings-in-nlp-ee3f9e4663ed",
        "https://www.geeksforgeeks.org/nlp/word-embeddings-in-nlp/"
    ]
)