import spacy

nlp = spacy.load("en_core_web_md")

def split_text_into_sentences(text):
    """
    Splits the input text into sentences using SpaCy's sentence segmentation.
    """
    doc = nlp(text)
    for sent in doc.sents:
        print(sent.text)
    return [sent.text for sent in doc.sents]

def calculate_similarity(reference_sentence, sentences):
    """
    Calculates the similarity between a reference sentence and a list of sentences.
    """
    similarities = []
    for sentence in sentences:
        similarity_score = nlp(reference_sentence).similarity(nlp(sentence))
        similarities.append((sentence, similarity_score))
    
    return similarities

def reorder_sentences_by_similarity(similarities):
    """
    Reorders the list of sentences based on their similarity to the reference sentence.
    """
    return sorted(similarities, key=lambda x: x[1], reverse=True)

# Example usage
long_text = """Modern artificial intelligence systems have transformed the way organizations process information and solve complex problems. 
Businesses across many industries are adopting AI-powered solutions to automate repetitive tasks, analyze large amounts of data, improve customer experiences, and make more informed decisions. 
Machine learning models can identify patterns in datasets, predict future outcomes, and provide recommendations that help companies optimize their operations. 
In healthcare, artificial intelligence is being used to assist doctors in analyzing medical images, detecting diseases earlier, and developing personalized treatment approaches. 
Financial institutions use AI algorithms to detect fraudulent transactions, evaluate risks, and improve investment strategies. 
As AI technologies continue to evolve, organizations are investing in intelligent systems that enhance productivity, reduce operational costs, and create new opportunities for innovation. 
However, successful implementation of artificial intelligence requires careful planning, high-quality data, appropriate security measures, and responsible management to ensure that these technologies provide accurate and reliable results.
"""
reference_sentence = "Companies are using artificial intelligence solutions to automate work, analyze data, improve customer service, and make better business decisions."

# Split the long text into sentences
sentences = split_text_into_sentences(long_text)

# Calculate similarity scores between the reference sentence and the sentences from the long text
similarities = calculate_similarity(reference_sentence, sentences)

# Reorder the sentences based on their similarity to the reference sentence
reordered_sentences = reorder_sentences_by_similarity(similarities)

# Display the reordered sentences with their similarity scores
for sentence, score in reordered_sentences:
    print(f"Similarity Score: {score:.4f} | Sentence: {sentence}")