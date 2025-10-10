import pandas as pd
data=pd.read_csv("CollegePlacement.csv")
#print(data)
print(data.head(13))#for starting 13 values
print(data.tail(10))#for ending 10 values
print(data.isnull())
