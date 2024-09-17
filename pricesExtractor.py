import requests as req
import time
from datetime import datetime
import numpy as np
from MetricsAnalyzer import calculate_volatility
import pandas as pd

def get_token_historical_price(t, token_id):
    historicalPrice = np.array([])
    
    to_timestamp = int(time.time()) - 86400
    from_timestamp = to_timestamp - 15638400

    if t == 'whbar':
        r = req.get('https://api.binance.com/api/v3/klines?symbol=HBARUSDT&interval=1d&limit=181')

        for r in r.json():
            historicalPrice = np.append(historicalPrice, [float(r[1])])

    else:
        r = req.get('https://api.saucerswap.finance/tokens/prices/usd/'+token_id+'?from='+str(from_timestamp)+'&to='+str(to_timestamp)+'&interval=DAY')

        for r in r.json():
            historicalPrice = np.append(historicalPrice, [float(r['usdPrice'])])

    return historicalPrice.reshape(-1,1)


tokens = {
    'whbar': '0.0.1456986',
    'hbarx': '0.0.834116',
    'usdc': '0.0.456858',
    'sauce': '0.0.731861',
    'xsauce': '0.0.1460200',
    'hst': '0.0.968069',
    'hbarsuite': '0.0.786931'
    }

for t in tokens:
    prices = get_token_historical_price(t, tokens[t])
    
    volatility_30d = calculate_volatility(prices, 30)
    volatility_60d = calculate_volatility(prices, 90)
    volatility_180d = calculate_volatility(prices, 180)

    print(t)
    print(f"Volatilità a 30 giorni: {volatility_30d}")
    print(f"Volatilità a 60 giorni: {volatility_60d}")
    print(f"Volatilità a 180 giorni: {volatility_180d}")
    print('\n\n')
