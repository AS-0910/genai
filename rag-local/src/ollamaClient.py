import ollama

class OllamaClient:
    client = None

    def __init__(self):
        if(self.client is None):
            self.client = ollama.Client()
        else:
            print("Ollama client already exists.")

    def get_client(self):
        return self.client

    def query(self, collection_name, query):
        return self.client.query(collection_name=collection_name, query=query)