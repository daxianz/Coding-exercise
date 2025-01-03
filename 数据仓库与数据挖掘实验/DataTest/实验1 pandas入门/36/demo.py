import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130],[112,115,140]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

#删除特定条件的行
df.drop(index=df[df['数学'].isin([88])].index[0],inplace=True)    #删除“数学”包含88的行
df.drop(index=df[df['语文']<110].index[0],inplace=True)           #删除“语文”小于110的行
print(df)
