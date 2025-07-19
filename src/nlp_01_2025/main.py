#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from nlp_01_2025.crew import Nlp012025

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Introdução a RAG com exemplos',
        'current_year': str(datetime.now().year),
        'knowledge_sources': [
            "https://neptune.ai/blog/tokenization-in-nlp",
        ]
    }
    
    try:
        Nlp012025().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
