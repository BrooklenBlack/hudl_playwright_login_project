import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("HUDL_BASE_URL")
HUDL_EMAIL = os.getenv("HUDL_EMAIL")
HUDL_PASSWORD = os.getenv("HUDL_PASSWORD")