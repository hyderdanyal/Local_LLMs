import streamlit as st
from langchain_ollama import OllamaLLM


st.title("Local LLM with LangChain")

# Input for the prompt
prompt = st.text_area("Enter your prompt:")
button= st.button("Send")

if button:
    if prompt:
        # Create an instance of the Ollama class
        llm = OllamaLLM(model="llama3.2-sm ")  # Specify the model you want to use

        # Generate a response using the prompt
        response = llm.invoke(prompt)

        # Display the response
        st.markdown("Response:")
        st.markdown(response)