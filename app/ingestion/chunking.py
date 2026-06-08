"""
chunking.py

Splits loaded documents into smaller chunks for semantic retrieval.

Responsibilities:
- Split document pages into retrievable chunks
- Preserve source and page metadata
- Use centralized chunking settings
"""

from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_documents(documents: List[Document]) -> List[Document]:
    """Split documents into smaller chunks while preserving metadata."""

    if not documents:
        raise ValueError("No documents provided for chunking.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks from {len(documents)} document page(s).")

    return chunks