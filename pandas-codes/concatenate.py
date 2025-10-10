import pandas as pd
dict={"fruits":["apple","banana","orange","pineapple"],
    "cost":[100,120,200,230,],"quantity":[2,3,8,9]}
df=pd.DataFrame(dict)
print(df)

df1=df.copy()
df1.loc[0:"cost"]=190
df1.loc[1:"cost"]=110
df1.loc[2:"cost"]=140
df1.loc[0:"quantity"]=1
df1.loc[1:"quantity"]=19
df1.loc[2:"quantity"]=10
#print(df1)

#print(df.compare(df1))
#print(df.compare(df1,keep_shape=True))
print(df.pivot(index="fruits",columns="quantity",values="cost"))