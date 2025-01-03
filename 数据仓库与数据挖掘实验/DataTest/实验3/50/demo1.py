import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#读取数据集tips
tips =pd.read_csv('tips.csv')
sns.violinplot(x='total_bill',y='day',hue='time',data=tips)
plt.show()

