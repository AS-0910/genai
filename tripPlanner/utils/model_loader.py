from utils.config_loader import ConfigLoader
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

class ModelLoader:
    def __init__(self):
        logger.debug("Initializing ModelLoader")
        load_dotenv()
        logger.debug("Environment variables loaded")
        self.config_loader = ConfigLoader()
        self.config = self.config_loader.get_config()
        logger.debug("Configuration loaded")

    def load_model(self):
        logger.debug("Loading LLM model...")
        llm_config = self.config.get('llm', {})
        provider = llm_config.get('provider')
        model_name = llm_config.get('model')
        logger.debug(f"LLM Config - Provider: {provider}, Model: {model_name}")
        
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            logger.warning("GOOGLE_API_KEY environment variable not set")
        else:
            logger.debug("GOOGLE_API_KEY found")

        #can use factory design pattern here later
        context=f"{provider}:{model_name}"
        logger.debug(f"Model context: {context}")
        
        if provider == 'google_genai':
            logger.info(f"Loading {model_name} from Google GenAI")
            return init_chat_model(context, api_key=api_key)
        else:
            logger.error(f"Unsupported LLM provider: {provider}")
            raise ValueError(f"Unsupported LLM provider: {provider}")

# if __name__ == "__main__":
#     model_loader = ModelLoader()
#     model = model_loader.load_model()
#     print(model.invoke("Hello, how are you?"))