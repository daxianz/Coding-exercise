from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

bar =(
    Bar(init_opts=opts.InitOpts(width='500px',height='300px',  # 设置画布大小
                                theme=ThemeType.LIGHT,  # 设置主题
                                #theme=ThemeType.PURPLE_PASSION,  # 紫色
                                bg_color='#fff'))       # 设置图表背景颜色
    # x轴和y轴数据
    .add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    .add_yaxis("零基础学Python", [2567, 1888, 1359, 3400, 4050, 5500])
    .add_yaxis("Python趣味案例编程", [1567, 988, 2270,3900, 2750, 3600])
    )
bar.render("mycharts1.html") # 渲染图表到HTML文件

