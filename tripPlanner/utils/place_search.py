import os
import json
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

class GooglePlaceSearchTool:
    def __init__(self):
        logger.debug("Initializing GooglePlaceSearchTool")
        load_dotenv()
        api_key = os.getenv("GPLACES_API_KEY")
        if not api_key:
            logger.warning("GPLACES_API_KEY environment variable not set")
        else:
            logger.debug("GPLACES_API_KEY loaded")
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
        logger.debug("GooglePlaceSearchTool initialized")
    
    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using GooglePlaces API.
        """
        logger.debug(f"google_search_attractions called for place: {place}")
        result = self.places_tool.run(f"top attractive places in and around {place}")
        logger.debug(f"google_search_attractions API call completed for {place}")
        return result
    
    def google_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using GooglePlaces API.
        """
        logger.debug(f"google_search_restaurants called for place: {place}")
        result = self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
        logger.debug(f"google_search_restaurants API call completed for {place}")
        return result
    
    def google_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.
        """
        logger.debug(f"google_search_activity called for place: {place}")
        result = self.places_tool.run(f"Activities in and around {place}")
        logger.debug(f"google_search_activity API call completed for {place}")
        return result

    def google_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using GooglePlaces API.
        """
        logger.debug(f"google_search_transportation called for place: {place}")
        result = self.places_tool.run(f"What are the different modes of transportations available in {place}")
        logger.debug(f"google_search_transportation API call completed for {place}")
        return result)

