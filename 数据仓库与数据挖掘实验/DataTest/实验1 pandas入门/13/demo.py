import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('1月.xlsx',sheet_name='莫寒')

print(df.head())         #输出前5条数据

