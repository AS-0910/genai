import chromadb

class ChromaDBClient:
    client = None

    def __init__(self):
        if(self.client is None):
            #persistent client to save restart data / permanent data storage
            self.client =  chromadb.PersistentClient(path="./demo-rag-chroma")
        else:
            print("ChromaDB client already exists.")

    def get_client(self):
        return self.client

    def get_or_create_collection(self, collection_name, embedding_function=None):
        return self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_function,
            metadata={"hnsw:space": "cosine"},
        )
    
    def add_file_to_collection(self, collection_name, file_path):
        collection = self.get_collection(collection_name)
        collection.add(file=file_path)

    


