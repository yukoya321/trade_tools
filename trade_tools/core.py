import settings
from api.account import Account
from api.pricing import Pricing
from api.candle import Candle


API_REST_URL = settings.main.API_REST_URL
API_STREAM_URL = settings.main.API_STREAM_URL
API_KEY = settings.main.API_KEY

account = Account(API_REST_URL, API_STREAM_URL, API_KEY)

pricing = Candle(account, "EUR_USD")
print(pricing.get_candles())
# pricing.streaming(["EUR_USD", "USD_CAD"])


# print(prices)