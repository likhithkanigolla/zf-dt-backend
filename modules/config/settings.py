import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
DATABASE_URL = os.getenv("DEMO_TEXT")
