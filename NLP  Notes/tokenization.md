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

['I', 'am', 'learning', 'Natural', 'Language', 'Processing', 'using', 'spaCy', '.']

2. Sentence Tokenization with spaCy
import spacy

nlp = spacy.load("en_core_web_sm")
text = "I love NLP. It is fascinating. Let's learn together!"
doc = nlp(text)

sentences = [sent.text for sent in doc.sents]
print(sentences)


Output:

['I love NLP.', 'It is fascinating.', "Let's learn together!"]

3. Tokenization with NLTK
from nltk.tokenize import word_tokenize, sent_tokenize

text = "I love learning NLP. Tokenization is the first step!"

# Word Tokenization
word_tokens = word_tokenize(text)
print(word_tokens)

# Sentence Tokenization
sentence_tokens = sent_tokenize(text)
print(sentence_tokens)


Output:

['I', 'love', 'learning', 'NLP', '.', 'Tokenization', 'is', 'the', 'first', 'step', '!']
['I love learning NLP.', 'Tokenization is the first step!']

4. Regex-Based Tokenization

Useful when you want custom rules for tokenization.

import re

text = "Email me at abc@example.com or visit https://example.com"
tokens = re.findall(r"[A-Za-z0-9@.]+", text)
print(tokens)


Output:

['Email', 'me', 'at', 'abc@example.com', 'or', 'visit', 'https://example.com']

5. Subword Tokenization (Byte Pair Encoding - BPE)

Used in modern NLP models like BERT, GPT, etc.
Example (conceptual):

"playing" → ["play", "ing"]
"unhappiness" → ["un", "happiness"]


(BPE is not directly implemented in spaCy but is used internally in transformer models.)

6. Character-Level Tokenization
text = "NLP"
tokens = list(text)
print(tokens)


Output:

['N', 'L', 'P']

