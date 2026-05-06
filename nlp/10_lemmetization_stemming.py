import nltk
import spacy

from nltk.stem import PorterStemmer

stmer = PorterStemmer()
print(stmer.stem("running"))

npl = spacy.load("en_core_web_sm")
doc = npl("I ate apple while returning to my home")

##pos example
for token in doc:
    print(token.text, " | ", token.lemma_ , " | ", token.pos_)

##ner example
doc = npl("I have 40 dollar from Apple")
for token in doc.ents:
    print(token.text, " | ", token.label_)


