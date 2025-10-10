import pandas as pd
data=pd.read_csv("kpop_group_debut_astrology.csv")
print(data["group_name"].duplicated().sum())#number of duplicates in list
print(data.drop_duplicates("group_name"))