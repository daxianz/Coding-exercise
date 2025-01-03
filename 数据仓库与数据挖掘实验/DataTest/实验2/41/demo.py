import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.DataFrame({'编号':['mr001','mr002','mr003','mr001','mr001'],
                    '体育':[34.5,39.7,38,33,35]})
print(df1)
df2 = pd.DataFrame({'编号':['mr001','mr002','mr003','mr003','mr003'],
                    '语文':[110,105,109,110,108],
                    '数学':[105,88,120,123,119],
                    '英语':[99,115,130,109,128]})
print(df2)
df_merge=pd.merge(df1,df2)
df_merge.to_excel('merge.xlsx',startrow=2)
df_merge.to_csv('merge.csv')