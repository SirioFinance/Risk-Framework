import requests as req
import time
from datetime import datetime
import numpy as np
from MetricsAnalyzer import *
import pandas as pd

def get_token_historical_price(t, token_id):
    historicalPrice = np.array([])
    
    to_timestamp = int(time.time()) - 86400
    from_timestamp = to_timestamp - 31622400

    if t == 'whbar':
        r = req.get('https://api.binance.com/api/v3/klines?symbol=HBARUSDT&interval=1d&limit=365')

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
    
    volatility_ltv = parkinson_volatility_mean(prices, 365)
    print(t)
    print(volatility_ltv)

