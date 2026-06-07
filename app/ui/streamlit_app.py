"""
streamlit_app.py

User interface for the HR Policy RAG Assistant.

Responsibilities:
- Accept user questions
- Display answers
- Display source citations
"""

import streamlit as st

from app.chains.rag_chain import answer_question


st.set_page_config(
    page_title="HR Policy RAG Assistant",
    layout="wide"
)

st.title("HR Policy RAG Assistant")

question = st.text_input(
    "Ask a question about your HR policy documents:"
)

if st.button("Ask Question"):

    if question.strip():

        with st.spinner("Searching documents..."):

            result = answer_question(question)

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Sources")

        for source in result["sources"]:
            st.write(
                f"- {source['source']} "
                f"(Page {source['page']})"
            )
        
        st.subheader("Metrics")

        st.write(
            f"Retrieved Chunks: "
            f"{result['retrieved_chunks']}"
        )

        st.write(
            f"Response Time: "
            f"{result['response_time']} seconds"
        )

        st.write(
            f"Prompt Tokens: "
            f"{result['prompt_tokens']}"
        )

        st.write(
            f"Completion Tokens: "
            f"{result['completion_tokens']}"
        )

        st.write(
            f"Total Tokens: "
            f"{result['total_tokens']}"
        )