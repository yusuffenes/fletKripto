import requests

def get_crypto_price(symbol):
    params={
        'symbol': symbol
    }
    rq = requests.get('https://api.binance.com/api/v3/ticker/price?', params=params)
    return float(rq.json()['price'])


def get_crypto_info(symbol):
    params={
        'symbol': symbol
    }
    rq = requests.get('https://api.binance.com/api/v3/ticker/24hr?', params=params)
    return rq.json()

def get_coin_names():
    rp = requests.get('https://api.binance.com/api/v3/ticker/price')
    name = rp.json()
    for i in range(len(name)):
        name[i] = name[i]['symbol']
    return name
    