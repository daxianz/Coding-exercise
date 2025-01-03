import pandas as pd
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(5,3),facecolor='yellow')
#导入Excel文件
df=pd.read_excel('体温.xls')
#折线图
x=df['日期']          #x轴数据
y=df['体温']          #y轴数据
plt.plot(x,y,color='m',linestyle='-',marker='o',mfc='w')
plt.show()

