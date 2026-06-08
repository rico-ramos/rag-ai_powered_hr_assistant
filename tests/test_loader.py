from app.ingestion.loader import load_pdf_documents


def test_load_pdf_documents():
    documents = load_pdf_documents("data")

    assert len(documents) > 0

    first_doc = documents[0]

    assert "source" in first_doc.metadata
    assert "page" in first_doc.metadata
    assert first_doc.page_content