import pandas as pd
data=pd.read_csv("CollegePlacement.csv")
gp=data.groupby(["Prev_Sem_Result","Academic_Performance"]).agg({"Extra_Curricular_Score":"max"})
print(gp) 