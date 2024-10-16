import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('hbar.csv')

# Ensure the data is sorted from the least recent to the most recent
df = df.sort_index(ascending=True)

# Calculate the 30, 60, and 90-day volatility
def normalized_volatility(prices, window):
    prices = pd.DataFrame({'Prices': prices[:,0]})

    log_returns = np.log(prices / prices.shift(1))
    volatility = log_returns.rolling(window=window).std()
    return volatility.iloc[-1]  # Get the most recent value corresponding to the latest window

def parkinson_volatility_mean(prices, window=360):
    # Ensure the array has the correct shape and convert to 1D array
    if prices.ndim != 2 or prices.shape[1] != 1:
        raise ValueError("The input array must have dimensions (365, 1)")
    
    # Remove the second dimension to obtain a one-dimensional array
    prices = prices.flatten()
    
    # Convert the numpy array to a pandas Series to use the rolling function
    prices_series = pd.Series(prices)
    
    # Calculate the daily highs and lows over a 1-day window
    high = prices_series.rolling(window=window, min_periods=1).max()
    low = prices_series.rolling(window=window, min_periods=1).min()
    #print(high, low)
    
    # Calculate the logarithm of highs and lows
    log_hl = np.log(high / low)
    
    # Compute Parkinson’s volatility factor
    parkinson_vol = (log_hl ** 2).rolling(window=window).mean() * (1 / (4 * np.log(2)))
    
    # Take the square root to obtain the standard deviation
    parkinson_vol = np.sqrt(parkinson_vol)
    
    # Calculate the mean volatility value
    parkinson_vol_mean = parkinson_vol.mean()
    
    return parkinson_vol_mean
