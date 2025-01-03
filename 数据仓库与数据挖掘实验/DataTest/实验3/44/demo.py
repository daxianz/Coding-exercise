import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df1=pd.read_excel('data2.xls')              #导入Excel文件
data=df1[['得分']]
sns.distplot(data,rug=True)                #直方图，显示观测的小细条
plt.show()# 显示