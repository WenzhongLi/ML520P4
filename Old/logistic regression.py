#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Tan
'''
import copy
from numpy import *


def get_data():
    X = [[1,2,5,4,3,4,5,6,7],[2,2,6,3,5,8,12,14,17],[3,4,6,7,10,14,19,22,32],[4,6,7,9,12,2,5,32,42],[5,10,11,13,15,15,12,13,17]]
    Y = []
    for xi in X:
        Y.append(2*xi[4])
    print Y
    return X, Y

def sigmoid(z):
    t = exp(z)
    t = t/(t+1)
    return t

# vectorize
sigmoid_vec = vectorize(sigmoid)

#  descent
def descentgrad(X, Y):
    X = mat(X)
    Y = mat(Y)
    r, c = shape(X)
    a = 0.30
    repeat = 1000

    W = ones((1, c))
    V = zeros((r, r), float32)

    for k in range(repeat):
        Q = sigmoid_vec(W*X.transpose())
        for i in range(r):
            V[i, i] = Q[0, i]*(Q[0,i] - 1)
        W = W - a * (Y - Q)*V*X
    return W



if __name__ == "__main__":
    X, Y = get_data()
    print X
    print Y
    X, Y = get_data()
    W = descentgrad(X, Y)
    print W
