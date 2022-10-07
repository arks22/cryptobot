from binance.spot import Spot 
from binance.lib.utils import get_timestamp

import datetime
import time

def main():
    #import api keys
    f = open('binance_keys.txt', 'r')
    keys = f.readlines()
    api_key = keys[0].rstrip('\n')
    api_secret = keys[1].rstrip('\n')
    client = Spot(key=api_key, secret=api_secret)
    account(client)


def get_trades():
    startTime = int(datetime.datetime(2022,1,1,12,0,0).timestamp() * 1000)
    endTime   = int(datetime.datetime(2022,1,1,12,16,0).timestamp() * 1000)

    hour = client.klines("BNBUSDT", "5m", limit=1, startTime=startTime, endTime=endTime)


def account(client):
    account_balances  = client.account()['balances']
    btc_balance = list(filter(lambda s : s['asset'] == 'BTC', account_balances))[0]
    eth_balance = list(filter(lambda s : s['asset'] == 'ETH', account_balances))[0]
    print(btc_balance)
    print(eth_balance)


def order():
    params = {
        'symbol': 'BTCBUSD',
        'side': 'SELL',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 0.002,
        'price': 9500
    }

    response = client.new_order(**params)
    print(response)


if __name__ == "__main__":
    main()
