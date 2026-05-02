from sentence_transformers import CrossEncoder as STCrossEncoder

class CrossEncoder:
    def __init__(self):
        self.model = STCrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        # Initialize your cross-encoder model here (e.g., load the model)

    def encode(self, prompt, documents : list[str])->tuple[str, list[int]]:
        relevant_text = ""
        relevant_text_ids = []

        ## return type is list of dicts with keys "corpus_id" and "score"
        ranks = self.model.rank(prompt, documents, top_k=3)
        for rank in ranks:
            relevant_text += documents[rank["corpus_id"]]
            relevant_text_ids.append(rank["corpus_id"])

        return relevant_text, relevant_text_ids
    