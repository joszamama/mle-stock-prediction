from autots import AutoTS
import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("datasets/AAPL (2021-2022).csv")

model = AutoTS(forecast_length=5, frequency='infer', ensemble='simple')
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)

prediction = model.predict()
forecast = prediction.forecast
print(forecast)