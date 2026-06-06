"""
vector_store.py

Creates and loads the FAISS vector store used
for semantic document retrieval.

Responsibilities:
- Create vector embeddings
- Build FAISS index
- Persist index to disk
- Load existing index
"""


from app.retrieval.embeddings import get_embedding_model
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from typing import List
import os

VECTOR_STORE_PATH = "vector_store"

def create_vector_store(chunks: List[Document]) -> FAISS:
    """Create a FAISS vector store from document chunks."""

    if not chunks:
        raise ValueError("No document chunks provided for vector store creation.")

    print("Creating FAISS vector store from document chunks...")
    
    embedding_model = get_embedding_model()

    vector_store = FAISS.from_documents(chunks, embedding_model)

    if not os.path.exists("vector_store"):
        os.makedirs("vector_store")
     
    os.makedirs("vector_store", exist_ok=True)

    vector_store.save_local(VECTOR_STORE_PATH)
    
    print(
        f"Created and saved FAISS vector store "
        f"with {len(chunks)} chunks."
    )
    
    return vector_store

def load_vector_store() -> FAISS:
    """Load the FAISS vector store from disk."""

    if not os.path.exists(VECTOR_STORE_PATH):
        raise FileNotFoundError("FAISS index not found. Please run the ingestion process first.")
    
    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    print("Loaded FAISS vector store from disk.")
    
    return vector_store