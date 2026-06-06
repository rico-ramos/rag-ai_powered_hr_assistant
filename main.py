from app.retrieval.retriever import get_retriever

retriever = get_retriever()

docs = retriever.invoke("What does the policy say about training and learning?")

print(f"Retrieved {len(docs)} chunks")

for doc in docs:
    print(doc.metadata)
    print(doc.page_content[:300])
    print("-" * 80)