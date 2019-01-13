#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 09:55:08 2019

@author: vpapg
"""

from nltk.corpus import gutenberg
from math import log

# store the books in lists of lowercase words
d0 = [w.lower() for w in gutenberg.words('austen-emma.txt')]
d1 = [w.lower() for w in gutenberg.words('austen-persuasion.txt')]
d2 = [w.lower() for w in gutenberg.words('austen-sense.txt')]

# d0 = [w.lower() for w in gutenberg.words('austen-emma.txt') if w.isalpha()]
# not necessary, since we never count the length of the texts

D = 3   # number of texts (books) in the collection

collection = [d0, d1, d2]   # the collection of books-texts (list of lists)

def TF(word, doc_words):
    return doc_words.count(word)

def DF(word):
    df = 0
    if word in d0: df+=1
    if word in d1: df+=1
    if word in d2: df+=1
    return df

def CF(word):
    return [doc for i in collection for doc in i].count(word)

def IDF(word, doc_words):
    return log(D/DF(word))

def TFIDF(word, doc_words):
    return TF(word, doc_words)*IDF(word, doc_words)

def print_word_counts(word):
    print('\''+word+'\'')
    print('DF:',DF(word), '-- CF:',CF(word))
    print('TF0:',TF(word,d0), '-- TF1:',TF(word,d1), '-- TF2:',TF(word,d2))
    print('IDF0:',IDF(word,d0), '-- IDF1:',IDF(word,d1), '-- IDF2:',IDF(word,d2))
    print('TFIDF0:',TFIDF(word,d0), '-- TFIDF1:',TFIDF(word,d1), '-- TFIDF2:',TFIDF(word,d2))
    print()
    
print('Using Jane Austen\'s books: \'Emma\', \'Persuasion\', \'Sense and sensibility\'\n')
print_word_counts('the')
print_word_counts('family')
print_word_counts('blindness')