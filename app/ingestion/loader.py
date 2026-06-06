"""
loader.py

Loads PDF documents from the data directory.

Responsibilities:
- Discover PDF files
- Load PDF content
- Attach source metadata
- Return LangChain Documents
"""

import os
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf_documents(data_directory: str) -> List[Document]:
    """Load PDF documents from the specified directory."""

    if not os.path.exists(data_directory):
        raise FileNotFoundError(f"Data directory not found: {data_directory}")

    documents: List[Document] = []

    pdf_files = [
        fname for fname in os.listdir(data_directory)
        if fname.lower().endswith(".pdf")
    ]

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in: {data_directory}")

    for fname in pdf_files:
        pdf_path = os.path.join(data_directory, fname)

        loader = PyPDFLoader(pdf_path)
        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = fname

        documents.extend(docs)

    print(f"Loaded {len(documents)} pages from {len(pdf_files)} PDF file(s).")

    return documents