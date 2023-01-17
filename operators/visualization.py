import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("datasets/AAPL (2021-2022).csv")

figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"], high=data["High"], low=data["Low"], close=data["Close"])])
figure.update_layout(title = "Apple Stock Price Analysis (2021-2022)", xaxis_rangeslider_visible=False)
figure.show()

# Analizar cuantas veces Close es mayor que Open
print("Close is greater than Open", len(data[data["Close"] > data["Open"]]), "times")

# Analizar cuantas veces Close es menor que Open
print("Close is less than Open", len(data[data["Close"] < data["Open"]]), "times")

# Analizar cuantas veces Close es igual que Open
print("Close is equal to Open", len(data[data["Close"] == data["Open"]]), "times")

# Buscar mejor momento para invertir en las acciones de Apple
print("Best time to invest in Apple stock is", data.iloc[data["Close"].idxmin()]["Date"])