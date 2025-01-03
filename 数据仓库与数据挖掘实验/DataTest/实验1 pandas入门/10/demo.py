import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130]]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,columns=columns)
print(df)

