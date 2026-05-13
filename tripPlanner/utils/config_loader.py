import yaml
import os

class ConfigLoader:
    def __init__(self):
        self.config = self.load_config()

    def get_config(self):
        return self.config
    
    def load_config(self, config_path : str = "config/config.yaml") -> dict:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    

# if __name__ == "__main__":
#     config_loader = ConfigLoader()
#     config = config_loader.get_config()
#     print(config)

