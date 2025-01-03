import pandas as pd
import numpy as np
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,113,102,105,108],[118,98,119,85,118]]
index=['小黑','小白']
columns = ['物理1','物理2','物理3','物理4','物理5']
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print(df.var(axis=1))

