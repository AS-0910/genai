import requests
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

class CurrencyConverter:
    def __init__(self):
        logger.debug("Initializing CurrencyConverter")
        load_dotenv()
        api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        if not api_key:
            logger.warning("EXCHANGE_RATE_API_KEY environment variable not set")
        else:
            logger.debug("EXCHANGE_RATE_API_KEY loaded")
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
        logger.debug("CurrencyConverter initialized")

    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert the amount from one currency to another"""
        logger.debug(f"convert_currency called: {amount} {from_currency} to {to_currency}")
        url = f"{self.base_url}/{from_currency}"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                logger.error(f"Currency conversion API returned status code {response.status_code}")
                raise Exception("API call failed:", response.json())
            rates = response.json()["conversion_rates"]
            logger.debug(f"Exchange rates retrieved for {from_currency}")
            if to_currency not in rates:
                logger.error(f"Currency {to_currency} not found in exchange rates")
                raise ValueError(f"{to_currency} not found in exchange rates.")
            result = amount * rates[to_currency]
            logger.debug(f"Conversion result: {amount} {from_currency} = {result} {to_currency}")
            return result
        except Exception as e:
            logger.error(f"Error during currency conversion: {str(e)}", exc_info=True)
            raise



# if __name__ == "__main__":
#     converter = CurrencyConverter()
#     result = converter.convert_currency(100, "USD", "EUR")
#     print(f"100 USD = {result} EUR")