#Loading the library
import pandas as pd
import numpy as np
df=pd.read_csv('D:\Zomato\zomato.csv')
print(df)
#Checking the first 10 values
print(df.head(10))
print(df.info())
print(df.shape)
print(df.isna().sum())