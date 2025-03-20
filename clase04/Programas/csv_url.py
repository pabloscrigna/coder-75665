import pandas as pd

url = "https://raw.githubusercontent.com/"
url = f"{url}jbrownlee/Datasets/master/pima-indians-diabetes.csv"

df = pd.read_csv(url, sep=',', header=None)
print(f"shape: {df.shape}")
print(df.head())
