import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df1=pd.read_excel('data.xls')              #导入Excel文件

#绘制多折线图
dfs=[df1['语文'],df1['数学'],df1['英语']]
sns.lineplot(data=dfs)
plt.show()# 显示
