## IDF inverse documnet frequency
"""
tf- idf  = tf * idf
tf = term frequency
idf = log(N/n) where N is the total number of documents and n is the number of documents in which the term appears
"""

from sklearn.feature_extraction.text import TfidfVectorizer

strs = [
    "Ankur is looking for a job",
    "Ankur is looking for a job in the IT industry",
    "Ankur is looking for a job in the IT industry and he is also looking for a job in the software industry"
]

v = TfidfVectorizer()
output = v.fit(strs)
print(v.vocabulary_)

all_features = v.get_feature_names_out()

for feature in all_features:
    idx= v.vocabulary_.get(feature)
    print(feature, v.idf_[idx])

check = "Ankur is looking for job in the IT industry"
check_vectorized = v.transform([check])
print(check_vectorized.toarray()[:2])


