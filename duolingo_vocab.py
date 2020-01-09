#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:05:43 2020

@author: vpapg
"""


import duolingo
# https://github.com/KartikTalwar/duolingo

username = str(input("Enter your username: "))
passw = str(input("Enter your password: "))
print('\n***** Connecting to your account...')
lingo = duolingo.Duolingo(username, password=passw)
print('***** Connection established.')

def retrieve_vocab(duolingo_account, language, filename):
    vocab = duolingo_account.get_vocabulary(language_abbr = language)
    
    skills = set()
    for skill in vocab['vocab_overview']:
        skills.update([skill['skill']])
    
    with open(filename, 'w') as f:
        for skill in skills:
            for item in vocab['vocab_overview']:
                if item['skill'] == skill:
                    f.write(str(item['word_string']) + '\t' +str(item['normalized_string'])+'\t'+str(item['skill'])+'\n')

while True:
    lang = str(input("Select a language (give its abbreviation, e.g. ru, de, en): "))
    filename = str(input("Give the desired path (including the filename) for the vocabulary txt file: "))
    try:    # TO DO: when a language is non-existant (e.g. 'da'), there is no error -> it creates an empty file
        retrieve_vocab(lingo, lang, filename)
        print('\n***** Vocabulary has been successfully stored in', filename)
    except:
        print('\n[ERROR] No vocabulary found for this language!')
    repeat = str(input("Do you want to retrieve the vocabulary for another language? [y/n]: "))
    while repeat != 'y' and repeat != 'n':
        repeat = str(input("Do you want to retrieve the vocabulary for another language? [y/n]: "))
    if repeat == 'n':
        print('\n***** Goodbye!')
        break
        