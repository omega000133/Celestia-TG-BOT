import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "")
BASE_URL_API = os.getenv("BASE_URL_API", "")
BASE_URL_RPC = os.getenv("BASE_URL_RPC", "")
DEBUG = os.getenv("DEBUG", False)
PORCENTAJE = os.getenv("PORCENTAJE", False)
MIN_FREE_SPACE = os.getenv(
    "MIN_FREE_SPACE", 2
)  # Define the percentage or minimum fixed value of free space required in GB
VALOPER_ADDRESS = os.getenv("VALOPER_ADDRESS", "")  # address of validator
