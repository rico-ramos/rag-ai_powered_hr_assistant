"""
retriever.py

Creates the retriever used to find relevant document chunks
from the persisted FAISS vector store.

Responsibilities:
- Load the FAISS vector store
- Configure top-k retrieval
- Return a LangChain retriever
"""

from langchain_core.vectorstores import VectorStoreRetriever

from app.config.settings import TOP_K
from app.retrieval.vector_store import load_vector_store


def get_retriever() -> VectorStoreRetriever:
    """Load the vector store and return a configured retriever."""

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": TOP_K}
    )

    return retriever