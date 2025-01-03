import pandas as pd
excelFile = 'mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)

pd.set_option('display.unicode.east_asian_width', True)

print('-------------------------对分组统计结果排序-------------------------')
df1=df.groupby(["类别"])["销量"].sum().reset_index()
df2=df1.sort_values(by='销量',ascending=False)
print(df2)




