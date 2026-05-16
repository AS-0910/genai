import yaml
import os
import logging

logger = logging.getLogger(__name__)

class ConfigLoader:
    def __init__(self):
        logger.debug("Initializing ConfigLoader")
        self.config = self.load_config()
        logger.debug("Configuration loaded in __init__")

    def get_config(self):
        logger.debug("get_config called")
        return self.config
    
    def load_config(self, config_path : str = "config/config.yaml") -> dict:
        logger.debug(f"Loading configuration from {config_path}")
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
            logger.info(f"Configuration loaded successfully from {config_path}")
            return config
        except Exception as e:
            logger.error(f"Failed to load configuration from {config_path}: {str(e)}", exc_info=True)
            raise
    

# if __name__ == "__main__":
#     config_loader = ConfigLoader()
#     config = config_loader.get_config()
#     print(config)

