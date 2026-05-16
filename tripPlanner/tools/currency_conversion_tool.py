from utils.currency_conversion import CurrencyConverter
from langchain.tools import tool
from typing import List


class CurrencyConversionTool:
    def __init__(self):
        self.converter = CurrencyConverter()
        self.tools_list= self.__setup_tools()
    
    def __setup_tools(self) -> List:
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
            """Convert the amount from one currency to another"""
            return self.converter.convert_currency(amount, from_currency, to_currency)
        
        return [convert_currency]