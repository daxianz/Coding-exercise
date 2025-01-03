import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
tips=sns.load_dataset('tips')
#绘制回归模型，描述线性关系
sns.lmplot(x='total_bill',y='tip',data=tips)
plt.show()# 显示