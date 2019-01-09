import requests
import json

class Account(object):

    def __init__(self, API_REST_URL, API_STREAM_URL, API_KEY):
        self.api_url = API_REST_URL
        self.api_stream_url = API_STREAM_URL
        self.api_key = API_KEY
        self.auth_key = "Bearer " + self.api_key
        self.authorize()

    def authorize(self):
        url = self.api_url + "/v3/accounts"
        headers = {
            'Authorization': self.auth_key
        }
        account_info = requests.get(url, headers=headers)
        account_info_json = json.loads(account_info.text)
        self.account_id = account_info_json["accounts"][0]["id"]

    def get_account_detail(self):
        url = self.api_url + "/v3/accounts/" + self.account_id
        headers={
            "Content-Type": "application/json",
            "Authorization": self.auth_key
        }
        account_detail = requests.get(url, headers=headers)
        account_detail_json = json.loads(account_detail.text)
        account = account_detail_json["account"]
        lastTransactionID = account_detail_json["lastTransactionID"]
        return account, lastTransactionID