# coding : utf-8
#author : GE

import numpy as np
from sklearn.cluster import KMeans
data = np.loadtxt(open("input.csv","rb"),delimiter=",",skiprows=0)

print(type(data))

estimator = KMeans(n_clusters=60,max_iter=1000)#构造聚类器
estimator.fit(data)#聚类
label_pred = estimator.labels_ #获取聚类标签
print(label_pred)
centroids = estimator.cluster_centers_ #获取聚类中心
print(centroids)
inertia = estimator.inertia_ # 获取聚类准则的总和
np.savetxt('new.csv', label_pred, delimiter = ',')