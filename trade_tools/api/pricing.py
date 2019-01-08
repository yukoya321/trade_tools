import json
import requests
import urllib.parse

class Pricing(object):

    def __init__(self, Account):
        self.api_url = Account.api_url
        self.api_key = Account.api_key
        self.account_id = Account.account_id
        self.auth_key = "Bearer " + self.api_key

    def get_price(self, *currencies):
        url = self.api_url + "/v3/accounts/" + self.account_id + "/pricing"
        result = self.pricing_request(url, *currencies)
        return result

    def get_stream(self, *currencies):
        url = self.api_url + "/v3/accounts/" + self.account_id + "/pricing/stream"
        result = self.pricing_request(url, *currencies)
        return result

    def pricing_request(self, url, *currencies):
        headers={
            "Content-Type": "application/json",
            "Authorization": self.auth_key
        }
        instruments_code = ",".join(currencies)
        params = {"instruments": instruments_code}
        prices_json = requests.get(url, headers=headers, params=params)
        prices = json.loads(prices_json.text)
        return prices
