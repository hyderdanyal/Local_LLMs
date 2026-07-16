import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

st.title("Local LLM with LangChain")

# Input for the prompt
user_name = st.text_input("Enter your name:")
topic = st.text_input("Enter a topic:")
question = st.text_area("Enter your question:")
instructions = st.text_area("Enter any additional instructions:")
button= st.button("Send")

if button:
    if user_name and topic and question and instructions:
        # Create an instance of the Ollama class
        llm = OllamaLLM(model="llama3.2")  # Specify the model you want to use

        # Create a prompt template
        template = """You are a helpful assistant. {name} has asked a question about {topic}, 
        Question: {question}
        Additional instructions: {instructions}
        Please provide a detailed and thoughtful response"""

        prompt_template = PromptTemplate(template=template, input_variables=["name", "topic", "question", "instructions"])

        # Create an LLMChain with the prompt template and the LLM
        chain = prompt_template | llm

        # Generate a response using the prompt
        response = chain.invoke({"name": user_name, "topic": topic, "question": question, "instructions": instructions})

        # Display the response
        st.markdown("Response:")
        st.markdown(response)