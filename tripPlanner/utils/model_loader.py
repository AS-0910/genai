from utils.config_loader import ConfigLoader
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

class ModelLoader:
    def __init__(self):
        load_dotenv()
        self.config_loader = ConfigLoader()
        self.config = self.config_loader.get_config()

    def load_model(self):
        llm_config = self.config.get('llm', {})
        provider = llm_config.get('provider')
        model_name = llm_config.get('model')
        api_key = os.getenv('GOOGLE_API_KEY')
        # print(api_key)

        #can use factory design pattern here later
        context=f"{provider}:{model_name}"
        if provider == 'google_genai':
            return init_chat_model(context, api_key=api_key)
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

# if __name__ == "__main__":
#     model_loader = ModelLoader()
#     model = model_loader.load_model()
#     print(model.invoke("Hello, how are you?"))