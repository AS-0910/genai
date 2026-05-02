from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)

class EmbeddingModel:
    ollama_ef = None
    
    def __init__(self):
        if self.ollama_ef is None:
            self.ollama_ef = OllamaEmbeddingFunction(
                url="http://localhost:11434/api/embeddings",
                model_name="nomic-embed-text:latest",
            )
        else:
            print("Ollama embedding function already exists.")

    def get_embedding_function(self):
        return self.ollama_ef
    