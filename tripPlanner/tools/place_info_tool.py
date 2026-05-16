import os
from utils.place_info_search import TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

class PlaceSearchTool:
    def __init__(self):
        logger.debug("Initializing PlaceSearchTool")
        self.tavily_search = TavilyPlaceSearchTool()
        self.tools_list = self._setup_tools()
        logger.debug(f"PlaceSearchTool initialized with {len(self.tools_list)} tools")

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        logger.debug("Setting up place search tools...")
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            logger.debug(f"search_attractions called for place: {place}")
            try:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                if tavily_result:
                    logger.debug(f"Attractions found for {place}")
                    return f"Following are the attractions of {place} as : {tavily_result}"
            except Exception as e:
                logger.error(f"Error searching attractions for {place}: {str(e)}", exc_info=True)
                return f"Cannot find the details due to {e}."
                
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            logger.debug(f"search_restaurants called for place: {place}")
            try:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                if tavily_result:
                    logger.debug(f"Restaurants found for {place}")
                    return f"Following are the restaurants of {place} as : {tavily_result}"
            except Exception as e:
                logger.error(f"Error searching restaurants for {place}: {str(e)}", exc_info=True)
                return f"Cannot find the details due to {e}."

        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            logger.debug(f"search_activities called for place: {place}")
            try:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                if tavily_result:
                    logger.debug(f"Activities found for {place}")
                    return f"Following are the activities in and around {place} as : {tavily_result}"
            except Exception as e:
                logger.error(f"Error searching activities for {place}: {str(e)}", exc_info=True)
                return f"Cannot find the details due to {e}."
               
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            logger.debug(f"search_transportation called for place: {place}")
            try:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                if tavily_result:
                    return f"Following are the modes of transportation available in {place} as : {tavily_result}"
            except Exception as e:
                return f"Cannot find the details due to {e}."
            
        return [search_attractions, search_restaurants, search_activities, search_transportation]