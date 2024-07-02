import pandas as pd
df = pd.read_csv("Inputs/data/raw_data/BrentOilPrices.csv")
data_understanding =df.head(100)
print(data_understanding)

print("Number of null counts",df.isnull().count())