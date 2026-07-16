import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

st.title("Local LLM with LangChain")

# Input for the prompt
prompt = st.text_area("Enter your prompt:")
button= st.button("Send")

if button:
    if prompt:
        # Create an instance of the Ollama class
        llm = OllamaLLM(model="llama3.2-sm ")  # Specify the model you want to use

        # Create a prompt template
        template = """You are a helpful assistant. you have been asked the following question:
        Question: {question}
        
        Please provide a detailed and thoughtful response as a list with short items"""

        prompt_template = PromptTemplate(template=template, input_variables=["question"])

        # Create an LLMChain with the prompt template and the LLM
        chain = prompt_template | llm

        # Generate a response using the prompt
        response = chain.invoke({"question": prompt})

        # Display the response
        st.markdown("Response:")
        st.markdown(response)