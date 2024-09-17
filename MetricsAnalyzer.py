import pandas as pd
import numpy as np

# Leggi il file CSV
df = pd.read_csv('hbar.csv')

# Assicurati che i dati siano ordinati dal meno recente al più recente
df = df.sort_index(ascending=True)

# Calcola la volatilità a 30, 60, 90 giorni
def calculate_volatility(prices, window):
    prices = pd.DataFrame({'Prices': prices[:,0]})

    log_returns = np.log(prices / prices.shift(1))
    volatility = log_returns.rolling(window=window).std()
    return volatility.iloc[-1]  # Ottieni l'ultimo valore, corrispondente alla finestra più recente


# Calcola i volumi medi giornalieri a 30, 60, 90 giorni
def calculate_volume(volumes):
    average_volume_30d = df['total_volume'].tail(30).mean()
    average_volume_60d = df['total_volume'].tail(60).mean()
    average_volume_90d = df['total_volume'].tail(90).mean()

