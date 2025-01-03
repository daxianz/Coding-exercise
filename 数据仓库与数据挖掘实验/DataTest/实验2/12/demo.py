import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.random([5, 5]),
     columns=['A1', 'A2', 'A3','A4','A5'])
print(df)
print(df.round(2))                                   #保留小数点后两位
print(df.round({'A1': 1, 'A2': 2}))                  #A1列保留小数点后一位、A2列保留小数点后两位
s1 = pd.Series([1, 0, 2], index=['A1', 'A2', 'A3'])
print(df.round(s1))                                  #设置Series对象小数位数

#print(df.applymap(lambda x: '%.2f'%x))              #通过自定义函数设置小数位数，返回类型为object

