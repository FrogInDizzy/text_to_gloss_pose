# !/opt/homebrew/bin/python3.9
# -*- coding: utf-8 -*-
"""
@Author         :  Edwin Gao
@Version        :  macos 14.0, python3.9
------------------------------------
@IDE            ： PyCharm
@Description    :  
@CreateTime     :  6/24/24 4:23 PM
------------------------------------
"""
import spacy
nlp = spacy.load('en_core_web_sm')
def lemmatize_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc])

lemmatized_text = lemmatize_text("He is running to the store.")
# Output: "he be run to store"
print(lemmatized_text)