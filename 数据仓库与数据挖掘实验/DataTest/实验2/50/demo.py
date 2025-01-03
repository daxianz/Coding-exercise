import pandas as pd

# 设置数据显示的列数和宽度
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)

# 从Excel文件读取数据
df = pd.read_excel('time.xls')

# 将“订单付款时间”列设置为索引
df1 = df.set_index('订单付款时间')

# 按照天（D）重新取样并求和
df_D = df1.resample('D').sum()

# 将每日总和保存为新的Excel文件，改为 .xlsx 格式
df_D.to_excel('dd.xlsx')

# 输出每周的总和（闭合右侧）
print(df1.resample('W').sum())

# 输出每周的总和（闭合右侧的样式）
print(df1.resample('W', closed='right').sum())

# 输出每周的总和（闭合左侧的样式）
print(df1.resample('W', closed='left').sum())
