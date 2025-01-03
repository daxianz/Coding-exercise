import pandas as pd
df=pd.read_excel('mrbooks.xls',usecols=['买家会员名','宝贝标题']).head()
df.to_html('mrbooks.html',header = True,index = False)
print(df)