##python -m  spacy download en_core_web_lg 

import spacy

##large model has word vectors, but small and medium do not have word vectors.
nlp = spacy.load('en_core_web_lg')

text = "I like to eat pizza abcdefg"
doc = nlp(text)

for token in doc:
    print(token.text, token.has_vector, token.is_oov)

for token in doc:
    print(token.text, token.vector[:5])

##check similarity between words
base_word = nlp("king")
similar_words = nlp("queen man woman apple")
for token in similar_words:
    print(token.text, base_word.similarity(token))