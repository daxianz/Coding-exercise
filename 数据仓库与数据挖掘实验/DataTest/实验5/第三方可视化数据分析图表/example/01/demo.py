import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# 导入Excel文件
df = pd.read_excel('data2.xls')
x_data=df['地区']
y_data=df['累计']
# 将数据转换为列表加元组的格式（[(key1, value1), (key2, value2)]）
data=[list(z) for z in zip(x_data, y_data)]
# 数据排序
data.sort(key=lambda x: x[1])

# 创建饼形图并设置画布大小
pie=Pie(init_opts=opts.InitOpts(width='800px',height='400px'))
# 为饼形图添加数据
pie.add(
        series_name="地区",   # 序列名称
        data_pair=data,       # 数据
        radius=["8%","160%"], #内外半径
        center=["60%","80%"], # 位置
        rosetype='area',      # 玫瑰图
        color='auto'          # 颜色自动渐变
    )
pie.set_global_opts(
        # 不显示图例
        legend_opts=opts.LegendOpts(is_show=False),
        # 视觉映射
        visualmap_opts=opts.VisualMapOpts(is_show=False,
         min_=100,    # 颜色条最小值
         max_=450000, # 颜色条最大值
    )
)
pie.set_series_opts(
        # 序列标签
        label_opts=opts.LabelOpts(position='inside',  # 标签位置
                                  rotate=45,
                                  font_size=8)       # 字体大小
                                  #formatter="{b}: {c}") # 标签格式
    )
# 渲染图表到HTML文件，存放在程序所在目录下
pie.render("mypie1.html")
