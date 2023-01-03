import numpy as np
import pandas as pd 
a1=np.array([10, 23, 34, 54, 657 ])
a2=np.array([45, 23, 432, 75, 98])
a3=np.array(['jan', 'feb', 'mar', 'apr', 'may'])
df=pd.DataFrame([a1, a2, a3], columns=['a', 'b', 'c', 'd', 'e'])
print(df)
df["f"]=[1, 2, 3]
print(df)
df.loc[3]=["i", 'am', 'the', 'best', 'ever', 'made']
df=df.drop(2, axis=0)
df=df.drop("a", axis=1)
print(df)
df=df.rename({3:"raghuvar"}, axis=0)
df=df.rename({"e":"eeeee"}, axis=1)
print(df)
import pandas as pd
Name=['Manpreet','Kavil','Manu','Ria']
Phy=[70,60,76,89]
Chem=[30,70,50,65]
df2=pd.DataFrame([Name,Phy,Chem],columns=['Name',"Phy","Chem","Total"])
print(df2)
 
