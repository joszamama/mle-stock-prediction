from autots import AutoTS
import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("datasets/AAPL (2021-2022).csv")

print(data.corr())