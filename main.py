#!usr/bin/env python3
# encoding: utf-8

import requests
import json

API_KEY = "API-KEY HERE"
GAINERS_LOSERS_ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/gainers-losers"
LATEST_COINS_ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/latest"
MOST_VISITED_ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/most-visited"

parameters = {}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}


def main():
    gainers_losers_list = requests.get(MOST_VISITED_ENDPOINT, headers=headers)
    print(gainers_losers_list.json())


if __name__ == '__main__':
    main()
