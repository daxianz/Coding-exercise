import pandas as pd
df =pd.read_excel('mrbooks.xls')
df1=df[['买家会员名']].head()
list1=df1['买家会员名'].values.tolist()
for s in list1:
    print(s)
