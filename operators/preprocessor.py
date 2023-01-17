import pandas as pd

# Cargar el dataset
df = pd.read_csv("datasets/AAPL (2021-2022).csv")

# Transformación de variables, convertir las fechas a un formato estandarizado y establecer la columna de fecha como el índice del DataFrame
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Cambio porcentual diario
df['daily_change'] = df['Close'].pct_change()

# Promedio móvil de 30 días
df['30d_ma'] = df['Close'].rolling(window=30).mean()

# Volatilidad de 30 días
df['30d_volatility'] = df['Close'].rolling(window=30).std()

# Rango del día (high-low)
df['daily_range'] = df['High'] - df['Low']

# Relación precio-ganancias
df['P/E'] = df['Close'] / df['Adj Close']

# Volumen promedio de 30 días
df['30d_avg_volume'] = df['Volume'].rolling(window=30).mean()

# Guardar el dataset
df.to_csv("datasets/AAPL (2021-2022) - Transformed.csv")
