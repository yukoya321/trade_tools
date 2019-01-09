import json
import requests
import urllib.parse

class Pricing(object):

    def __init__(self, Account):
        self.rest_url = Account.api_url  + "/v3/accounts/" + Account.account_id + "/pricing"
        self.api_stream_url = Account.api_stream_url + "/v3/accounts/" + Account.account_id + "/pricing/stream"
        self.auth_key = Account.auth_key

    def get_price(self, *currencies):
        headers={
            "Content-Type": "application/json",
            "Authorization": self.auth_key
        }
        instruments_code = ",".join(currencies)
        params = {"instruments": instruments_code}
        prices_json = requests.get(self.rest_url, headers=headers, params=params)
        prices = json.loads(prices_json.text)
        return prices

    def streaming(self, *currencies):
        headers={
            "Authorization": self.auth_key
        }
        instruments_code = ",".join(currencies)
        params = {"instruments": instruments_code}
        prices = requests.get(self.api_stream_url, headers=headers, params=params, stream=True)
        for line in prices.iter_lines():
            if line:
                print(json.loads(line))
