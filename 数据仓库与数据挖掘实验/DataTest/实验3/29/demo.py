import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('data1.xls',sheet_name='高二一班')
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
X = df.loc[:,"语文":"生物"].values
name=df['姓名']
plt.imshow(X)
plt.xticks(range(0,6,1),['语文','数学','英语','物理','化学','生物'])#设置x轴刻度标签
plt.yticks(range(0,12,1),name)#设置y轴刻度标签
plt.colorbar()  #显示颜色条
plt.title('学生成绩统计热力图')
plt.show()