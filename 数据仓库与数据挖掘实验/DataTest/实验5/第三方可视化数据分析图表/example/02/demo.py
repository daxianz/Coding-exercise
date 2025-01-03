import pyecharts.options as opts
from pyecharts.charts import Bar, Line
import pandas as pd
import numpy
# 导入Excel文件
df=pd.read_excel('books.xlsx')
x_data =list(df['月份'])
y1=list(df['京东'])
y2=list(df['天猫'])
y3=list(df['自营'])
# 颜色列表
colors = ["#5793f3", "#FFD700", "#675bba"]
# 求平均值并保留整数位
y_average=list(((df['京东']+df['天猫']+df['自营'])/3).apply(numpy.round))
# 绘制柱形图
legend_list =["京东","天猫","自营"]
bar = (
    Bar(init_opts=opts.InitOpts(width="1000px", height="500px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="京东",
        yaxis_data=y1,
        color=colors[0],
        yaxis_index=0,
    )
    .add_yaxis(
        series_name="天猫",yaxis_data=y2,color=colors[1]
    )
    .add_yaxis(
        series_name="自营",yaxis_data=y3,color=colors[2]
    )
    .extend_axis(yaxis=opts.AxisOpts())
)
# 绘制折线图
line =Line()
line.add_xaxis(xaxis_data=x_data)
line.add_yaxis(
        series_name="平均销量",
        y_axis=y_average,     # y轴平均值
        color='red',
        yaxis_index=1,
    )
# 渲染图表到HTML文件，存放在程序所在目录下
bar.overlap(line).render("barline.html")


