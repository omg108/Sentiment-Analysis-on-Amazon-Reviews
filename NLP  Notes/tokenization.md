# Tokenization in NLP (with spaCy)

## What is Tokenization?
**Tokenization** is the process of breaking down text into smaller units called **tokens**.  
Tokens can be:
- **Words** (most common)
- **Subwords**
- **Sentences**
- **Characters**

Tokenization is usually the **first step in NLP**, as most models work on tokens rather than raw text.

---

## Why Tokenization is Important
- Helps convert unstructured text into structured form.
- Makes it easier to perform tasks like:
  - Stopword removal
  - Lemmatization
  - Part-of-Speech tagging
  - Text classification (e.g., sentiment analysis)

---

## Tokenization Techniques

### 1. **Word Tokenization**
Splits a sentence into words.

```python
import spacy
nlp = spacy.load("en_core_web_sm")

text = "I love programming in Python! It's awesome."
doc = nlp(text)

tokens = [token.text for token in doc]
print(tokens)
