import pandas as pd
from matplotlib import pyplot as plt
df1 = pd.read_excel('data2.xls')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.figure(figsize=(5,3)) #设置画布大小
labels = df1['省']
sizes = df1['销量']
#设置饼形图每块的颜色
colors = ['red', 'yellow', 'slateblue', 'green','magenta','cyan','darkorange','lawngreen','pink','gold']
plt.pie(sizes, #绘图数据
        labels=labels,#添加区域水平标签
        colors=colors,# 设置饼图的自定义填充色
        autopct='%.1f%%',# 设置百分比的格式，这里保留一位小数
        #radius =1 , # 设置饼图的半径
        pctdistance=0.85,
        startangle = 180,
        textprops = {'fontsize':9, 'color':'k'}, # 设置文本标签的属性值
        wedgeprops = {'width': 0.4, 'edgecolor': 'k'})
plt.title('2020年1月各省销量占比情况分析')
plt.show()