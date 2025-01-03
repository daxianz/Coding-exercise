import pandas as pd
excelFile = 'mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
#按“销量”列降序排序
df=df.sort_values(by='销量',ascending=False)
# 顺序排名
df['顺序排名'] = df['销量'].rank(method="first", ascending=False)
print(df[['图书名称', '销量', '顺序排名']])

