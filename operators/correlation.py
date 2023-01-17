from autots import AutoTS
import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("datasets/AAPL (2021-2022).csv")

# Análisis de la correlación del dataset, para el precio de las acciones de Apple (AAPL) en el intervalo de tiempo de 2021 a 2022
print(data.corr())

# Gráfico de correlación del dataset, para el precio de las acciones de Apple (AAPL) en el intervalo de tiempo de 2021 a 2022
fig = go.Figure(data=go.Heatmap(
                     z=data.corr(),
                        x=data.columns,
                        y=data.columns,
                        colorscale='Viridis'))
fig.update_layout(title='Correlación del dataset, para el precio de las acciones de Apple (AAPL) en el intervalo de tiempo de 2021 a 2022')
fig.show()

# Los valores de las variables Open, High, Low, Close, Adj Close, Volume están altamente correlacionadas entre sí, 
# ya que los valores de las correlaciones son muy cercanos a 1. Sin embargo, la variable Volume está inversamente 
# correlacionada con el resto de las variables. Esto significa que a medida que aumenta el valor de Volume, los 
# valores de las otras variables tienden a disminuir. También se puede observar que la correlación entre las variables 
# Open, High, Low, Close, Adj Close es muy similar, lo cual indica que estas variables están altamente relacionadas 
# entre sí.

# Teniendo en cuenta que el análisis de correlación se refiere al precio de las acciones de Apple este año, se puede 
# concluir que el precio de apertura (Open), el precio máximo (High), el precio mínimo (Low), el precio de cierre 
# (Close) y el precio de cierre ajustado (Adj Close) están altamente relacionados entre sí. Esto sugiere que el precio 
# de las acciones de Apple varía de manera similar en relación a estas variables. Sin embargo, el volumen negociado 
# de las acciones de Apple (Volume) está inversamente relacionado con el resto de las variables. Esto podría indicar 
# que cuando el volumen de negociación es alto, el precio de las acciones de Apple tiende a disminuir.