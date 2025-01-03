import pandas as pd
excelFile = 'books.xls'
dfrow = pd.DataFrame(pd.read_excel(excelFile))
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


print('-------------------------按行数据排序-------------------------')
#按照索引值为0的行，即第一行的值升序排序
dfrow.sort_values(by=0,ascending=True,axis=1)
print(dfrow.sort_values(by=0,ascending=True,axis=1))



