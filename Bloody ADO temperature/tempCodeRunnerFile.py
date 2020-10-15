from fillupscript import UpdateTempBackLog


import pandas as pd
df = pd.read_csv(r'D:\LouisPersonalProjects\Bloody ADO temperature\History.csv',encoding='utf8') 
print(len(df))
#print(df.loc[len(df)-1])
#print(len(df))
#print(df.loc[124,"IfNil"])
###