# coding : utf-8
#author : GE
import numpy as np
import random
import sys

class KMeans:
    def __init__(self):
        pass

    def distance(self,x,y):
        return np.sqrt(np.sum(np.power(x - y,2)))

    def createRC(self,data,k):
        n = data.shape[1]
        centroids = np.zeros((k,n))
        for j in range(n):
            minJ = min(data[:,j])
            maxJ = max(data[:,j])
            rangeJ = maxJ - minJ
            centroids[:,j] = minJ + rangeJ * random.random(k,1)
        return centroids

    def KMeans(self,data,k):
        m = data.shape[0]
        centroids = self.createRC(data,k)
        assignment_mat = np.zeros((m,2))
        flag = True
        while flag:
            flag = False
            for i in range(m):
                min_dis = sys.maxsize
                min_idx = -1
                for j in range(k):
                    dis_ji = self.distance(centroids[j,:],data[i,:])
                    if dis_ji < min_dis:
                        min_dis = dis_ji
                        min_idx = j
                if assignment_mat[i,0] != min_idx:
                    flag = True
                assignment_mat[i,:] = min_idx,min_dis**2
            for cent in range(k):
                point_in_cluster = []
                for l in range(m):
                    if assignment_mat[j,0] == cent:
                        point_in_cluster.append(data[j].tolist()[0])
                point_in_cluster = np.mat(point_in_cluster)
                centroids = np.mean(point_in_cluster, axis= 0)
        return centroids, assignment_mat


