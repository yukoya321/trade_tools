import json
import requests

class Candle(object):

    def __init__(self, Account, instrument):
        self.rest_url = Account.api_url  + "/v3/instruments/" + instrument + "/candles"
        self.auth_key = Account.auth_key
    
    def get_candles(self, params={}):
        headers={
            "Authorization": self.auth_key
        }
        prices = requests.get(self.rest_url, headers=headers, params=params)
        return prices.text