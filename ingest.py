from app.ingestion.loader import load_pdf_documents
from app.ingestion.chunking import chunk_documents
from app.retrieval.vector_store import create_vector_store

documents = load_pdf_documents("data")
chunks = chunk_documents(documents)

vector_store = create_vector_store(chunks)

print(chunks[0].metadata)
print(chunks[0].page_content[:500])
