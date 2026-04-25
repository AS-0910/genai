from langchain_community.llms.google_palm import GooglePalm
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
print(f"Environment variables loaded successfully : {os.getenv('api_key')}")

