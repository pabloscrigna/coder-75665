"""
Los archivos de texto también pueden ser leídos con pd.read_csv() si están estructurados
en un formato tabular con un delimitador constante, como espacios o tabuladores.
Si el archivo no tiene una estructura fija, se puede procesar de forma personalizada.
"""

import pandas as pd

file_name = "Pokemon_data.txt"
path = "./samples"
file = f"{path}/{file_name}"

# Cargar el archivo de texto en un DataFrame
df = pd.read_csv(file, delimiter="\t")

# Mostrar las primeras filas del DataFrame
print(df.head())