from chromaClient import ChromaDBClient
from embeddings import EmbeddingModel
from crossEncoder import CrossEncoder

class Query:
    def __init__(self):
        self.embedding_function = EmbeddingModel().get_embedding_function()
        self.collection = ChromaDBClient().get_or_create_collection("rag-local-collection", self.embedding_function)
        self.encoder= CrossEncoder()

    def query_collection(self, query, n_results=3):
        try:
            results = self.collection.query(query_texts=[query], n_results=n_results)
            return results
        except Exception as e:
            return {
                "error": str(e),
                "documents": [[]],
                "ids": [[]],
                "metadatas": [[]],
            }
        
    def re_rank_results(self, prompt, documents):
        # Implement re-ranking logic here using cross-encoders or other methods
        # This is a placeholder implementation and should be replaced with actual re-ranking logic
        relevant_texts, relevant_text_ids = self.encoder.encode(prompt, documents)
        return relevant_texts, relevant_text_ids