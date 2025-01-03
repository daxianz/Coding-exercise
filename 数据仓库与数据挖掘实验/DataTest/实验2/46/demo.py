import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.DataFrame({'原日期':['2019.1.05', '2019.2.15', '2019.3.25','2019.6.25','2019.9.15','2019.12.31']})
df['日期']=pd.to_datetime(df['原日期'])
print(df)
df['年'],df['月'],df['日']=df['日期'].dt.year,df['日期'].dt.month,df['日期'].dt.day
df['星期几']=df['日期'].dt.day_name()
df['季度']=df['日期'].dt.quarter
df['是否年底']=df['日期'].dt.is_year_end
print(df)