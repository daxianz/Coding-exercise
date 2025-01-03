import pandas as pd
from pyecharts.charts import EffectScatter

# 导入Excel文件
df = pd.read_excel('books.xlsx',sheet_name='Sheet2')
# x轴和y轴数据
x=list(df['年份'])
y1=list(df['京东'])
y2=list(df['天猫'])
y3=list(df['自营'])
# 绘制涟漪散点图
scatter=EffectScatter()
scatter.add_xaxis(x)
scatter.add_yaxis("",y1)
scatter.add_yaxis("",y2)
scatter.add_yaxis("",y3)
# 渲染图表到HTML文件，存放在程序所在目录下
scatter.render("myscatter.html")


