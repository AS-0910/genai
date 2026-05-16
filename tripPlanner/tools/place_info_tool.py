import os
from utils.place_info_search import TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        self.tavily_search = TavilyPlaceSearchTool()
        self.tools_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                if tavily_result:
                    return f"Following are the attractions of {place} as : {tavily_result}"
            except Exception as e:
                return f"Cannot find the details due to {e}."
                
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                if tavily_result:
                    return f"Following are the restaurants of {place} as : {tavily_result}"
            except Exception as e:
                return f"Cannot find the details due to {e}."

        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                if tavily_result:
                    return f"Following are the activities in and around {place} as : {tavily_result}"
            except Exception as e:
                return f"Cannot find the details due to {e}."
               
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                if tavily_result:
                    return f"Following are the modes of transportation available in {place} as : {tavily_result}"
            except Exception as e:
                return f"Cannot find the details due to {e}."
            
        return [search_attractions, search_restaurants, search_activities, search_transportation]