import pandas as pd

df = pd.read_csv ("F:\AmazonBot\Links.csv")
print(df["ProductName"][1])