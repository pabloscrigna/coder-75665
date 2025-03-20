"""
Los archivos CSV (Comma-Separated Values) son uno de los formatos más
comunes para almacenar datos tabulares. Pandas facilita la
lectura de estos archivos mediante la función pd.read_csv().
Esta función es muy flexible y permite manejar archivos con
delimitadores distintos a la coma,
manejar encabezados, y gestionar datos faltantes.
"""

import pandas as pd

file_name = "./samples/compras-contrataciones-acumar-2024.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(file_name)

# Mostrar las primeras filas del DataFrame
print(df.head())