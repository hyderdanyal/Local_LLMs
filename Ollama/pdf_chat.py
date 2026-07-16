import streamlit as st
import ollama
import fitz
import os

#Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    doc= fitz.open(uploaded_file)
    text=""
    for page in doc:
        text+=page.get_text()
    return text

def save_uploaded_file(uploaded_file):
    # Get the current working directory
    save_path = os.getcwd()
    #Create the full path to save the file
    file_path = os.path.join(save_path, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return st.success(f"Saved file: {uploaded_file.name} at {save_path}")

st.title("Chat with PDF")
uploaded_file = st.file_uploader("Choose a PDF file...", type=["pdf"])
print(uploaded_file)

if uploaded_file is not None:
    save_uploaded_file(uploaded_file)

    # Extract text from the uploaded PDF
    pdf_text = extract_text_from_pdf(uploaded_file)

    st.subheader("PDF Content:")
    st.write(pdf_text)

    prompt = st.text_area(label="Ask a question based on the PDF content:")
    button = st.button("Send")

    if button:
        if prompt:
            #Combine the PDF text and the user's question into a single prompt
            combined_prompt = f"Based on the content of the PDF: {pdf_text}\n\nUser's question: {prompt}"
            response = ollama.generate(
                model="llama3.2-sm", 
                prompt=combined_prompt)
            st.markdown(response['response'])