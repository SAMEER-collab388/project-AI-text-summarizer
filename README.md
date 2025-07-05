
🧠 Project: AI Text Summarizer  in Python


---

📌 Goal:

Build a web app that allows users to input long text and receive a concise summary using a Generative AI model (GPT-3.5 from OpenAI).


---

🔧 Tools & Libraries:

Python: Programming language.

Streamlit: For building the web interface.

OpenAI: To access the GPT-3.5-turbo model.

Environment Variables: To securely store your API key.



---

🗂️ Code Explanation:

✅ 1. Import Required Libraries

import os
import openai
import streamlit as st

os: Used to access environment variables like the API key.

openai: The official OpenAI library to talk to GPT models.

streamlit: Used to make a simple and interactive UI.



---

✅ 2. Set Your API Key

openai.api_key = os.getenv("OPENAI_API_KEY")

Fetches the API key securely from the system environment.

This avoids hardcoding sensitive info directly into the file.



---

✅ 3. Create the App Title

st.title("🧠 AI Text Summarizer with GPT")

Shows the title on the Streamlit web app.



---

✅ 4. Text Input Area

input_text = st.text_area("Paste your long text here:")

Allows users to paste a long paragraph or article for summarization.



---

✅ 5. Button to Trigger Summarization

if st.button("Summarize"):

Starts summarization only when the user clicks the "Summarize" button.



---

✅ 6. Check if Text is Empty

if input_text.strip() == "":
    st.warning("Please enter some text to summarize.")

Warns the user if they click the button without entering any text.



---

✅ 7. Send Request to OpenAI API

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


temperature=0.7: Adds some randomness to results.

max_tokens=200: Controls how long the summary can be.



---

✅ 8. Display the Summary

summary = response['choices'][0]['message']['content']
st.success("✅ Summary:")
st.write(summary)

Extracts the summary from the API response.

Shows it nicely in the app.



---

✅ 9. Error Handling

except Exception as e:
    st.error(f"Error: {e}")

Displays any issues (like wrong API key, too much text, or API quota exceeded).



---

▶️ How to Run the Project:

1. Save the code to a file, e.g., app.py.


2. Open terminal in that folder.


3. Run:


