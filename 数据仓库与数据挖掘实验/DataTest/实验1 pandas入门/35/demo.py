import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130],[112,115,140]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
print('原数据：')
print(df)

#删除行列数据
print('删除行列数据：')
print(df.drop(['数学'],axis=1,inplace=True))                     #删除某列
#print(df.drop(columns='数学',inplace=True))                                   #删除columns为“数学”的列
#df.drop(labels='数学', axis=1,inplace=True)                            #删除列标签为“数学” 的列
#print(df.drop(['明日','二月二'],inplace=True))                   #删除某行
#df.drop(index='明日',inplace=True)                                     #删除index为“明日”的行
#df.drop(labels='明日', axis=0,inplace=True)                            #删除行标签为“明日”的行
