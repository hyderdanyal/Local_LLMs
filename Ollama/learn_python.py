import streamlit as st
import ollama
import io
import sys

st.title("Learn Python with ChatBot")
prompt = st.text_area(label="Enter your prompt:")
button = st.button("Send")

if button:
    if prompt:
        while True:
            response = ollama.generate(
                model="llama3.2", 
                prompt=prompt + "\nNote: Output must have only Python code. Do not include any explanations or text. Only provide the code.")
            
            old_stdout = sys.stdout
            sys.stdout = buffer = io.StringIO()

            code = response['response'].replace("python", "").replace("```", "").strip()
            try:
                exec(code)
            except Exception as e:
                print(f"Error executing generated code: {e}")

            sys.stdout = old_stdout
            output = buffer.getvalue()

            if "Error executing generated code" in output:
                prompt = f"""
                The previous code had an error: {output}. Please provide a corrected version of the code: {code}
                """
                st.markdown(f'Code has error, fixing... \n{response["response"]} \n {output}')
            else:
                st.markdown(f'Code executed successfully: \n{response["response"]} \n {output}')
                st.session_state["response"] = response['response']
                break

question = st.text_area(label="Ask a question about the code:")
ask = st.button("Ask")
if ask:
    st.markdown(st.session_state["response"])
    prompt = f"""
            Can you explain why we used this code "{question}" in the folowing code: {st.session_state["response"]} step by step and explain the logic behind it. Please provide a detailed explanation.
            """
    answer = ollama.generate(
        model="llama3.2-sm",
        prompt=prompt
    )
    st.markdown(f'Answer: {answer["response"]}')