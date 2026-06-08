from app.ingestion.loader import load_pdf_documents
from app.ingestion.chunking import chunk_documents


def test_chunk_documents():
    documents = load_pdf_documents("data")

    chunks = chunk_documents(documents)

    assert len(chunks) > 0

    first_chunk = chunks[0]

    assert first_chunk.page_content

    assert "source" in first_chunk.metadata
    assert "page" in first_chunk.metadata