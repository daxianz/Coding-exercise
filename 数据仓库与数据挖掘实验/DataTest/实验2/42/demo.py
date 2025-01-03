# import pandas as pd
# #解决数据输出时列名不对齐的问题
# pd.set_option('display.unicode.east_asian_width', True)
# data = [['a',110,105,99],['b',105,88,115],['c',109,120,130],['d',112,115]]
# index = [1,2,3,4]
# columns = ['name','语文','数学','英语']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# print(df)
#
# #相对位置，保存在程序所在路径下
# df.to_csv('Result1.csv',encoding='gb2312')
# #绝对位置
# df.to_csv('d:\Result.csv',encoding='gb2312')
# #分隔符。使用问号（?）分隔符分隔需要保存的数据
# df.to_csv('Result2.csv',sep='?',encoding='gb2312')
# #替换空值，缺失值保存为NA
# df.to_csv('Result3.csv',na_rep='NA',encoding='gb2312')
# #格式化数据，保留两位小数
# df.to_csv('Result4.csv',float_format='%.2f',encoding='gb2312')
# #保留某列数据，保存索引列和name列
# df.to_csv('Result5.csv',columns=['name'],encoding='gb2312')
# #是否保留列名，不保留列名
# df.to_csv('Result6.csv',header=0,encoding='gb2312')
# #是否保留行索引，不保留行索引
# df.to_csv('Result7.csv',index=0,encoding='gb2312')
import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)

# 创建数据框，包含学生姓名和他们的各科成绩
data = [['a', 110, 105, 99], ['b', 105, 88, 115], ['c', 109, 120, 130], ['d', 112, 115]]
index = [1, 2, 3, 4]
columns = ['name', '语文', '数学', '英语']
df = pd.DataFrame(data=data, index=index, columns=columns)

# 输出数据框
print(df)

# 保存数据框为不同格式的CSV文件

# 1. 保存为相对路径
df.to_csv('Result1.csv', encoding='gb2312')

# 2. 保存为绝对路径
df.to_csv('d:\\Result.csv', encoding='gb2312')

# 3. 使用问号（?）作为分隔符
df.to_csv('Result2.csv', sep='?', encoding='gb2312')

# 4. 替换空值，用NA表示
df.to_csv('Result3.csv', na_rep='NA', encoding='gb2312')

# 5. 格式化数据，保留两位小数
df.to_csv('Result4.csv', float_format='%.2f', encoding='gb2312')

# 6. 只保存'name'列
df.to_csv('Result5.csv', columns=['name'], encoding='gb2312')

# 7. 保存时不保留列名
df.to_csv('Result6.csv', header=0, encoding='gb2312')

# 8. 保存时不保留行索引
df.to_csv('Result7.csv', index=0, encoding='gb2312')
