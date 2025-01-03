import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1=pd.read_excel('1月.xlsx',index_col=0)  #设置“买家会员名”为行索引
print(df1.head())                          #输出前5条数据
df2=pd.read_excel('1月.xlsx',header=1)     #设置第1行为列索引
print(df2.head())
df3=pd.read_excel('1月.xlsx',header=None)  #列索引为数字
print(df3.head())
#通过索引快速检索数据
print(df3[0])
print(df1.loc['mrhy1'])
