# Word Embedding

Word embedding is a technique in **Natural Language Processing (NLP)** used to represent words in a continuous vector space where similar words have similar representations.  

## Key Points
- Words are converted into **dense vectors** of real numbers instead of sparse one-hot encodings.  
- Captures **semantic meaning**: words with similar context are placed closer in the vector space.  
- Helps machine learning models understand relationships between words.

## Popular Methods
- **Word2Vec**: Uses skip-gram or CBOW models to learn embeddings.  
- **GloVe (Global Vectors)**: Learns embeddings based on word co-occurrence statistics.  
- **FastText**: Extends Word2Vec by considering subword information (character n-grams).  
- **Contextual Embeddings (BERT, ELMo, GPT)**: Provide different embeddings for the same word depending on context.

## Advantages
- Improves performance of NLP tasks like sentiment analysis, translation, and text classification.  
- Handles semantic similarity better than bag-of-words or TF-IDF.  
- Reduces dimensionality and sparsity.  

## Example
- "king" - "man" + "woman" ≈ "queen"  
This shows how embeddings capture semantic and syntactic relationships.  
