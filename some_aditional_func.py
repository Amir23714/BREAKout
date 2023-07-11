from main import client
from binance.client import Client


# tickers = client.get_all_tickers()
# print(tickers)
# all_tickers = pd.DataFrame(tickers)
# only_usdt = all_tickers[all_tickers.symbol.str.contains('USDT')]
# only_usdt.set_index('symbol', inplace=True)
#
# for index, row in only_usdt.iterrows():
#     print(index, row[['symbol', 'price']])
# # pd['Price in past'] = client.get_historical_klines(str(pd['symbol']), Client.KLINE_INTERVAL_1DAY, "1 day ago UTC")[0][1]

#
# tickers = client.get_all_tickers()
# final = list()
# tickers = list(filter(lambda x: x['symbol'].endswith('USDT'), tickers))
# lst = []
# for item in tickers:
#     lst.append(item['symbol'])
# l2 = []
# for item in lst:
#     l2.append(item[:-4])
# # print(l2)

    #
# l = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'BCCUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT',
#      'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'VENUSDT', 'NULSUSDT', 'VETUSDT',
#      'PAXUSDT', 'BCHABCUSDT', 'BCHSVUSDT', 'USDCUSDT', 'LINKUSDT', 'WAVESUSDT', 'BTTUSDT', 'USDSUSDT', 'ONGUSDT',
#      'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT',
#      'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', 'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT',
#      'FTMUSDT']

# print(l2)
#
#
# # if (client.get_historical_klines(str(item['symbol']), Client.KLINE_INTERVAL_1DAY, "1 day ago UTC") != []):
# #     ls = item['symbol'], item['price'], \
# #     client.get_historical_klines(str(item['symbol']), Client.KLINE_INTERVAL_1DAY, "1 day ago UTC")[0][1]
# #     final.append(ls)

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

