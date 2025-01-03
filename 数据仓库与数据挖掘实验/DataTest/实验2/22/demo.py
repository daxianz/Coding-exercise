import pandas as pd  #导入pandas模块
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('1月.xlsx')  #导入Excel文件
#x是“宝贝标题”对应的列
#value_counts()函数用于Series对象中的每个值进行计数并且排序
max1 = lambda x: x.value_counts(dropna=False).index[0]
max1.__name__ = "购买次数最多"
df1=df.agg({'宝贝标题': [max1],
        '数量': ['sum', 'mean'],
        '买家实际支付金额': ['sum', 'mean']})
print(df1)