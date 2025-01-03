import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style('darkgrid')
#读取数据集tips
tips=pd.read_csv('tips.csv')
#绘制箱形图
sns.boxplot(x='day',y='total_bill',hue='time',data=tips)
plt.show()# 显示图表

