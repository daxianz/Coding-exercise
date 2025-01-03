import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.random([5, 5]),
     columns=['A1', 'A2', 'A3','A4','A5'])
df['百分比']=df['A1'].apply(lambda x: format(x,'.0%'))       #整列保留0位小数
print(df)
df['百分比']=df['A1'].apply(lambda x: format(x,'.2%'))       #整列保留两位小数
print(df)
df['百分比']=df['A1'].map(lambda x:'{:.0%}'.format(x))       #整列保留0位小数，也可以使用map函数
print(df)
