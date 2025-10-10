import pandas as pd
'''df=pd.read_excel("chocolates.xlsx")
df["full name"]=df["NAMES"]+" "+df["CHOCOLATE"]
print(df)

df["DISCOUNT"]=(df["RATES"]/100)*20
print(df)
'''
data={"months":["january","feburary","march","april"]}
a=pd.DataFrame(data)

def extract(value):
    return value[0:3]
a["short_months"]=a["months"].map(extract)
print(a)