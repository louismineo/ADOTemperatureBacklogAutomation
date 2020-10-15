# reading cs
from fillupscript import UpdateTempBackLog


import pandas as pd
df = pd.read_csv(r'D:\LouisPersonalProjects\Bloody ADO temperature\History1.csv',encoding='utf8') 
print(len(str(df.loc[0,"Date"])))
print(df.loc[0,"Date"])
print("0"+str(df.loc[0,"Date"]))
#print(df.loc[len(df)-1])
#print(len(df))
#print(df.loc[124,"IfNil"])
###

for x in range (0,len(df)):
    if df.loc[x,"AM"] == "Nil":
        UpdateTempBackLog(df.loc[x,"Date"],"AM")
        print(str(df.loc[x,"Date"])+" AM Temperature updated")


    if df.loc[x,"PM"] == "Nil":
        UpdateTempBackLog(df.loc[x,"Date"],"PM")
        print(str(df.loc[x,"Date"])+" PM Temperature updated")