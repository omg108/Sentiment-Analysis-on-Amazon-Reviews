# TF-IDF (Term Frequency-Inverse Document Frequency)

**Definition:**  
TF-IDF is a statistical measure used to evaluate the importance of a word in a document relative to a collection (corpus) of documents. It helps in text analysis, search engines, and NLP tasks like document ranking and feature extraction.

---

## Components

1. **Term Frequency (TF):**  
Measures how frequently a term appears in a document.  
\[
TF(t, d) = \frac{\text{Number of times term t appears in document d}}{\text{Total number of terms in document d}}
\]

2. **Inverse Document Frequency (IDF):**  
Measures how important a term is across the corpus. Rare terms get higher weight.  
\[
IDF(t) = \log \frac{\text{Total number of documents}}{\text{Number of documents containing term t}}
\]

---

## TF-IDF Formula

\[
TF\text{-}IDF(t, d) = TF(t, d) \times IDF(t)
\]

- High TF-IDF → Term is important in that document.
- Low TF-IDF → Term is common or less relevant.

---

## Uses

- Feature extraction for text classification.
- Search engines to rank documents by relevance.
- Keyword extraction and information retrieval.


With BOW following problem may arise
![](images/Screenshot_20-09-27_083242.png)


By this model may think article 1 & 3 are similar .

Some may say that it is stop words so why we are not removing them directly. Yes this is right approach but stop word can help us to a certain extent.

So another approach is we find the this terms appeared in how many articles


![](images/Screenshot_20-09-27_083622.png)

So if word is appearing in the majority of the articles or document we should lower it's influence because it is may generic term.

We use following formula to see amount of influence it should have.
Formue is in inverse so more IDF (inverse document frequency)

![](images/Screenshot_20-09-27_132806.png)
![](images/Screenshot_20-09-27_133055.png)
![](images/Screenshot_20-09-27_133145.png)
![](images/Screenshot_20-09-27_133359.png)
![](images/Screenshot_20-09-27_133528.png)
![](images/Screenshot_20-09-27_133546.png)
