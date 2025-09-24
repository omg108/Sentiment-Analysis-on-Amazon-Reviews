# NLP Techniques – 3 Main Categories

Natural Language Processing (NLP) techniques can be broadly classified into **three categories**:

---

## 1. **Rule-Based Techniques**
Traditional approach using **linguistic rules** to process text.

- **Examples:**
  - Regular Expressions (Regex)
  - Part-of-Speech (POS) Tagging using predefined rules
  - Grammar-based parsing
- **Use Cases:**  
  - Text cleaning  
  - Pattern matching  
  - Simple chatbots  

---

## 2. **Statistical / Machine Learning Techniques**
Uses **probabilistic models** and ML algorithms to learn from data.

- **Examples:**
  - Naive Bayes
  - Hidden Markov Models (HMM)
  - Logistic Regression, SVM
  - TF-IDF + ML classifiers
- **Use Cases:**  
  - Sentiment analysis  
  - Text classification  
  - Named Entity Recognition (NER)  

---

## 3. **Neural Network / Deep Learning Techniques**
Uses **deep learning architectures** for complex language understanding.

- **Examples:**
  - RNN, LSTM, GRU
  - Transformers (BERT, GPT)
  - Seq2Seq models
- **Use Cases:**  
  - Machine Translation  
  - Text Summarization  
  - Question Answering  
  - Chatbots with contextual understanding  

---

**Summary:**  
| Category               | Key Strengths                 | When to Use                          |
|----------------------|----------------------------|------------------------------------|
| **Rule-Based**       | Simple, interpretable       | When patterns are clear & fixed    |
| **Statistical/ML**   | Data-driven, flexible       | For classification & prediction    |
| **Deep Learning**    | Contextual, highly accurate | For complex NLP (e.g., translation, summarization) |



# Basic NLP Tasks in Real Life

Natural Language Processing (NLP) is applied in many day-to-day applications.  
Here are the most common **basic NLP tasks** you should know:

---

## 1. **Text Classification**
Assigning predefined labels or categories to text.

- **Examples:**  
  - Spam vs. Ham email filtering  
  - Sentiment analysis (positive, negative, neutral)  
  - News categorization (sports, politics, tech)  

---

## 2. **Tokenization**
Breaking text into smaller units (words, sentences, or subwords).

- **Examples:**  
  - Splitting "I love NLP!" → ["I", "love", "NLP", "!"]  
  - Used in almost every NLP pipeline  

---

## 3. **Stopword Removal**
Filtering out common words that carry little meaning.

- **Examples:**  
  - Remove words like "the", "is", "on" before analysis  
  - Helps focus on important keywords  

---

## 4. **Stemming & Lemmatization**
Reducing words to their base/root form.

- **Examples:**  
  - Stemming: "running", "runs" → "run" (rough cut)  
  - Lemmatization: "better" → "good" (linguistically accurate)  

---

## 5. **Named Entity Recognition (NER)**
Identifying key entities in text.

- **Examples:**  
  - Extracting names: "Elon Musk" → PERSON  
  - Extracting locations: "New York" → LOCATION  
  - Extracting dates: "12 Sep 2025" → DATE  

---

## 6. **Part-of-Speech (POS) Tagging**
Labeling each word with its grammatical role.

- **Examples:**  
  - "Dogs bark loudly" → Noun-Verb-Adverb  

---

## 7. **Text Summarization**
Creating a shorter version of text while preserving meaning.

- **Examples:**  
  - News article summaries  
  - Automatic meeting notes  

---

## 8. **Machine Translation**
Automatically translating text between languages.

- **Examples:**  
  - English → Hindi using Google Translate  

---

## 9. **Question Answering & Chatbots**
Extracting or generating relevant responses from text.

- **Examples:**  
  - Siri, Alexa, ChatGPT  
  - FAQ bots on websites  

---

## 10. **Text Generation**
Creating human-like text.

- **Examples:**  
  - Auto-complete in search engines  
  - AI writing assistants  

---

**Summary Table**

| NLP Task             | Real-Life Example                   | Tools/Libraries        |
|---------------------|-----------------------------------|---------------------|
| Text Classification | Spam filter, sentiment analysis   | scikit-learn, spaCy |
| Tokenization        | Breaking text into words/sentences| NLTK, spaCy         |
| Stopword Removal    | Remove "the, is, on" from text    | NLTK, spaCy         |
| Stemming/Lemma      | Reduce "running" → "run"          | NLTK, spaCy         |
| NER                 | Extract names, dates, locations   | spaCy, HuggingFace  |
| POS Tagging         | Identify noun, verb, adj          | spaCy, NLTK         |
| Summarization       | Auto news summaries               | HuggingFace, GPT    |
| Translation         | English → Hindi                   | Google Translate API|
| Question Answering  | Chatbots, virtual assistants      | Transformers, Rasa  |
| Text Generation     | Auto-complete, AI writers         | GPT, LLMs           |

