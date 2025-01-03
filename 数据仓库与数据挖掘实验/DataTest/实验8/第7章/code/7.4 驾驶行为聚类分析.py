import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
from sklearn import cluster, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler

# 读取数据
data = pd.read_csv('../tmp/data.csv', encoding='gbk')
X = StandardScaler().fit_transform(data.iloc[:, 1:])  # 指标数据标准化

y_pre_com1 = []
def model_(d, y_pre_com):
    # 创建聚类模型
    connectivity = kneighbors_graph(d, n_neighbors=10)
    connectivity = 0.5 * (connectivity + connectivity.T)
    # K值中心聚类
    kmeans = cluster.KMeans(n_clusters=3, random_state=123)
    # 层次聚类
    average_linkage = cluster.AgglomerativeClustering(linkage='average',
                                                     affinity='euclidean',
                                                     n_clusters=3,
                                                     connectivity=connectivity)
    # 高斯混合模型聚类
    gmm = mixture.GaussianMixture(n_components=3, random_state=123)
    # 谱聚类
    spectral = cluster.SpectralClustering(n_clusters=3, affinity='nearest_neighbors',
                                          random_state=123)
    # 聚类模型整合
    clustering_algorithms = (('K-Means', kmeans),
        ('Average linkage agglomerative clustering', average_linkage),
        ('GanssianMixture', gmm),
        ('Spectral clustering', spectral))
    # 预测各车辆行驶标签
    for i, (alg_name, algorithm) in enumerate(clustering_algorithms):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            algorithm.fit(d)
            if hasattr(algorithm, 'labels_'):
                y_pred = algorithm.labels_.astype(np.int)
            else:
                y_pred = algorithm.predict(d)
            y_pre_com.append(y_pred)
model_(X, y_pre_com1)
# 聚类分析
colors = ['blue','orange','green']  # 定义线条颜色
# K-Means聚类
data['labels'] = y_pre_com1[0].tolist()
c0 = data.loc[data['labels'] == 0]
c1 = data.loc[data['labels'] == 1]
c2 = data.loc[data['labels'] == 2]
# 绘制图形
plt.scatter(c0['sd_speed'], c0['avg_speed'], c=colors[0], marker='o', label='簇1')  
plt.scatter(c1['sd_speed'], c1['avg_speed'], c=colors[1], marker='s', label='簇2')  
plt.scatter(c2['sd_speed'], c2['avg_speed'], c=colors[2], marker='*', label='簇3')  
plt.xlabel('sd_speed')  
plt.ylabel('avg_speed')  
plt.legend(loc=2)  
plt.title('K-Means聚类')
plt.show()
print('K-Means聚类簇1个数：', c0['labels'].count())
print('K-Means聚类簇2个数：', c1['labels'].count())
print('K-Means聚类簇3个数：', c2['labels'].count())

# 层次聚类
data['labels'] = y_pre_com1[1].tolist()
c0 = data.loc[data['labels'] == 0]
c1 = data.loc[data['labels'] == 1]
c2 = data.loc[data['labels'] == 2]
# 绘制图形
plt.scatter(c0['sd_speed'], c0['avg_speed'], c=colors[0], marker='o', label='簇1')  
plt.scatter(c1['sd_speed'], c1['avg_speed'], c=colors[1], marker='s', label='簇2')  
plt.scatter(c2['sd_speed'], c2['avg_speed'], c=colors[2], marker='*', label='簇3')  
plt.xlabel('sd_speed')  
plt.ylabel('avg_speed') 
plt.legend(loc=2)  
plt.title('层次聚类')
plt.show()
print('层次聚类簇1个数：', c0['labels'].count())
print('层次聚类簇2个数：', c1['labels'].count())
print('层次聚类簇3个数：', c2['labels'].count())

# 高斯混合模型聚类
data['labels'] = y_pre_com1[2].tolist()
c0 = data.loc[data['labels'] == 0]
c1 = data.loc[data['labels'] == 1]
c2 = data.loc[data['labels'] == 2]
# 绘制图形
plt.scatter(c0['sd_speed'], c0['avg_speed'], c=colors[0], marker='o', label='簇1')  
plt.scatter(c1['sd_speed'], c1['avg_speed'], c=colors[1], marker='s', label='簇2')  
plt.scatter(c2['sd_speed'], c2['avg_speed'], c=colors[2], marker='*', label='簇3')  
plt.xlabel('sd_speed')  
plt.ylabel('avg_speed')  
plt.legend(loc=2)  
plt.title('高斯混合模型聚类')
plt.show()
print('高斯混合模型聚类簇1个数：', c0['labels'].count())
print('高斯混合模型聚类簇2个数：', c1['labels'].count())
print('高斯混合模型聚类簇3个数：', c2['labels'].count())

# 谱聚类
data['labels'] = y_pre_com1[3].tolist()
c0 = data.loc[data['labels'] == 0]
c1 = data.loc[data['labels'] == 1]
c2 = data.loc[data['labels'] == 2]
# 绘制图形
plt.scatter(c0['sd_speed'], c0['avg_speed'], c=colors[0], marker='o', label='簇1')  
plt.scatter(c1['sd_speed'], c1['avg_speed'], c=colors[1], marker='s', label='簇2')  
plt.scatter(c2['sd_speed'], c2['avg_speed'], c=colors[2], marker='*', label='簇3')  
plt.xlabel('sd_speed')  
plt.ylabel('avg_speed')  
plt.legend(loc=2)  
plt.title('谱聚类1')
plt.show()
print('第一次谱聚类簇1个数：', c0['labels'].count())
print('第一次谱聚类簇2个数：', c1['labels'].count())
print('第一次谱聚类簇3个数：', c2['labels'].count())

# 至此，所有的聚类分析都已实现，其中谱聚类效果较好，但簇1和簇3还不能清楚的分类出来，故选取标准差指标和比率指标进一步聚类
X_no = data[['slip_rate', 'dscs_rate', 'tired_rate', 'plus_rate',
              'minus_rate', 'sd_speed', 'sd_speed_diff']].values
X2 = StandardScaler().fit_transform(X_no)
y_pre_com2 =[]
model_(X2, y_pre_com2)
# 第二次谱聚类
data['labels'] = y_pre_com2[3].tolist()
c0 = data.loc[data['labels'] == 0]
c1 = data.loc[data['labels'] == 1]
c2 = data.loc[data['labels'] == 2]
# 绘制图形
plt.scatter(c0['sd_speed'], c0['avg_speed'], c=colors[0], marker='o', label='簇1')  
plt.scatter(c1['sd_speed'], c1['avg_speed'], c=colors[1], marker='s', label='簇2')  
plt.scatter(c2['sd_speed'], c2['avg_speed'], c=colors[2], marker='*', label='簇3')  
plt.xlabel('sd_speed')  
plt.ylabel('avg_speed')  
plt.legend(loc=2)
plt.title('谱聚类2')
plt.show()
print('第二次谱聚类簇1个数：', c0['labels'].count())
print('第二次谱聚类簇2个数：', c1['labels'].count())
print('第二次谱聚类簇3个数：', c2['labels'].count())

# 写出数据文件
data.to_csv('../tmp/new_data.csv', index=0, encoding='gbk')