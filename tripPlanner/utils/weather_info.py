import requests
from dotenv import load_dotenv
import os

class WeatherInfo:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        # print(f"OpenWeather API Key: {self.api_key}")
        self.base_url = "https://api.openweathermap.org/data/2.5"

    
    def get_current_weather(self, place:str):
        """Get current weather of a place"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key,
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e
    
    def get_forecast_weather(self, place:str):
        """Get weather forecast of a place"""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": place,
                "appid": self.api_key,
                "cnt": 10,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e


# if __name__ == "__main__":
#     weatherInfo = WeatherInfo()
#     print(weatherInfo.get_current_weather("Bangalore"))



        