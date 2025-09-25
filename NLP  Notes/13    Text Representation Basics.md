# Text Representation Basics

In the NLP pipeline, one important step is **feature engineering**.  

- Instead of representing text directly as words, we convert them into **vectors**.  
- These vectors contain a set of features (not always directly interpretable to us).  
- This process is also known as:  
  - **Feature Engineering**  
  - **Vector Space Model**  

👉 It allows algorithms to process text numerically for tasks like classification, clustering, and similarity measurement.


# Ways of Text Representation

There are various ways to represent text as vectors:

- **One-Hot Encoding** → Each word is represented as a binary vector.  
- **Bag of Words (BoW)** → Counts word occurrences in documents.  
- **TF-IDF** → Weights words by frequency and importance across documents.  
- **Word Embeddings** → Dense vectors capturing semantic meaning (e.g., Word2Vec, GloVe, FastText).

---

👉 A **great representation with a decent model** often performs better than a **great model with a poor representation**.


# Cosine Similarity

**Cosine similarity** measures how similar two vectors are by comparing the **angle** between them, ignoring magnitude.

- **Formula:**  
\[
\text{Cosine Similarity} = \frac{A \cdot B}{||A|| \, ||B||}
\]  
where \(A \cdot B\) is the dot product, and \(||A||, ||B||\) are the vector magnitudes.

- **Range:** -1 to 1  
  - **1** → vectors point in the same direction (high similarity)  
  - **0** → vectors are orthogonal (no similarity)  
  - **-1** → vectors point in opposite directions  

- **Use in NLP:** Compare text embeddings to find semantic similarity between words, sentences, or documents.  
- **Applications:** Document similarity, semantic search, clustering, recommendations.


# Label & One-Hot Encoding

**Pipeline:**  
Raw text → Number vector → Machine learning model

## 1. Label Encoding
- Create a **vocabulary** of unique words.  
- Assign a **number** to each word.  
- Store numbers in a vector.  

## 2. One-Hot Encoding
- Create a **column for each unique word**.  
- Set **1** if the word appears, **0** otherwise.  

### ⚠️ Limitations in NLP
- Different vectors for similar words → **does not capture meaning**.  
- Large vocabulary → **high memory usage**.  
- New words → **problematic**.  
- Different text lengths → **variable vector sizes**, but ML models require **fixed-size input**.  

> In NLP, these approaches are generally **not used** due to the above limitations.
