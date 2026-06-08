from app.retrieval.retriever import get_retriever


def test_retriever_returns_documents():
    retriever = get_retriever()

    docs = retriever.invoke(
        "What does the policy say about training and development?"
    )

    assert len(docs) > 0

    first_doc = docs[0]

    assert first_doc.page_content

    assert "source" in first_doc.metadata
    assert "page" in first_doc.metadata