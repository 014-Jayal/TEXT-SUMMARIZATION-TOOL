# TEXT-SUMMARIZATION-TOOL

*COMPANY*: CODTECH IT SOLUTUIONS

*NAME*: JAYAL SHAH

*INTERN ID*: CODF94

*DOMAIN*: Artificial Intelligence Markup Language

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH



---

# 🧠 Text Summarization Tool

This repository contains a simple yet effective **Text Summarization Tool** built in Python using **Natural Language Processing (NLP)** techniques. The goal of this project is to provide a concise extractive summary of a given article—specifically, it demonstrates summarization by scraping and processing the **Wikipedia article on Natural Language Processing**.

## 🔍 How It Works

The tool follows a classic pipeline for extractive text summarization. It begins by web scraping a target article, performs extensive text preprocessing, analyzes word frequencies, and finally scores and ranks sentences to generate a coherent summary composed of the most relevant ones. Here’s a step-by-step breakdown of the key operations:

1. **Web Scraping**:
   The script uses `urllib` and `BeautifulSoup` to fetch and parse the HTML content of a Wikipedia article. It extracts all paragraphs (`<p>` tags) and consolidates the text for analysis.

2. **Text Preprocessing**:
   The raw text is cleaned by:

   * Removing references like `[1]`, `[2]`, etc.
   * Removing special characters and digits.
   * Reducing redundant whitespace.

   This cleaned version is also lowercased and stripped of unnecessary formatting to prepare for tokenization.

3. **Tokenization and Stopword Removal**:
   Using NLTK’s `sent_tokenize` and `word_tokenize`, the script splits the text into sentences and words. It filters out common stopwords (like “the,” “is,” “and,” etc.) and punctuation to focus on meaningful content words.

4. **Frequency Analysis**:
   The script calculates the weighted frequency of each word based on its occurrence in the cleaned text. The highest frequency is normalized to a value of 1, and all others are scaled accordingly.

5. **Sentence Scoring**:
   Each sentence is scored by summing the frequencies of its significant words, with a constraint that sentences must be fewer than 30 words to avoid overly long selections. This prioritizes concise, information-rich sentences.

6. **Summary Extraction**:
   The top 7 highest-scoring sentences are selected using Python’s `heapq` library. These sentences are then joined to form the final summary output.

7. **Visualization**:
   A frequency distribution plot of the top 30 most frequent words is generated using NLTK, giving a visual insight into the article's keyword density.

## 📦 Requirements

The script requires the following Python libraries:

* `bs4` (BeautifulSoup)
* `urllib`
* `re`
* `nltk`
* `heapq`
* `matplotlib` (for plotting)

NLTK data dependencies:

```python
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
```

## 🎯 Use Cases

This tool is ideal for:

* Quick summarization of lengthy articles.
* Educational purposes to understand basic NLP.
* Preprocessing pipeline demos in machine learning projects.

## 🚀 Future Improvements

Possible enhancements include:

* Making the URL input dynamic.
* Adding support for other languages.
* Implementing abstractive summarization using deep learning models.

---
