import os
import re
from string import punctuation
from collections import Counter

import nltk
from nltk.corpus import stopwords
from string import punctuation

import pymorphy2
from pymystem3 import Mystem
#nltk.download('punkt')
nltk. download('stopwords')

morf = pymorphy2.MorphAnalyzer()
russian_stopwords = stopwords.words("russian")
mystem = Mystem()

def preprocess_text(text):
    print(9)
    tokens = mystem.lemmatize(text.lower())
    print(6)
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]
    print(7)
    text = " ".join(tokens)
    print(8)
    return text

"""
data_collection = os.listdir("data")
for file in data_collection:
    print('1')
    f = open('data/' + file, 'r', encoding='utf-8')
    text = f.read()
    text = re.sub(r'[^\w\s]','', text)
    nltk_tokens = nltk.word_tokenize(text)
    f.close()
    print('2')
    for word_id in range(len(nltk_tokens)):
        nltk_tokens[word_id] = morf.parse(nltk_tokens[word_id])[0].normal_form
    print('3')
    f1 = open('tokenize_data/' + file, 'w', encoding='utf-8')
    for word in nltk_tokens:
        f1.write(word + "\n")
    f1.close()
    print('4')
"""
print(1)
data_collection = os.listdir("data")
for file in data_collection:
    print(2)
    f1 = open('data/' + file, 'r', encoding='utf-8')
    f2 = open('tokenize_data/' + file, 'w', encoding='utf-8')
    print(3)
    text = f1.read()
    f1.close()
    print(4)
    text = preprocess_text(text)
    print((5))
    print(text)
    text = re.sub('\n', ' ', text)
    words = text.split(' ')
    for word in words:
        print(word)
        f2.write(word + "\n")
    f2.close()