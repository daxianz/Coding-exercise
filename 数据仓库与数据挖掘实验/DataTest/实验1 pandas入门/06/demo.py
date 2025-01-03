import pandas as pd
s1=pd.Series([88,60,75],index=['明日同学','高同学','七月流火'])
print(s1['明日同学':'七月流火'])  #通过切片获取索引值
