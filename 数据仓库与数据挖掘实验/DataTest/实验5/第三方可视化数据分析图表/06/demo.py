from pyecharts import options as opts
from pyecharts.charts import Bar

bar=Bar()

# 为柱状图添加数据
bar.add_dataset(source=[
            ["val", "销量","月份"],
            [24, 10009, "1月"],
            [57, 19988, "2月"],
            [74, 39870, "3月"],
            [50, 12345, "4月"],
            [99, 50145, "5月"],
            [68, 29146, "6月"]
            ]
        )
bar.add_yaxis(
        series_name="销量",   # 系列名称
        yaxis_data=[],       # 系列数据
        encode={"x": "销量", "y": "月份"},   # 对x轴y轴数据进行编码
        label_opts=opts.LabelOpts(is_show=False)  #不显示标签文本
        )
bar.set_global_opts(
        title_opts=opts.TitleOpts("线上图书月销量分析", # 主标题
                                  subtitle='www.mingrisoft.com'), # 副标题
        xaxis_opts=opts.AxisOpts(name="销量"),        # x轴坐标轴名称
        yaxis_opts=opts.AxisOpts(type_="category"),   # y轴坐标轴类型为“类目”
        # 视觉映射
        visualmap_opts=opts.VisualMapOpts(
            orient="horizontal",                      # 水平放置颜色条
            pos_left="center",                        # 居中
            min_=10,                                  # 颜色条最小值
            max_=100,                                 # 颜色条最大值
            range_text=["High", "Low"],               # 颜色条两端的文本
            dimension=0,                              # 颜色条映射的维度
            range_color=["#FFF0F5", "#8B008B"]        # 颜色范围
                         )
        )
bar.render("mycharts6.html")                          # 生成图表

