# Sentiment Analysis on Amazon Reviews

## Project Structure

```bash
Sentiment-Analysis-on-Amazon-Reviews/
├── Data/
│   ├── amazon_reviews.md        # Large Amazon reviews dataset (Google Drive link)
│   └── amazon_alexa.tsv         # Alexa reviews dataset
│
├── NLP Notes/
│   └── ...                      # Notes and references on NLP techniques
│
├── Notebooks/
│   ├── 1.amazon_product_review_distlBERT_based.ipynb   # DistilBERT-based sentiment analysis
│   ├── 2.amazon_product_review_ML_based.ipynb         # ML-based sentiment analysis
│   └── 3.basic_alexa_review.ipynb                     # Basic Alexa review analysis
│
├── models/
│   ├── CountVectorizer_n-grams_Naive-Bayes_model.md   # Naive Bayes model (Google Drive link)
│   ├── Fine-tuned_DistilBERT_transformer_model.md     # DistilBERT model (Google Drive link)
│   └── basic_alexa_review_model.pkl                   # Alexa review ML model
│
├── static/
│   └── style.css               # CSS for web app
│
├── templates/
│   └── index.html              # HTML template for web app
│
├── uploads/
│   └── ...                     # Folder for user-uploaded files
│
├── app.py                      # Main app script (Flask)
├── README.md                   # Project overview and instructions
└── Requirement.txt             # Python dependencies
```



# Table of Contents
- [Introduction](#introduction)
- [Description](#description)
- [Tech Stack](#tech-stack)
- [Contributors](#contributors)
- [Future Prospects](#future-prospects)
- [Resources](#resources)
- [Acknowledgement](#acknowledgement)

## Introduction
This project focuses on performing sentiment analysis on Amazon product reviews. It allows users to analyze text data and classify reviews as positive, negative, or neutral. The system also includes analysis of Alexa product reviews.

## Description
The project implements multiple approaches for sentiment analysis:

- Traditional Machine Learning models (Naive Bayes, Random Forest)
- Transformer-based models (DistilBERT fine-tuned on Amazon reviews)

The project includes both exploratory data analysis (EDA) and model deployment via a web application.

## Tech Stack
- Python
- Jupyter Notebook
- Scikit-learn
- PyTorch
- Transformers
- Flask

## Contributors
- Om Gaikwad

## Future Prospects
- Expand to multi-lingual Amazon reviews
- Integrate other pre-trained models like BERT, RoBERTa
- Deploy as a full web service with user-upload support
- Build real-time sentiment dashboards

## Resources
- Amazon Reviews Dataset
- HuggingFace Transformers
- Scikit-learn Documentation
- Flask Documentation

## Acknowledgement
- HuggingFace community for pre-trained models
- Open-source contributors for Python libraries and tools
- CodeBasics NLP tutorials on YouTube for beginner-friendly guidance

