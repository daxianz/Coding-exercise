import pyecharts.options as opts
from pyecharts.charts import HeatMap
import pandas as pd

# 导入Excel文件
df=pd.read_csv('data.csv',encoding='gb2312')
series=df['中奖号码'].str.split('  ',expand=True) # 提取中奖号码
# 统计每一位中奖号码出现的次数
df1=df.groupby(series[0]).size()
df2=df.groupby(series[1]).size()
df3=df.groupby(series[2]).size()
df4=df.groupby(series[3]).size()
df5=df.groupby(series[4]).size()
df6=df.groupby(series[5]).size()
df7=df.groupby(series[6]).size()
#横向表合并（行对齐）
data = pd.concat([df1,df2,df3,df4,df5,df6,df7], axis=1,sort=True)
data=data.fillna(0)   #空值NaN替换为0
data=data.round(0).astype(int)#浮点数转换为整数
# 数据转换为HeatMap支持的列表格式
value1=[]
for i in range(7):
    for j in range(33):
        value1.append([i,j,int(data.iloc[j,i])])
# 绘制热力图
x=['第1位','第2位','第3位','第4位','第5位','第6位','第7位']
heatmap=HeatMap(init_opts=opts.InitOpts(width='600px',height='650px'))
heatmap.add_xaxis(x)
heatmap.add_yaxis("aa",list(data.index),value=value1,  # y轴数据
                  # y轴标签
                  label_opts=opts.LabelOpts(is_show=True,color='white',position="center"))
heatmap.set_global_opts(title_opts=opts.TitleOpts(title="统计2014~2019年双色球中奖号码出现的次数",pos_left="center"),
        legend_opts=opts.LegendOpts(is_show=False),# 不显示图例
        xaxis_opts=opts.AxisOpts( # 坐标轴配置项
            type_="category",  # 类目轴
            splitarea_opts=opts.SplitAreaOpts( # 分隔区域配置项
                is_show=True,
                # 区域填充样式
                areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
            ),
        yaxis_opts=opts.AxisOpts( # 坐标轴配置项
            type_="category", # 类目轴
            splitarea_opts=opts.SplitAreaOpts( # 分隔区域配置项
                is_show=True,
                # 区域填充样式
                areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        # 视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True,   # 分段显示
                                          min_=1,max_=170,     # 最小值、最大值
                                          orient='horizontal', # 水平方向
                                          pos_left="center")   # 居中
    )
heatmap.render("heatmap.html")
