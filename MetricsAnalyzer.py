import pandas as pd
import numpy as np

# Leggi il file CSV
df = pd.read_csv('hbar.csv')

# Assicurati che i dati siano ordinati dal meno recente al più recente
df = df.sort_index(ascending=True)

# Calcola la volatilità a 30, 60, 90 giorni
def normalized_volatility(prices, window):
    prices = pd.DataFrame({'Prices': prices[:,0]})

    log_returns = np.log(prices / prices.shift(1))
    volatility = log_returns.rolling(window=window).std()
    return volatility.iloc[-1]  # Ottieni l'ultimo valore, corrispondente alla finestra più recente

def parkinson_volatility_mean(prices, window=360):
    # Assicurati che l'array abbia dimensione corretta e converti in array 1D
    if prices.ndim != 2 or prices.shape[1] != 1:
        raise ValueError("L'array di input deve avere dimensioni (365, 1)")
    
    # Rimuovi la seconda dimensione per ottenere un array unidimensionale
    prices = prices.flatten()
    
    # Converti il numpy array in una pandas Series per poter usare la funzione rolling
    prices_series = pd.Series(prices)
    
    # Calcola i massimi e minimi giornalieri su una finestra di 1 giorno
    high = prices_series.rolling(window=window, min_periods=1).max()
    low = prices_series.rolling(window=window, min_periods=1).min()
    #print(high, low)
    
    # Calcola la logaritmica dei massimi e minimi
    log_hl = np.log(high / low)
    
    # Calcola il fattore di volatilità di Parkinson
    parkinson_vol = (log_hl ** 2).rolling(window=window).mean() * (1 / (4 * np.log(2)))
    
    # Prendi la radice quadrata per ottenere la deviazione standard
    parkinson_vol = np.sqrt(parkinson_vol)
    
    # Calcola la media dei valori di volatilità
    parkinson_vol_mean = parkinson_vol.mean()
    
    return parkinson_vol_mean
