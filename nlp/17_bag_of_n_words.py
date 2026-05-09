from sklearn.feature_extraction.text import  CountVectorizer

##bigram example (min,max)
v = CountVectorizer(ngram_range = (2,2))
v.fit(["Ankur is looking for a job"])
print(v.vocabulary_)

