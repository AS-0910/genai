import spacy

#downlading the trained pipeline for english language
# python -m spacy download en_core_web_sm

nlp= spacy.load("en_core_web_sm")
print(nlp.pipeline)
print(nlp.pipe_names)

##custom pipeline
source_nlp = spacy.load("en_core_web_sm")
nlp= spacy.blank("en")
nlp.add_pipe("ner",source=source_nlp)
print(nlp.pipe_names)