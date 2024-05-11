import pandas as pd


df = pd.read_excel("./csv/depositos.xlsx")

df.to_json("./output.json", orient="records")
