import spacy
import spacy.cli
import numpy as np
import time
# Load the SpaCy model for English
# spacy.cli.download("en_core_web_md")  # Uncomment this line if the model is not downloaded
nlp = spacy.load("en_core_web_md")


# Function to get embedding and similarity score between two texts
def calculate_similarity(text1, text2):
    # Process the texts using SpaCy
    vector1 = nlp(text1).vector
    vector2 = nlp(text2).vector
    # similarity = vector1 @ vector2 / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    similarity = nlp(text1).similarity(nlp(text2))
    return similarity


# Input texts for comparison
text1 = """Artificial intelligence is changing the way businesses operate by automating tasks, analyzing large amounts of data, and helping organizations make better decisions. 
Machine learning algorithms allow computers to learn from experience and improve their performance without being explicitly programmed. 
Many companies are using AI technologies to improve customer service, optimize processes, and create new products."""
text2 = """AI is transforming modern businesses by automating repetitive work, processing huge volumes of information, and supporting smarter decision-making. 
Machine learning techniques enable computers to learn from data and become more accurate over time without requiring direct instructions for every task. 
Organizations are adopting artificial intelligence solutions to enhance customer support, streamline operations, and develop innovative services."""
# text2 = """The Amazon rainforest contains millions of plant and animal species and plays an important role in maintaining the Earth's climate. 
# Scientists study its ecosystem to understand biodiversity and the impact of environmental changes."""

start = time.time()

# Calculate similarity between the two texts
for i in range(100):  # Run the similarity calculation 100 times
    similarity_score = calculate_similarity(text1, text2)
end = time.time()
print(f"Time taken: {end - start}")

# print the similarity score
print(f"Similarity score between the two texts: {similarity_score:.4f}")


