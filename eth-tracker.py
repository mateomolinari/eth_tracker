import requests
import json
import time
from datetime import datetime


headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': 'fc1f90b5-782c-4f3e-b3fd-f4831190fe00',}
ETH_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
IFTTT_WEBHOOK = "https://maker.ifttt.com/trigger/ethprice/with/key/m78XbHthdIy-PhG8D-DUb1lgKvx3VPwcj9FVdlvU86F"
ETH_PRICE_TRESHOLD = 2200

def check_price():
    response = requests.get(ETH_API_URL, headers=headers)
    response_json = response.json()
    return(response_json["data"][1]["quote"]["USD"]["price"])


def post_ifttt_webhook(event, value):
    data = {"value1" : value}
    print(requests.post(event, json=data))

def main ():
    while True:
        price = check_price()
        if price < ETH_PRICE_TRESHOLD:
            post_ifttt_webhook(IFTTT_WEBHOOK, round(price))

        time.sleep(5 * 60)



if __name__ == "__main__":
    main()