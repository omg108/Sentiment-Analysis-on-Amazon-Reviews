# Stemming vs Lemmatization in spaCy & NLTK

- **spaCy**
  - ✅ Supports **Lemmatization** only.
  - ❌ Does **not** have built-in stemming.
  - Lemmatization is rule-based + vocabulary-based, giving meaningful base words.
  - Example: `running → run`, `children → child`, `ate → eat`.

- **NLTK**
  - ✅ Supports **Stemming** (e.g., `PorterStemmer`, `LancasterStemmer`).
  - ✅ Supports **Lemmatization** (via `WordNetLemmatizer`).
  - Stemming is faster but may produce non-words (e.g., `dancing → danc`).
  - Lemmatization uses WordNet to return correct dictionary words.

---

### Key Difference
- **Stemming** = mechanical rule-based chopping → may lose meaning.
- **Lemmatization** = uses linguistic rules → gives meaningful base word.
- **spaCy** = only lemmatization, **NLTK** = both.


![](images/Screenshot_2025-09-24_194823)
![](images/Screenshot_2025-09-24_194914)


---
