from chromaClient import get_or_create_collection
from embeddings import get_embedding_function
from crossEncoder import CrossEncoderModel

class Query:
    def __init__(self):
        self.embedding_function = get_embedding_function()
        self.collection = get_or_create_collection("rag-local-collection", self.embedding_function)
        self.encoder= CrossEncoderModel()

    def query_collection(self, query, n_results=5):
        try:
            results = self.collection.query(query=query, n_results=n_results)
            return results
        except Exception as e:
            return f"An error occurred while querying the collection: {str(e)}"
        
    def re_rank_results(self, prompt, documents):
        # Implement re-ranking logic here using cross-encoders or other methods
        # This is a placeholder implementation and should be replaced with actual re-ranking logic
        relevant_texts, relevant_text_ids = self.encoder.encode(prompt, documents)
        return relevant_texts, relevant_text_ids