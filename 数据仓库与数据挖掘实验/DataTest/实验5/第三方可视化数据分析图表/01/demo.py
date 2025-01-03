from pyecharts.charts import Bar  # 从Pyecharts模块导入Bar对象

bar = Bar()  # 创建一个空的Bar（柱状图）对象
# 定义x轴和y轴数据
bar.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
bar.add_yaxis("零基础学Python", [2567, 1888, 1359, 3400, 4050, 5500])
bar.add_yaxis("Python趣味案例编程", [1567, 988, 2270,3900, 2750, 3600])
# 渲染图表到HTML文件，存放在程序所在目录下
bar.render("mycharts.html")