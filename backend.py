import streamlit as st
from transformers import pipeline

@st.cache_resource
def get_summarizer():
    print("Loading the Facebook BART model... This will take a moment on the first run.")
    try:
        model = pipeline("summarization", model="facebook/bart-large-cnn")
        print("Model loaded successfully and is ready to use!")
        return model
    except Exception as e:
        print(f"Failed to load the model. Error: {e}")
        return None

def summarize_text(text):
    # 1. Validate the input
    if not text or len(text.strip()) == 0:
        return "Error: No text provided."
        
    word_count = len(text.split())
    if word_count < 30:
        return f"Error: Text is too short ({word_count} words). Please provide at least 30 words."

    summarizer = get_summarizer()
    if summarizer is None:
        return "Error: Could not load the summarization model."

    # 3. Generate the summary
    try:
        # Generate summary using greedy decoding (do_sample=False) for factual accuracy
        result = summarizer(
            text, 
            max_length=150, 
            min_length=40, 
            do_sample=False
        )
        # 3. Return the exact summary string
        return result[0]['summary_text']
        
    except Exception as e:
        return f"An error occurred during summarization: {str(e)}"

# TESTING BLOCK
if __name__ == "__main__":
    print("\n--- Terminal Testing Mode ---")
    user_test_text = input("Paste the text you want to summarize and press Enter: ")
    if user_test_text.strip():
        print("\nProcessing... please wait.")
        summary = summarize_text(user_test_text)
        print(f"\nRESULT:\n{summary}")
    else:
        print("Error: You didn't enter any text!")