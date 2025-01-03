import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()       # 使用默认设置
plt.figure(figsize=(6,6))
plt.rcParams['font.sans-serif'] = ['SimHei']	# 显示中文
df=pd.read_csv('data.csv',encoding='gb2312')    #导入Excel文件
series=df['中奖号码'].str.split('  ',expand=True) #提取每一位中奖号码
#对每一位中奖号码统计出现次数
df1=df.groupby(series[0]).size()
df2=df.groupby(series[1]).size()
df3=df.groupby(series[2]).size()
df4=df.groupby(series[3]).size()
df5=df.groupby(series[4]).size()
df6=df.groupby(series[5]).size()
df7=df.groupby(series[6]).size()
#横向表合并（行对齐）
data = pd.concat([df1,df2,df3,df4,df5,df6,df7], axis=1,sort=True)
data=data.fillna(0)   #空值NaN替换为0
data=data.round(0).astype(int)#浮点数转换为整数
plt.title('统计2014~2019年双色球中奖数字热力图')
sns.heatmap(data,annot=True, fmt='d', lw=0.5)#绘制热力图
plt.xlabel('中奖号码位数')
plt.ylabel('双色球数字')
x=['第1位','第2位','第3位','第4位','第5位','第6位','第7位']
plt.xticks(range(0,7,1),x,ha='left')
plt.show()
