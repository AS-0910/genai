from utils.currency_conversion import CurrencyConverter
from langchain.tools import tool
from typing import List
import logging

logger = logging.getLogger(__name__)


class CurrencyConversionTool:
    def __init__(self):
        logger.debug("Initializing CurrencyConversionTool")
        self.converter = CurrencyConverter()
        self.tools_list= self.__setup_tools()
        logger.debug(f"CurrencyConversionTool initialized with {len(self.tools_list)} tools")
    
    def __setup_tools(self) -> List:
        logger.debug("Setting up currency conversion tools...")
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
            """Convert the amount from one currency to another"""
            logger.debug(f"convert_currency called: {amount} {from_currency} to {to_currency}")
            result = self.converter.convert_currency(amount, from_currency, to_currency)
            logger.debug(f"convert_currency result: {result} {to_currency}")
            return result
        
        return [convert_currency]