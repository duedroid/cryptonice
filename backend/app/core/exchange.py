from binance import Client
from binance.exceptions import BinanceAPIException


class Exchange:
    def __init__(self, api_key, api_secret):
        self.binance_client = Client(api_key=api_key, api_secret=api_secret)
    
    def get_balance(self):
        return self.binance_client.get_account()
    
    def check_auth(self):
        try:
            return bool(self.binance_client.get_account_status())
        except BinanceAPIException as e:
            return False