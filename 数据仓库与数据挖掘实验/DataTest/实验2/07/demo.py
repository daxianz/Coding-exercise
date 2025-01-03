import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,120,110],[130,130,130],[130,120,130]]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,columns=columns)
print(df.mode())           #三科成绩的众数
print(df.mode(axis=1))     #每一行的众数
print(df['数学'].mode())   #“数学”的众数
