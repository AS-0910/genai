from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()
print(f"Environment variables loaded successfully : {os.getenv('api_key')}")

def create_google_llm():
    api_key = os.getenv('api_key')
    llm = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-3-flash-preview")
    return llm


def datbase_connection():
    db_username = os.getenv('db_username')
    db_password = os.getenv('db_password')
    db_host = os.getenv('db_host')
    db_name = os.getenv('db_name')

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}")
    return db

def create_sql_database_chain(llm, db):
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    return db_chain

def few_shot_learning_example():
    var=0
    few_shots = [
        {
            'Question': "What is the capital of France?", 
            'SQLQuery': "The capital of France is Paris.",
            'SQLResult': "Result of SQL Query",
            'Answer': var
        },
        {
            "Question": "Who is the president of the United States?",
            "SQLQuery": "The president of the United States is Joe Biden.", 
            "SQLResult": "Result of SQL Query", 
            "Answer": var
        },
        {
            "Question": "What is the largest mammal?", 
            "SQLQuery": "The largest mammal is the blue whale.", 
            "SQLResult": "Result of SQL Query",
            "Answer": var
        }
    ]



if __name__ == "__main__":
    llm = create_google_llm()
    db = datbase_connection()
    db_chain = create_sql_database_chain(llm, db)
    # print(f"Database connection established: {db.table_info}")

    # Example query to test the database chain
    query = "What are the number of nike white tshirts?"
    result = db_chain(query)
    print(f"Query Result: {result}")
