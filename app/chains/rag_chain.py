"""
rag_chain.py

Builds and runs the RAG pipeline for answering HR policy questions.

Responsibilities:
- Retrieve relevant document chunks
- Format retrieved context for the prompt
- Call the language model
- Return answer and source metadata
"""

import os
from typing import Dict, List, Any

from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.config.settings import LLM_MODEL
from app.prompts.hr_prompt import HR_PROMPT
from app.retrieval.retriever import get_retriever


def format_documents(documents: List[Document]) -> str:
    """Format retrieved documents into a context string for the prompt."""

    formatted_docs = []

    for doc in documents:
        source = doc.metadata.get("source", "Unknown source")
        page = doc.metadata.get("page", "Unknown page")

        formatted_docs.append(
            f"Source: {source}, Page: {page + 1 if isinstance(page, int) else page}\n"
            f"{doc.page_content}"
        )

    return "\n\n---\n\n".join(formatted_docs)


def get_sources(documents: List[Document]) -> List[Dict[str, Any]]:
    """Extract source metadata from retrieved documents."""

    seen = set()
    sources = []

    for doc in documents:
        source = doc.metadata.get("source", "Unknown source")
        page = doc.metadata.get("page", "Unknown page")

        if isinstance(page, int):
            page += 1

        key = (source, page)

        if key not in seen:
            seen.add(key)

            sources.append(
                {
                    "source": source,
                    "page": page
                }
            )

    return sources


def answer_question(question: str) -> Dict[str, Any]:
    """Answer a user question using the RAG pipeline."""

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    retriever = get_retriever()
    retrieved_docs = retriever.invoke(question)

    context = format_documents(retrieved_docs)

    llm = ChatOpenAI(
        model=LLM_MODEL,
        temperature=0,
    )


    chain = HR_PROMPT | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return {
        "answer": response.content,
        "sources": get_sources(retrieved_docs),
        "retrieved_chunks": len(retrieved_docs),
    }