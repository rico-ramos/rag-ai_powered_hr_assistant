from app.ingestion.loader import load_pdf_documents
from app.ingestion.chunking import chunk_documents

documents = load_pdf_documents("data")
chunks = chunk_documents(documents)

print(chunks[0].metadata)
print(chunks[0].page_content[:500])