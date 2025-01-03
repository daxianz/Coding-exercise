import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel('tips.xlsx')
plt.boxplot(x = df['总消费'], # 指定绘制箱线图的数据
            whis = 1.5, # 指定1.5倍的四分位差
            widths = 0.3, #指定箱线图中箱子的宽度为0.3
            patch_artist = True, #填充箱子颜色
            showmeans = True, #显示均值
            boxprops = {'facecolor':'RoyalBlue'}, # 指定箱子的填充色为宝蓝色
            flierprops = {'markerfacecolor':'red', 'markeredgecolor':'red', 'markersize':3}, # 指定异常值的填充色、边框色和大小
            meanprops = {'marker':'h','markerfacecolor':'black', 'markersize':8},# 指定均值点的标记符号（六边形）、填充色和大小
            medianprops = {'linestyle':'--','color':'orange'}, # 指定中位数的标记符号（虚线）和颜色
            labels = ['']) # 去除x轴刻度值
plt.show()
# 计算下四分位数和上四分位
Q1 = df['总消费'].quantile(q = 0.25)
Q3 = df['总消费'].quantile(q = 0.75)
# 基于1.5倍的四分位差计算上下限对应的值
low_limit = Q1 - 1.5*(Q3 - Q1)
up_limit = Q3 + 1.5*(Q3 - Q1)
# 查找异常值
val=df['总消费'][(df['总消费'] > up_limit) | (df['总消费'] < low_limit)]
print('异常值如下：')
print(val)