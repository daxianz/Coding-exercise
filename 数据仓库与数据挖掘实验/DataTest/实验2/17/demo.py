import pandas as pd  #导入pandas模块
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_csv('JD.csv',encoding='gbk')
#抽取数据
df1=df[['二级分类','7天点击量']]
print(df1.groupby('二级分类')['7天点击量'].sum())
