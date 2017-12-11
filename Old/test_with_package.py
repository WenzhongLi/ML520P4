# coding : utf-8
#author : GE

import numpy as np
import scipy.cluster.vq as vq
from sklearn.cluster import KMeans
data = np.loadtxt(open("input.csv","rb"),delimiter=",",skiprows=0)

print(type(data))

# estimator = KMeans(n_clusters=40,max_iter=5000)#构造聚类器
# estimator.fit(data)#聚类
# label_pred = estimator.labels_ #获取聚类标签
# print(label_pred)
# centroids = estimator.cluster_centers_ #获取聚类中心
# print(centroids)
# inertia = estimator.inertia_ # 获取聚类准则的总和

centroids, label_pred = vq.kmeans2( data, 101 )

np.savetxt('gray_101.csv', label_pred, delimiter = ',')
np.savetxt('gray_centroids_101.csv', centroids, delimiter = ',')


