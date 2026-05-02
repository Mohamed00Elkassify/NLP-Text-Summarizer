import streamlit as st
from backend import summarize_text

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("Text Summarizer")
st.caption("Paste your text and get a concise summary.")
st.divider()

user_text = st.text_area("Your Text", placeholder="Paste your text here... (minimum 30 words)", height=250)
if st.button("Summarize", type="primary", use_container_width=True):
    if not user_text.strip():
        st.error("Please enter some text first.")
    else:
        with st.spinner("Generating summary..."):
            result = summarize_text(user_text)

        if result.startswith("Error"):
            st.error(result)
        else:
            st.subheader("Summary")
            st.success(result)