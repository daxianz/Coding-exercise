import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.DataFrame({'原日期':['14-Feb-20', '02/14/2020', '2020.02.14', '2020/02/14','20200214']})
df['转换后的日期']=pd.to_datetime(df['原日期'])
print(df)

