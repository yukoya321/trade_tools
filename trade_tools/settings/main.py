from dotenv import load_dotenv
import os
load_dotenv()

API_REST_URL = os.getenv("API_REST_URL")
API_STREAM_URL = os.getenv("API_STREAM_URL")
API_KEY = os.getenv("API_KEY")