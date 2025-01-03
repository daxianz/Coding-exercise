import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('1月.xlsx')
print(df.head())

#设置“买家会员名”为行索引
df=df.set_index(['买家会员名'])
print(df.head())
