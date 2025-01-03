import pandas as pd  #导入pandas模块
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_csv('JD.csv',encoding='gbk')  #导入csv文件
df=df.set_index(['商品名称'])
#创建字典
dict1={'上海出库销量':'北上广','北京出库销量':'北上广',
         '广州出库销量':'北上广','成都出库销量':'成都',
         '武汉出库销量':'武汉','西安出库销量':'西安'}
df1=df.groupby(dict1,axis=1).sum()
print(df1)


