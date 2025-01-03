import pandas as pd
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
#导入Excel文件指定列数据（“买家会员名”和“收货地址”）
df = pd.read_excel('mrbooks.xls',usecols=['买家会员名','收货地址'])
#使用split方法分割“收货地址”
series=df['收货地址'].str.split(' ',expand=True)
df['省']=series[0]
df['市']=series[1]
df['区']=series[2]
print(df.head())

