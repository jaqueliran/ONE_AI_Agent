import streamlit as st

from rag import generate_response


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
        with st.spinner("Searching the documents..."):
            response, sources = generate_response(question)

        st.subheader("Answer")
        st.write(response)

        if sources:
            st.subheader("Sources")

            for source in sources:
                st.write(f"- {source}")

    else:
        st.warning("Please enter a question.")