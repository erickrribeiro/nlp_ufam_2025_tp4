#!/usr/bin/env python
import os
import warnings
from datetime import datetime

from crewai import LLM

from src.nlp_ufam.crew import Nlp012025
# from src.nlp_ufam.knowledges import (
#     raq_knowledge_source_template,
#     nextjs_knowledge_source_template,
#     word_embeddings_knowledge_source_template
# )   
from src.nlp_ufam.knowledges import init_pdf_knowledge_source, init_web_knowledge_source

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """

    inputs = {
        # 'topic': 'Impacto de Ferramentas de IA no desenvolvimento de Software',
        # 'topic': 'Explicando o que é Análise de Sentimentos Baseada em Aspectos e onde aplicar',
        'topic': 'O que é Similaridade Vetorial e por que ela importa no Machine Learning?',
        'current_year': str(datetime.now().year),
    }
    
    try:
        project = Nlp012025()
        project.llm = LLM(model=os.getenv("MODEL"))

        project.web_knowledge_sources = init_web_knowledge_source(
            file_paths=[
                "https://huggingface.co/blog/setfit-absa",
                "https://medium.com/nlplanet/quick-intro-to-aspect-based-sentiment-analysis-c8888a09eda7"
            ]
        )
        project.pdf_knowledge_sources = init_pdf_knowledge_source(file_paths=["./triplet-absa.pdf"])
        
        project.crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()