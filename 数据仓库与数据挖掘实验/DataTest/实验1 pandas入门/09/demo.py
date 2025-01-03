import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130]]
index = [0,1,2]  #行索引
columns = ['语文','数学','英语']  #列索引
df = pd.DataFrame(data, index,columns)
print(df)
#遍历DataFrame表格数据的每一列
for col in df.columns:
    series = df[col]
    print(series)
