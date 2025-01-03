import pandas as pd
from pyecharts.charts import Boxplot

# 导入Excel文件
df = pd.read_excel('Tips.xlsx')
y_data=[list(df['总消费'])]

boxplot=Boxplot()   #创建箱形图
# 为箱形图添加数据
boxplot.add_xaxis([""])
boxplot.add_yaxis('',y_axis=boxplot.prepare_data(y_data))
# 渲染图表到HTML文件，存放在程序所在目录下
boxplot.render("myboxplot.html")


