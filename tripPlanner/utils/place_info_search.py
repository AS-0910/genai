import json
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

class TavilyPlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("TAVILY_API_KEY")

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearchResults(
            tmax_results=5,
            include_answer=True,
            tavily_api_key=self.api_key
        )
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearchResults(
            tmax_results=5,
            include_answer=True,
            tavily_api_key=self.api_key
        )
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearchResults(
            tmax_results=5,
            include_answer=True,
            tavily_api_key=self.api_key
        )
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearchResults(
            tmax_results=5,
            include_answer=True,
            tavily_api_key=self.api_key
        )
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
# if __name__ == "__main__":
#     place_search_tool = TavilyPlaceSearchTool()
#     print(place_search_tool.tavily_search_attractions("Bangalore"))
#     print(place_search_tool.tavily_search_restaurants("Bangalore"))