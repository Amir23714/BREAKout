from binance.client import Client
from keys import secret_key, api_key
import numpy as np

client = Client(api_key, secret_key)
def answer(coin):
    if client.get_historical_klines(f"{coin}USDT", Client.KLINE_INTERVAL_1DAY, "1 day ago UTC") != []:
        befor_cost = float(client.get_ticker(symbol=f"{coin}USDT")['priceChangePercent'])
        now_cost = client.get_ticker(symbol=f"{coin}USDT")['lastPrice']
        if float(befor_cost) > 0:
            final_answer = f"{coin}:\t\t{round(float(now_cost), 2)}$\t\t ✅{round(befor_cost, 2)}"
        elif float(befor_cost) < 0:
            final_answer = f"{coin}:\t\t{round(float(now_cost), 2)}$\t\t 🔻{round(befor_cost, 2)}"
        else:
            final_answer = f"{coin}:\t\t{round(float(now_cost), 2)}$\t\t same as yesterday"
        return final_answer
    else:
        return f'For {coin}: no data'

