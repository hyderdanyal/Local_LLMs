import streamlit as st
import ollama

st.title("Ollama LLM Chatbot")
prompt = st.text_area(label="Enter your prompt:")
if(st.button("Send")):
    # response = ollama.chat(
    #     model="llama3.2-sm", 
    #     messages=[
    #         {"role": "user", "content": prompt},
    #     ])
    # st.write(response['message']['content'])

        response = ollama.generate(
        model="llama3.2-sm", 
        prompt=prompt)
        st.write(response['response'])