import os
import tempfile

from ollama import create
from chromaClient import ChromaDBClient
from ollamaClient import OllamaClient
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embeddings import EmbeddingModel

class FileProcessor:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.chroma_client = ChromaDBClient()

    def get_embedding_function(self):
        return self.embedding_model.get_embedding_function()
    
    def create_collection(self, collection_name, embedding_function):
        self.collection = self.chroma_client.get_or_create_collection(
            collection_name=collection_name,
            embedding_function=embedding_function,
        )

    def convert_docs_to_chunks(self, docs):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", "?", "!", " ", ""],
        )
        return text_splitter.split_documents(docs)
    
    def add_chunks_to_collection(self, chunks, normalize_uploaded_file_name):
        ##add file to collection
        documents, metadatas, ids = [], [], []
        for idx, split in enumerate(chunks):
            documents.append(split.page_content)
            metadatas.append(split.metadata)
            ids.append(f"{normalize_uploaded_file_name}_{idx}")

        ##add file chunks to collection
        try:
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids,
            )
            return f"Added {len(chunks)} chunks to collection {self.collection.name}."
        except Exception as e:
            return f"An error occurred while adding chunks to the collection: {str(e)}"

        
    def normalize_uploaded_file_name(self, upload_file):
        return upload_file.name.translate(
                str.maketrans({"-": "_", ".": "_", " ": "_"})
        )
    
    def process_and_add_uploaded_file(self, upload_file):
        # Implement any additional processing logic here if needed
        # create temporary file and save the uploaded file to it
        try:
            temp_file = tempfile.NamedTemporaryFile("wb", suffix=".pdf", delete=False)
            temp_file.write(upload_file.read())

            loader = PyMuPDFLoader(temp_file.name)
            docs = loader.load()
            os.unlink(temp_file.name)  # Delete temp file

            ##convert ot chunks
            chunks=self.convert_docs_to_chunks(docs)

            ##get embedding function
            embedding_function = self.get_embedding_function()

            ##get or create collection
            self.create_collection(collection_name="rag-local-collection", embedding_function=embedding_function)

            ##add chunks to collection
            response = self.add_chunks_to_collection(chunks, self.normalize_uploaded_file_name(upload_file))

            return response
        except Exception as e:
            return f"An error occurred while processing the file: {str(e)}"


        
    
    

    
    