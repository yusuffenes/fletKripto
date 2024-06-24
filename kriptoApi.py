import requests

def get_crypto_price(symbol):
    params={
        'symbol': symbol
    }
    rp = requests.get('https://api.binance.com/api/v3/ticker/price?', params=params)
    return float(rp.json()['price'])


def get_crypto_info(symbol):
    params={
        'symbol': symbol
    }
    rp = requests.get('https://api.binance.com/api/v3/ticker/24hr?', params=params)
    return rp.json()

def get_coin_names():
    rp = requests.get('https://api.binance.com/api/v3/ticker/price')
    name = rp.json()
    for i in range(len(name)):
        name[i] = name[i]['symbol']
    return name
    