import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings('ignore')  # 忽略警告信息
# 读取驾驶行为数据
data = pd.read_csv('../tmp/data.csv', encoding='gbk')
print(data.describe())  # 查看数据的相关统计量，包括数量、均值、最大值、最小值等
print(data.info())  # 查看数据类型

# 相关性分析
correlation = data.corr()  # 皮尔逊相关系数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
f , ax = plt.subplots(figsize=(7, 7))
plt.title('各属性相关系数热力图', fontsize=14)
sns.heatmap(correlation, square=True, vmax=1)  # vmax-热力图颜色取值的最大值,默认会从数据集中推导

# 异常值检测
data['mileage'].value_counts()  # 查看mileage分布
data['tired'].value_counts()  # 查看tired分布
data['slip'].value_counts()  # 查看slip分布
data['dscs'].value_counts()  # 查看dscs分布
# 绘制箱线图
data.boxplot(['mileage'])
data.boxplot(['tired'])
data.boxplot(['slip'])
data.boxplot(['dscs'])





