import pandas as pd
df = pd.read_excel('mrbooks.xls')
df1=df.groupby(["宝贝标题"])["宝贝总数量"].sum().head()
mydict=df1.to_dict()
for i,j in mydict.items():
    print(i,':\t', j)


