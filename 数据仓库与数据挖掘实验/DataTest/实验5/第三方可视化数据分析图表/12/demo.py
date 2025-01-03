import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# 导入Excel文件
df = pd.read_excel('data2.xls')
x_data=df['地区']
y_data=df['销量']
# 将数据转换为列表加元组的格式（[(key1, value1), (key2, value2)]）
data=[list(z) for z in zip(x_data, y_data)]
# 数据排序
data.sort(key=lambda x: x[1])


pie=Pie()   #创建饼形图
# 为饼形图添加数据
pie.add(
        series_name="地区",    # 序列名称
        data_pair=data,     # 数据
    )
pie.set_global_opts(
        # 饼形图标题居中
        title_opts=opts.TitleOpts(
            title="各地区销量情况分析",
            pos_left="center"),
        # 不显示图例
        legend_opts=opts.LegendOpts(is_show=False),
    )
pie.set_series_opts(
        # 序列标签
        label_opts=opts.LabelOpts(),
    )
# 渲染图表到HTML文件，存放在程序所在目录下
pie.render("mypie1.html")
