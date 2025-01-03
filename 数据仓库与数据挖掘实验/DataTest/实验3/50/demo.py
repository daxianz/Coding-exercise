import matplotlib.pyplot as plt
import seaborn as sns
#调用seaborn自带数据集tips
tips = sns.load_dataset('tips')
sns.violinplot(x='total_bill',y='day',hue='time',data=tips)
plt.show()

