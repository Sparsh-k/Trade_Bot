from binance.client import Client
import os
from dotenv import load_dotenv
import time

load_dotenv()

#### Binance Connection Strings
def get_client():
    client = Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET"),
        testnet=True
    )

    # Sync time
    server_time = client.get_server_time()
    client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)

    return client