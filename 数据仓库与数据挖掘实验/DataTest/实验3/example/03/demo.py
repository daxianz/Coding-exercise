from matplotlib import font_manager as fm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.style.use('ggplot')
from  matplotlib import cm
#原始数据
shapes = ['天津', '江西省', '安徽省', '云南省', '福建省', '河南省', '辽宁省',
       '重庆', '湖南省', '四川省', '北京', '上海', '广西壮族自治区', '河北省',
       '浙江省', '江苏省', '湖北省', '山东省', '广东省']
values = [287,383,842,866,1187,1405,1495,1620,1717,
          2313,2378,3070,4332,5841,6482,7785,9358,9818,20254]
s = pd.Series(values, index=shapes)
labels = s.index
sizes = s.values
fig, ax = plt.subplots(figsize=(6,6)) # 设置绘图区域大小
colors = cm.rainbow(np.arange(len(sizes))/len(sizes)) # 颜色地图：秋天→彩虹→灰色→春天→黑色
patches, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%',
        shadow=False, startangle=170, colors=colors)
ax.axis('equal')
ax.set_title('各省线上图书销售占比图', loc='left')
# 重新设置字体大小
proptease = fm.FontProperties()
# 字体大小（从小到大）: xx-small、x-small、small、medium、large、x-large、xx-large，或者是数字，如18
proptease.set_size('small')
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)
plt.show()