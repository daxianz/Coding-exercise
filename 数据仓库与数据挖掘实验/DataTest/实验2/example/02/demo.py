import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
aa =r'000001.xlsx'
#设置数据显示的列数和宽度
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame(pd.read_excel(aa))
df['date'] = pd.to_datetime(df['date']) #将数据类型转换为日期类型
df = df.set_index('date') # 将date设置为index
df=df[['close']]

df['20天'] = np.round(df['close'].rolling(window = 20, center = False).mean(), 2)
df['50天'] = np.round(df['close'].rolling(window = 50, center = False).mean(), 2)
df['200天'] = np.round(df['close'].rolling(window = 200, center = False).mean(), 2)
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df.plot(secondary_y = ["收盘价", "20","50","200"], grid = True)
plt.legend(('收盘价','20天', '50天', '200天'), loc='upper right')
plt.show()
