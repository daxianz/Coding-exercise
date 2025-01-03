import pyecharts.options as opts
from pyecharts.charts import Pie

# 饼形图数据
x1 = ["北京", "上海", "广州"]
y1 = [1168, 890,578]
data1 = [list(z) for z in zip(x1,y1)]
# 环形图数据
x2 = ["北京", "上海", "河南省", "广州", "湖南省", "四川省", "湖北省", "河北省", "江苏省", "浙江省"]
y2 = [1168, 890, 234, 578, 345, 225, 188, 101,999,1300]
data2 = [list(z) for z in zip(x2,y2)]
# 饼形图与环形图组合
(
    Pie(init_opts=opts.InitOpts(width="1000px", height="600px"))
    # 饼形图
    .add(
        series_name="销售地区",
        data_pair=data1,
        radius=[0, "30%"],
        label_opts=opts.LabelOpts(position="inner"), # 饼形图标签
    )
    # 环形图
    .add(
        series_name="销售地区",
        radius=["40%", "55%"],
        data_pair=data2,
        # 环形图标签
        label_opts=opts.LabelOpts(
            position="outside", # 标签位置
            # 标签格式化
            formatter="{a|{a}}{bg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#FAFAD2",  # 背景色
            border_color="#FFA500", # 边框颜色
            border_width=1,  # 边框宽度
            border_radius=4, # 边框半径
            # 利用富文本样式，定义标签效果
            rich={
                "a": {"color": "black", "lineHeight": 22, "align": "center"},
                "bg": {
                    "backgroundColor": "#FFA500",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 14, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
    .render("mypies.html")
)

