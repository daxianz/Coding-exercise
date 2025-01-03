import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Calendar
# 导入Excel文件
df=pd.read_excel('202001.xls')
data=df.stack()  # 行列转换
# 求最大值和最小值
mymax=round(max(data),2)
mymin=round(min(data),2)
# 生成日期
index=pd.date_range('20200601','20200630')  
# 合并列表
data_list=list(zip(index,data))
# 生成日历图
calendar=Calendar()
calendar.add("",
             data_list,
             calendar_opts=opts.CalendarOpts(range_=['2020-06-01','2020-06-30']))
calendar.set_global_opts(
        title_opts=opts.TitleOpts(title="2020年6月加班情况",pos_left='center'),
        visualmap_opts=opts.VisualMapOpts(
            max_=mymax,
            min_=mymin+0.1,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="70px",
        ),
    )
calendar.render("mycalendar.html")