import pandas as pd
data={"names":["brutikaa","raj","kabir"],
    "salary":[1000000000,123445,223455],
    "subject":["maths","movie","lab"]}
df=pd.DataFrame(data)
print(df)
data=pd.read_csv("game_details.csv")
print(data)