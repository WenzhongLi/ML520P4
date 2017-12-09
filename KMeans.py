# coding : utf-8
#author : GE
import numpy as np
import random

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
        flag = True
