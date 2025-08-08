import pandas

db = pandas.read_csv("CH_Nationality_List_20171130_v1.csv")
db = db["Nationality"].tolist()