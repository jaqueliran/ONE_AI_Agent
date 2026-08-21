import streamlit as st


st.set_page_config(
    page_title="Common Ground AI Assistant",
    page_icon="📚",
    layout="centered"
)


st.title("Common Ground AI Assistant")

st.write(
    "Ask questions about Common Ground policies, "
    "academic procedures, and teacher benefits."
)


question = st.text_input(
    "Your question:",
    placeholder="What is the minimum attendance requirement?"
)


if st.button("Ask"):
    if question.strip():
        st.info(
            "The RAG system will answer this question "
            "once the vector database is available."
        )
    else:
        st.warning("Please enter a question.")