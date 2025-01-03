import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style('darkgrid')
#读取数据集tips
tips=pd.read_csv('tips.csv')
#绘制回归模型，描述线性关系
sns.lmplot(x='total_bill',y='tip',data=tips)
plt.show()# 显示

