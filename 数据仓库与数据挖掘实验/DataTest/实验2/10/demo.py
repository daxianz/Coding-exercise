import pandas as pd
#创建DataFrame数据（数学成绩）
data = [120,89,98,78,65,102,112,56,79,45]
columns = ['数学']
df = pd.DataFrame(data=data,columns=columns)
#计算35%的分位数
x=df['数学'].quantile(0.35)
#输出淘汰学生
print(df[df['数学']<=x])
