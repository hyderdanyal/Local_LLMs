import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
import spacy

# Load the SpaCy model for English
# specy.cli.download("en_core_web_md")  # Uncomment this line if the model is not downloaded
nlp = spacy.load("en_core_web_md")

st.title("Chat with Long Story")

# Input for a long text
long_text = st.text_area("Enter a long text:", height=300)
question = st.text_input("Enter your question:")
button= st.button("Answer")

st.markdown(f"{len(long_text)} characters")

if button:
    if long_text:
        # Create an instance of the Ollama class
        llm = OllamaLLM(model="llama3.2")  # Specify the model you want to use

        # Create a prompt template for answering the question based on the long text
        template = """You are a helpful assistant. Please answer the following question based on the provided text:
        Text: {text}
        Question: {question}
        """
        
        prompt_template = PromptTemplate(template=template, input_variables=["text", "question"])

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
        chunks = text_splitter.create_documents([long_text])

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