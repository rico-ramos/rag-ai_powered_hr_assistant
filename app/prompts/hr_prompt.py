"""
hr_prompt.py

Defines the prompt used by the HR Policy RAG Assistant.

Responsibilities:
- Provide system instructions
- Keep responses grounded in retrieved context
- Require source-aware answers
"""

from langchain_core.prompts import ChatPromptTemplate


HR_PROMPT = ChatPromptTemplate.from_template(
    """
You are an HR policy assistant.

Answer the user's question using only the provided context.

If the answer cannot be found in the context, say:
"I could not find that information in the provided HR policy documents."

Provide a clear, concise answer.

Context:
{context}

Question:
{question}

Answer:
"""
)