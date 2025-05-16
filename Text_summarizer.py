import bs4 as bs
import urllib.request as url
import re
import nltk
# Download the necessary NLTK data, including 'punkt_tab' which is required for sentence tokenization.
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab') # Explicitly download punkt_tab
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import heapq
from string import punctuation

#Fetch Articles from Wikipedia

# web scrape Wikipedia article on Natural Language Processing
scraped_data = url.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article,'lxml')
paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

#Text Preprocessing

# remove square brackets and extra spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

# remove special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

#Tokenize Sentences

# This line caused the error because the punkt_tab resource was missing.
# The download of punkt_tab above should resolve this.
sentence_list = nltk.sent_tokenize(article_text)

#Find Weighted Frequency of Occurrence

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}

for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords and word not in punctuation:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

#Frequency Distribution

frequency_dist = nltk.FreqDist(word_frequencies)
frequency_dist.plot(30)

#Calculate Sentence Scores

sentence_scores = {}

for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

#Extract Output Summary

summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)

summary
