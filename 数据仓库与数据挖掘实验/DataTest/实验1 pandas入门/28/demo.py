import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130],[112,115,140]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

#增加数据，使用insert方法
wl =[88,79,60,50]
df.insert(1,'物理',wl) #在第1列后面插入“物理”，其值为wl的数值。
print(df)
