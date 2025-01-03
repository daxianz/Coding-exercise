import pandas as pd            #导入pandas模块
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('data.xlsx')  #读取Excel文件
pd.set_option('display.max_columns', None)  #显示所有列
pd.set_option('display.max_rows', None)      #显示所有行
print(df)               #显示前5条数据

