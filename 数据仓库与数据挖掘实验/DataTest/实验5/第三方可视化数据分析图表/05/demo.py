from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
bar =(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 主题风格
     # x轴和y轴数据
    .add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    .add_yaxis("零基础学Python", [2567, 1888, 1359, 3400, 4050, 5500])
    .add_yaxis("Python趣味案例编程", [1567, 988, 2270,3900, 2750, 3600])
    # 设置图表标题
    .set_global_opts(title_opts=opts.TitleOpts("热门图书销量分析",   # 主标题
                                               padding=[10,4,5,90],  # 标题内边距
                                               subtitle='www.mingrisoft.com',  # 副标题
                                               item_gap=5,         # 主标题与副标题之间的间距
                                               # 主标题字体颜色和大小
                                               title_textstyle_opts=opts.TextStyleOpts(color='red',font_size=18)),
                     # 设置图例
                     legend_opts=opts.LegendOpts(pos_right=50,   # 图例离容器右侧的距离
                            item_width=45, # 图例标记的宽度
                            legend_icon='circle'),  # 图例标记的样式为圆形
                     # 提示框
                     tooltip_opts=opts.TooltipOpts(trigger="axis", # 坐标轴触发
                              trigger_on='click', # 鼠标点击时触发
                              axis_pointer_type='cross',  # 十字线指示器
                              background_color='blue',  # 背景色为蓝色
                              border_width=2,      # 边框宽度
                              border_color='red')  # 边框颜色为红色
                     )
    )
bar.render("mycharts5.html")        # 生成图表

