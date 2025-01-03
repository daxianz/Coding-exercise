import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,120,110],[130,130,130],[130,120,130],[113,123,101]]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,columns=columns)
print(df)

print(df.median())
