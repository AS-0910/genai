from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)

class RequestModel(BaseModel):
    question : str