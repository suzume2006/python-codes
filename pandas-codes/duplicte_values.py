import pandas as pd
data=pd.read_excel("student info1.xlsx")
#print(data)
#print(data.isnull().sum())#total number of null cell in each row
print(data.dropna())
#print(data["salary"].mean())
#print(data.fillna(method="bfill"))#below values get filled in the null place
#print(data.fillna(method="ffill"))#above values get filled in the null place
