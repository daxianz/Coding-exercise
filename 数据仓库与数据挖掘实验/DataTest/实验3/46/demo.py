import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
#加载内置数据集tips（小费数据集），并对total_bill和tip字段绘制散点图
tips=sns.load_dataset('tips')
sns.relplot(x='total_bill',y='tip',data=tips,color='r')
plt.show()# 显示

