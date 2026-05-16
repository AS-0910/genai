import requests
from dotenv import load_dotenv
import os

class CurrencyConverter:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert the amount from one currency to another"""
        url = f"{self.base_url}/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("API call failed:", response.json())
        rates = response.json()["conversion_rates"]
        if to_currency not in rates:
            raise ValueError(f"{to_currency} not found in exchange rates.")
        return amount * rates[to_currency]



# if __name__ == "__main__":
#     converter = CurrencyConverter()
#     result = converter.convert_currency(100, "USD", "EUR")
#     print(f"100 USD = {result} EUR")