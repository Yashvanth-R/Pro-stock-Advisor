import streamlit as st
import openai
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(question, paper_urls):
    # Combine the question with paper URLs to form the prompt
    prompt = f"Question: {question}\nPaper URLs: {', '.join(paper_urls)}"

    # Get the response from OpenAI API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app layout
st.title('IEEE Paper Chatbot')

# Sidebar for IEEE paper URLs
st.sidebar.title("Paste IEEE Paper URLs")
paper_urls = []
for i in range(3):  # Allow up to 5 paper URLs
    url = st.sidebar.text_input(f"Paper URL {i + 1}", key=f"url{i}")
    if url:
        paper_urls.append(url)

# Sidebar for asking questions
question = st.sidebar.text_input("Ask a question about the papers:")

if st.sidebar.button('Get Answer'):
    if not paper_urls:
        st.sidebar.error("Please paste at least one paper URL.")
    elif not question:
        st.sidebar.error("Please ask a question.")
    else:
        # Get the response from the chatbot
        answer = get_response(question, paper_urls)
        st.write(f"Answer: {answer}")

# Display the paper URLs
st.write("IEEE Paper URLs:")
for url in paper_urls:
    st.write(url)