import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1=pd.read_excel('1月.xlsx',usecols=[0])                  #通过指定列索引号导入第0列
print(df1.head())
df1 = pd.read_excel('1月.xlsx', usecols=[0, 3])            #通过指定列索引号导入第0列、第3列
print(df1.head())
df1=pd.read_excel('1月.xlsx',usecols=['买家会员名','宝贝标题'])   #通过指定列名导入指定列
print(df1.head())

