import os
import openai
import streamlit as st

# Set your API key (best to use env variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI Text Summarizer with GPT")

input_text = st.text_area("Paste your long text here:")

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful summarizer."},
                        {"role": "user", "content": f"Summarize the following text:\n{input_text}"}
                    ],
                    temperature=0.7,
                    max_tokens=200
                )
                summary = response['choices'][0]['message']['content']
                st.success("✅ Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
