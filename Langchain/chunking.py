import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.title("Text summarizer with chunking")

# Input for a long text
long_text = st.text_area("Enter a long text:", height=300)
button= st.button("Summarize")

if button:
    if long_text:
        # Create an instance of the Ollama class
        llm = OllamaLLM(model="llama3.2")  # Specify the model you want to use

        # Split the long text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = text_splitter.create_documents([long_text])

        # Create a prompt template for summarization
        template = """You are a helpful assistant. Please summarize the following text:
        {text}
        Please provide a concise summary."""
        
        prompt_template = PromptTemplate(template=template, input_variables=["text"])

        # Generate summaries for each chunk and combine them
        summaries = []
        for chunk in chunks:
            # Create LLMChain for each chunk
            chain = prompt_template | llm
            st.markdown(chunk.page_content)  # Display the chunk content
            summary = chain.invoke(chunk.page_content)
            summaries.append(summary)

        # Combine all summaries into a final summary
        final_summary = "\n\n".join(summaries)

        combined_final_summary = llm.invoke(f"Combine the following summaries into one concise summary:\n{final_summary}")

        # Display the final summary
        st.markdown("Final Summary:")
        st.markdown(combined_final_summary)