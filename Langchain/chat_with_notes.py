import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
import spacy

# Load the SpaCy model for English
# specy.cli.download("en_core_web_md")  # Uncomment this line if the model is not downloaded
nlp = spacy.load("en_core_web_md")

st.title("Chat with Notes")

with st.form(key="my_form", clear_on_submit=True):
    # Input for a long text
    note = st.text_area("Enter your notes:", height=300)
    
    submit_button = st.form_submit_button(label="Save")

if submit_button:
    if note:
        with open("notes.txt", "r") as file:
            content = file.read()
            if note not in content:
                content += note + "\n"
                with open("notes.txt", "w") as file:
                    file.write(content)

question = st.text_input("Enter your question:")
button= st.button("Ask")

if button:
    if question:
        # Create an instance of the local LLM
        llm = OllamaLLM(model="llama3.2")  # Specify the model you want to use

        # Create a prompt template for answering the question based on the long text
        template = """You are a helpful assistant. Please answer the following question based on the provided text:
        Text: {text}
        Question: {question}
        """
        
        prompt_template = PromptTemplate(template=template, input_variables=["text", "question"])

        with open("notes.txt", "r") as file:
            content = file.read()

        # Split the long text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = text_splitter.create_documents([content])

        # Initialize a list to store the similarities
        similarities = []

        # Generate a summary for each chunk and calculate similarity with the question
        for chunk in chunks:
            similarity_score = nlp(question).similarity(nlp(chunk.page_content))
            similarities.append((similarity_score, chunk.page_content))

        ordered_chunks = sorted(similarities, key=lambda x: x[0], reverse=True)[:3]  # Get the top 3 most similar chunks

        text=""
        for score, sentence in ordered_chunks:
            st.markdown(f"Similarity Score: {score:.4f} | Sentence: {sentence}")
            text += sentence + "\n"

        chain = prompt_template | llm
        answer = chain.invoke({"text": text, "question": question})

        # Display the answer
        st.markdown("Answer:")
        st.markdown(answer)