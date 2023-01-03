import numpy as np
import pandas as pd 
#s1=pd.Series(['rax', 'is', 'the', 'best'])
#s2=pd.Series([10, 20, 30 , 40])
#s3=pd.Series([99, 88, 77, 66])
data={"s1":pd.Series(['rax', 'is', 'the', 'best'], index=[1, 2, 3, 4]), "s2":pd.Series([10, 20, 30 , 40], index=[9, 8, 7, 6]), "s3":pd.Series([99, 88, 77, 66], index=[5, 4, 3, 2])}
df=pd.DataFrame(data)
#print(df)
