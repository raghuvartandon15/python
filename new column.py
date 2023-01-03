import numpy as np
import pandas as pd 
a1=np.array([10, 23, 34, 54, 657 ])
a2=np.array([45, 23, 432, 75, 98])
a3=np.array(['jan', 'feb', 'mar', 'apr', 'may'])
df=pd.DataFrame([a1, a2, a3], columns=['a', 'b', 'c', 'd', 'e'])
print(df)
df["f"]=[1, 2, 3]
print(df)
