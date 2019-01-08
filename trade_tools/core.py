import settings
from api.account import Account
from api.pricing import Pricing

API_URL = settings.main.API_URL
API_KEY = settings.main.API_KEY

account = Account(API_URL, API_KEY)

pricing = Pricing(account)
prices = pricing.get_price(*["EUR_USD", "USD_CAD"])

print(prices)