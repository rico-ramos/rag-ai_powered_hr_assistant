from app.chains.rag_chain import answer_question

result = answer_question(
    "What does the policy say about employee training and development?"
)

print(result["answer"])
print("\nSources:")
for source in result["sources"]:
    print(f"- {source['source']} (Page {source['page']})")

print(f"\nRetrieved Chunks: {result['retrieved_chunks']}")