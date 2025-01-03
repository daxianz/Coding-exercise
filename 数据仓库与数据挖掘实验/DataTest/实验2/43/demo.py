import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)

# 定义数据和构建DataFrame
data = [['a', 110, 105, 99], ['b', 105, 88, 115], ['c', 109, 120, 130], ['d', 112, 115]]
index = [1, 2, 3, 4]
columns = ['A', '语文', '数学', '英语']
df1 = pd.DataFrame(data=data, index=index, columns=columns)

# 打印DataFrame
print(df1)

# 保存DataFrame到Excel文件
df1.to_excel('df1.xlsx', sheet_name='df1')

# 打开一个新的Excel文件并写入数据
work = pd.ExcelWriter('df2.xlsx')  # 创建Excel文件对象
df1.to_excel(work, sheet_name='df2')  # 将DataFrame保存到第二个sheet
df1['A'].to_excel(work, sheet_name='df3')  # 将第一列保存到第三个sheet
work._save()  # 保存Excel文件
