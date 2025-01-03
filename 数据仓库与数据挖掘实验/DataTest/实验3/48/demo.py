import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
tips=sns.load_dataset('tips')
#绘制箱形图
sns.boxplot(x='day',y='total_bill',hue='time',data=tips)
plt.show()# 显示图表

