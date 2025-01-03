import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
df1=pd.read_excel('data.xls',sheet_name='sheet2')              #导入Excel文件
sns.barplot(x='学号',y='得分',hue='学科',data=df1)                #条形图
plt.show()# 显示