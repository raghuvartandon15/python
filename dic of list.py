import numpy as np
import pandas as pd 
data={"jan":[50, 60, 70],"feb":[10, 20, 30], "march":[1, 3, 4]} 
df=pd.DataFrame(data)
print(df)
print(df.T)
