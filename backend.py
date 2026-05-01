from transformers import pipeline

print("Loading the Facebook BART model... This will take a moment on the first run.")

# Load the model once when this file is imported by the frontend
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("Model loaded successfully and is ready to use!")
except Exception as e:
    print(f"Failed to load the model. Error: {e}")

def summarize_text(text):
    """
    Takes a long string of text and returns a summary.
    """
    # 1. Validate the input
    if not text or len(text.strip()) == 0:
        return "Error: No text provided."
        
    word_count = len(text.split())
    if word_count < 30:
        return f"Error: Text is too short ({word_count} words). Please provide at least 30 words."

    # 2. Generate the summary
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


# ==========================================
# TESTING BLOCK
# ==========================================
# This allows you to test your backend independently of your teammate's frontend.
if __name__ == "__main__":
    
    print("\n--- Terminal Testing Mode ---")
    # Request text input from the user in the terminal
    user_test_text = input("Paste the text you want to summarize and press Enter: ")
    
    if user_test_text.strip():
        print("\nProcessing... please wait.")
        summary = summarize_text(user_test_text)
        print(f"\nRESULT:\n{summary}")
    else:
        print("Error: You didn't enter any text!")