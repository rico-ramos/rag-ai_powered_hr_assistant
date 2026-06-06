"""
embeddings.py

Creates the embedding model used to convert document chunks
into vector representations.

Responsibilities:
- Load environment variables
- Initialize OpenAI embeddings
- Use centralized model configuration
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import os

from app.config.settings import EMBEDDING_MODEL


def get_embedding_model() -> OpenAIEmbeddings:
    """Return the configured OpenAI embedding model."""

    load_dotenv()

    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )