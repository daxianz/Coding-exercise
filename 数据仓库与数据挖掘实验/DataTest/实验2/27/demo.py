import pandas as pd
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
#导入Excel文件部分列数据（“买家会员名”和“宝贝标题”）
df = pd.read_excel('mrbooks.xls',usecols=['买家会员名','宝贝标题'])
#使用join方法和split方法分割“宝贝标题”
df = df.join(df['宝贝标题'].str.split('，', expand=True))
print(df.head())

