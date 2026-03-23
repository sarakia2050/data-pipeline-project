import requests
import json
from datetime import datetime


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_last_updated_at": "true"
    }

    response = requests.get(url, params=params)
    data = response.json()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"data/raw/crypto_raw_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Raw data saved to {filename}")


if name == "__main__":
    fetch_crypto_data()
