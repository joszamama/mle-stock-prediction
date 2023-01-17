import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("datasets/AAPL (2021-2022).csv")

# Transformación de variables, convertir las fechas a un formato estandarizado y establecer la columna de fecha como el índice del DataFrame
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns='High'), df['High'], test_size=0.2)

# entrenar el modelo
rf = RandomForestRegressor()
rf.fit(X_train, y_train)

# calcular la importancia de las variables
importances = rf.feature_importances_

# mostrar las variables en orden de importancia
important_features = pd.Series(importances, index=X_train.columns)
important_features.sort_values(ascending=False)

# obtener las variables en orden de importancia
important_features = important_features.sort_values(ascending=False)

# crear el gráfico de barras
plt.barh(y=important_features.index, width=important_features.values)
plt.xlabel('Importancia')
plt.ylabel('Variables')
plt.show()