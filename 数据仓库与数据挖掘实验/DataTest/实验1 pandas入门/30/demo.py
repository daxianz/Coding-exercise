import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130],[112,115,140]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
print(df)

#按行增加数据，增加多行数据
df_insert = pd.DataFrame({'语文':[100,123,138],'数学':[120,142,60],'英语':[99,139,99]},index = ['钱多多','童年','无名'])
df1 = df.append(df_insert)
print(df1)
