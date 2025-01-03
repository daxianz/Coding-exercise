import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130]]
index=['mr001','mr003','mr005']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=index,columns=columns)
print(df)

#通过reindex()方法重新设置行索引、列索引和行列索引
print(df.reindex(['mr001','mr002','mr003','mr004','mr005']))
print(df.reindex(columns=['语文','物理','数学','英语']))
print(df.reindex(index=['mr001','mr002','mr003','mr004','mr005'],columns=['语文','物理','数学','英语']))
