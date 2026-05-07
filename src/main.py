import pandas as pd

df = pd.read_parquet("src/data/silver/transacional/goalscorers.parquet")
print("================ Dados Processados =================")
print(df.head())
print("")
print("================ Tipos de Dados =================")
print(df.dtypes)