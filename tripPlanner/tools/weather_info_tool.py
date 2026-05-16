import os
from utils.weather_info import WeatherInfo
from langchain.tools import tool
from typing import List
import logging

logger = logging.getLogger(__name__)

class WeatherInfoTool:
    def __init__(self):
        logger.debug("Initializing WeatherInfoTool")
        self.weather_service = WeatherInfo()
        self.weather_tool_list = self._setup_tools()
        logger.debug(f"WeatherInfoTool initialized with {len(self.weather_tool_list)} tools")
    
    def _setup_tools(self) -> List:
        """Setup all tools for the weather forecast tool"""
        logger.debug("Setting up weather tools...")
        @tool
        def get_current_weather(city: str) -> str:
            """Get current weather for a city"""
            logger.debug(f"get_current_weather called for city: {city}")
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main', {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                logger.debug(f"Weather data retrieved for {city}: {temp}°C, {desc}")
                return f"Current weather in {city}: {temp}°C, {desc}"
            logger.warning(f"Could not fetch weather for {city}")
            return f"Could not fetch weather for {city}"
        
        @tool
        def get_weather_forecast(city: str) -> str:
            """Get weather forecast for a city"""
            logger.debug(f"get_weather_forecast called for city: {city}")
            forecast_data = self.weather_service.get_forecast_weather(city)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp} degree celcius , {desc}")
                logger.debug(f"Weather forecast retrieved for {city} with {len(forecast_summary)} days")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            logger.warning(f"Could not fetch forecast for {city}")
            return f"Could not fetch forecast for {city}"
    
        return [get_current_weather, get_weather_forecast]