import requests
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

class WeatherInfo:
    def __init__(self):
        logger.debug("Initializing WeatherInfo")
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            logger.warning("OPENWEATHER_API_KEY environment variable not set")
        else:
            logger.debug("OPENWEATHER_API_KEY loaded")
        self.base_url = "https://api.openweathermap.org/data/2.5"
        logger.debug(f"WeatherInfo initialized with base_url: {self.base_url}")

    
    def get_current_weather(self, place:str):
        """Get current weather of a place"""
        logger.debug(f"get_current_weather called for place: {place}")
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key,
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                logger.debug(f"Current weather API call successful for {place}")
                return response.json()
            else:
                logger.warning(f"Current weather API returned status code {response.status_code} for {place}")
                return {}
        except Exception as e:
            logger.error(f"Error fetching current weather for {place}: {str(e)}", exc_info=True)
            raise e
    
    def get_forecast_weather(self, place:str):
        """Get weather forecast of a place"""
        logger.debug(f"get_forecast_weather called for place: {place}")
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": place,
                "appid": self.api_key,
                "cnt": 10,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                logger.debug(f"Forecast weather API call successful for {place}")
                return response.json()
            else:
                logger.warning(f"Forecast weather API returned status code {response.status_code} for {place}")
                return {}
        except Exception as e:
            logger.error(f"Error fetching forecast weather for {place}: {str(e)}", exc_info=True)
            raise e


# if __name__ == "__main__":
#     weatherInfo = WeatherInfo()
#     print(weatherInfo.get_current_weather("Bangalore"))



        