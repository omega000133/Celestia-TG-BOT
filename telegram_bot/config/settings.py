import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN", "")
BASE_URL_API = os.getenv("BASE_URL_API", "")
BASE_URL_RPC = os.getenv("BASE_URL_RPC", "")
DEBUG = os.getenv("DEBUG", False)
PORCENTAJE = os.getenv("PORCENTAJE", False)
MIN_FREE_SPACE = os.getenv(
    "MIN_FREE_SPACE", 2
)  # Define the percentage or minimum fixed value of free space required in GB
VALOPER_ADDRESS = os.getenv(
    "VALOPER_ADDRESS", "celestiavaloper14v4ush42xewyeuuldf6jtdz0a7pxg5fwrlumwf"
)  # address of validator
MISSED_BLOCK_NUMBER = os.getenv("MISSED_BLOCK_NUMBER", 5)  # address of validator
BASE_RPC_URL = os.getenv("BASE_RPC_URL", "https://rpc-celestia-1.latamnodes.org")
