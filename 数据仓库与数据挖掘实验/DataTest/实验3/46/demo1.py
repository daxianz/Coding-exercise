import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style('darkgrid')
#读取数据集tips（小费数据集），并对total_bill和tip字段绘制散点图
tips=pd.read_csv('tips.csv')
sns.relplot(x='total_bill',y='tip',data=tips,color='r')
plt.show()# 显示

