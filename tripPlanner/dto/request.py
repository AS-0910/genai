from pydantic import BaseModel

class RequestModel(BaseModel):
    question : str