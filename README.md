# Text Summarizer Backend

This project provides a text summarization engine powered by Hugging Face's Bidirectional and Auto-Regressive Transformers (BART) model. It specifically utilizes the facebook/bart-large-cnn model, which is fine-tuned for high-quality summarization tasks.

## Features
- Smart Summarization: Automatically condenses long text into a concise summary.
- Fixed Length Constraints: The backend generates summaries with a length between 40 and 150 tokens to ensure consistency. These values are hardcoded in the `summarize_text` function and can be adjusted as needed.

- Factual Accuracy: Uses greedy decoding (do_sample=False) to prioritize factual consistency and predictable results.
- Terminal Testing Mode: Includes a built-in testing block to verify logic without needing a frontend.

---

## Installation and Setup

1. Create a Virtual Environment (Recommended):
   ```bash
   python -m venv venv
   ```

2. Activate the Environment:
   - Windows: .\venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Note: On the first run, the system will download approximately 1.6GB for the BART model. Ensure you have a stable internet connection.

---

## How to Run and Test

### 1. Backend Testing (Terminal)
To test the summarization logic directly in your terminal, run:
```bash
python backend.py
```
It will prompt you to paste a text and will print the generated summary.

### 2. Streamlit Integration (For Frontend)
To integrate this backend into a Streamlit app, import the summarize_text function:

```python
import streamlit as st
from backend import summarize_text

# In your Streamlit app:
user_input = st.text_area("Paste text here...")
if st.button("Summarize"):
    summary = summarize_text(user_input)
    st.write(summary)
```

---

## Requirements
The project depends on the following libraries (listed in requirements.txt):
- transformers: To load the BART model and pipeline.
- torch: The deep learning framework required by the model.
- streamlit: Required if building the frontend app.

## Important Notes
- Minimum Input: The backend requires at least 30 words to generate a meaningful summary.
