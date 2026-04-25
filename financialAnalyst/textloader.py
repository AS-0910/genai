from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def load_text_from_url(url):
    loader = UnstructuredURLLoader(urls=[url])
    documents = loader.load()
    return documents

def split_text_into_chunks(text, chunk_size=100, overlap=0):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    chunks = text_splitter.split_text(text)
    return chunks

def split_text_into_recursive_chunks(text, chunk_size=100, overlap=0):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n", "."],
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    chunks = text_splitter.split_text(text)
    return chunks

def sentence_transformer_embeddings(texts, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts)
    print(f"Generated embeddings for {len(texts)} texts.")
    print(f"Sample embedding: {embeddings.shape}")  # Print the first 5 dimensions of the first embedding
    return embeddings

def create_faiss_index(embeddings):
    embeddings = np.array(embeddings)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print(f"FAISS index created with {index.ntotal} vectors.")
    return index

def search_faiss_index(index, query_embedding, top_k=5):
    query_embedding = np.array(query_embedding).reshape(1, -1)  # Reshape to 2D
    distances, indices = index.search(query_embedding, top_k)
    print(f"Search completed. Distances: {distances}, Indices: {indices}")
    return distances, indices

if __name__ == "__main__":
    url = "https://arxiv.org/"
    documents = load_text_from_url(url)

    # print(documents)
    # chunks = split_text_into_recursive_chunks(documents[0].page_content, chunk_size=100, overlap=0)
    # for chunk in chunks:
    #     print(len(chunk))

    text = '''
    My work is software engineering.
    I am a financial analyst.
    My name is Ankur.
    I love to play cricket.
    '''

    chunks = split_text_into_recursive_chunks(text,20)
    for chunk in chunks :
        print(chunk)

    embedding=sentence_transformer_embeddings(chunks)
    index = create_faiss_index(embedding)

    query_embedding = sentence_transformer_embeddings(["What is my hobby?"])
    distances, indices = search_faiss_index(index, query_embedding, top_k=1)
    print(f"Closest chunk: {chunks[indices[0][0]]}, Distance: {distances[0][0]}")
