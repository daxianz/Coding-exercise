#-*- coding: utf-8 -*-
#主成分分析 降维
import pandas as pd

#参数初始化
inputfile = '../data/principal_component.xls'
outputfile = '../tmp/dimention_reducted.xlsx' #降维后的数据

data = pd.read_excel(inputfile, header = None) #读入数据

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)
print("模型的各个特征向量")
print(pca.components_) #返回模型的各个特征向量
print("各个成分的方差百分比")
print(pca.explained_variance_ratio_) #返回各个成分各自的方差百分比

pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)                  # 用它来降低维度
pd.DataFrame(low_d).to_excel(outputfile, index = False,engine='openpyxl')     # 保存结果
pca.inverse_transform(low_d)                 # 必要时可以用inverse_transform()函数来复原数据