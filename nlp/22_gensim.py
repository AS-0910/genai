import gensim.downloader as api

wv = api.load("word2vec-google-news-300")

print(wv.similarity("king", "queen"))

print(wv.most_similar("king", topn=2))

print(wv.most_similar(positive=["king", "woman"], negative=["man"]))