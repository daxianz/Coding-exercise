import pandas as pd
import numpy as np
import keras
from sklearn import cluster
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import Dense
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


data = pd.read_csv('../tmp/new_data.csv', encoding='gbk')
# 构建LDA模型，并进行判别
td = data.iloc[:, 1:-1]
td_z = (td - td.mean()) / (td.std())
model = cluster.SpectralClustering(n_clusters=3, affinity='nearest_neighbors',
                                          random_state=123)
yhat = model.fit_predict(td_z)
X_no = data[['slip_rate', 'dscs_rate', 'tired_rate', 'plus_rate',
              'minus_rate', 'sd_speed', 'sd_speed_diff']].values
X2 = StandardScaler().fit_transform(X_no)
model = LinearDiscriminantAnalysis()
model.fit(X2, yhat)  # 拟合训练
print('预测精度为：', model.score(X2, yhat))  # 计算预测精度

lda_scores = model.fit(X2, yhat).transform(X2)
LDA_scores = pd.DataFrame(lda_scores, columns=['LD1', 'LD2'])
LDA_scores['species'] = yhat
d = {0: '疲惫', 1: '激进', 2: '稳健'}
LDA_scores['species'] = LDA_scores['species'].map(d) 


# 构建朴素贝叶斯模型，并进行判别
X1 = data.drop(['labels'],axis=1)
y = data['labels']
def nb_fit(X1, y):
    classes = y.unique()
    class_count = y.value_counts()
    class_prior = class_count / len(y)
    prior = dict()
    for col in X1.columns:
        for j in classes:
            p_x_y = X1[(y == j).values][col].value_counts()
            for i in p_x_y.index:
                prior[(col, i, j)] = p_x_y[i] / class_count[j]
    return classes, class_prior, prior
nb_fit(X1, y)

x1 = X2
y1 = data.values[:, -1]
print('x = \n', x1)
print('y = \n', y1)
le = preprocessing.LabelEncoder()
le.fit([0, 1, 2])
print(le.classes_)
y1 = le.transform(y1)
print('Last Version, y = \n', y1)

# 先验为高斯分布的朴素贝叶斯
GN = GaussianNB()
GN.fit(x1,y1)
print('得分为：', GN.score(x1,y1))
# 先验为伯努利分布的朴素贝叶斯
BN=BernoulliNB()
BN.fit(x1,y1)
print('得分为：', BN.score(x1,y1))


# 构建神经网络模型，并进行判别
X = StandardScaler().fit_transform(data.iloc[:, 1:-1])
target = data['labels']  # 标签
# 划分数据集
x_train, x_test, y_train, y_test = train_test_split(np.float32(X), np.float32(target),
                                                    test_size=0.2, random_state=123)
# 构建模型
model = Sequential()
model.add(Dense(10, activation='relu', input_dim=14))
model.add(Dense(3, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

labels = keras.utils.to_categorical(y_train, num_classes=3)
test_labels = keras.utils.to_categorical(y_test, num_classes=3)
# 模型训练与评价
model.fit(x_train, labels,validation_data=(x_test, test_labels), epochs=100, batch_size=32)

