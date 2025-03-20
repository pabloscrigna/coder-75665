"""
Pandas también soporta la lectura de archivos Excel, que son ampliamente utilizados para 
almacenar y compartir datos en un formato de hoja de cálculo. La función pd.read_excel() 
permite leer datos desde archivos Excel, y es posible especificar la hoja de la 
cual se quiere extraer los datos.
"""

import pandas as pd

filename = 'Financial Sample.xlsx'
path = "./samples"
sheet = 'Sheet1'

file = f"{path}/{filename}"

df = pd.read_excel(file, sheet_name=sheet)

print(df.head())
