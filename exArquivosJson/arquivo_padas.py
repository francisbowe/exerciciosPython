import pandas as pd

pd.__version__

arquivo = "economic-indicators.csv"
df = pd.read_csv(arquivo)
df.head()
print (df.head())