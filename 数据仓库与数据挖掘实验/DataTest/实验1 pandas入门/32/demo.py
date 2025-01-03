import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130],[112,115,140]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
print('原数据：')
print(df)

print('修改后：')
df.rename(columns = {'语文':'语文（上）','数学':'数学（上）','英语':'英语（上）'},inplace = True)
print(df)
