import json
import requests
from config import value


class ConvertionExeption(Exception):
    pass


class CryptoConverter():
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        try:
            quote_ticket = value[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту: {quote}')

        try:
            base_ticket = value[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать колличество: {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticket}&tsyms={base_ticket}')
        total_base = json.loads(r.content)[value[base]]
        total_base *= float(amount)
        return total_base
