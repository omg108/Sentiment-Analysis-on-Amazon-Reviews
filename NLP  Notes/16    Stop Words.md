# Stop Words in NLP

**Stop Words** are common words in a language (e.g., *a, an, the, in, on, is, and, to*)  
that usually do not carry significant meaning and can be removed during text preprocessing.

---

## Why Remove Stop Words?
- **Reduce Noise** – They often don't add value for tasks like search or topic modeling.
- **Improve Efficiency** – Less data to process, faster training.
- **Better Results** – Focus on meaningful words (nouns, verbs).

---

## When to Remove Stop Words
- **Information Retrieval (Search Engines):**
  - To focus on main keywords and improve search relevance.
- **Topic Modeling / Document Classification:**
  - To capture meaningful patterns without noise.
- **Clustering / Similarity Matching:**
  - To avoid high similarity scores caused by common filler words.

---

## When *Not* to Remove Stop Words
- **Sentiment Analysis:**
  - Words like *not*, *never* change the meaning of a sentence.
- **Text Generation / Translation:**
  - Stop words are important for grammar and sentence structure.
- **Named Entity Recognition (NER):**
  - Some stop words can be part of names or entities.
- **Context-Sensitive Tasks:**
  - Removing them may lose subtle meaning (e.g., *to be or not to be*).

---

## Key Tip
Use libraries like **NLTK** or **spaCy** for stop words list but always **customize**  
the list based on your task — sometimes you may want to keep certain words.




Let's take same example of finding company name from news article 
![](images/Screenshot_2025-09-25_210138.png)



But in reality there is a lot noise as shown.
<img width="392" height="68" alt="image" src="https://github.com/user-attachments/assets/ccf33552-981f-4f08-969d-dcb0cd173eaa" />

