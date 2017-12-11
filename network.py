#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import random
import copy
import sys
import time
import math


class network(object):
    # number of input and number of output
    # init level of layer and size of layer
    def __init__(self, input, output, level, size):
        if input <1 or output<1 or level<1 or size<1:
            print input, output, level, size, "error"
            return
        self.input = input
        self.output = output
        self.level = level
        self.size = size
        self.rate = 0.01
        # ---------------------weight----------------------
        self.layer_weight = []
        # self.layer_weight.append([])
        # input * size
        self.layer_weight.append([])
        for k in range(self.size):
            self.layer_weight[0].append([])
            for j in range(self.input):
                self.layer_weight[0][k].append(float(0))

        self.output_weight = []
        # output * size
        for k in range(self.output):
            self.output_weight.append([])
            for j in range(self.size):
                self.output_weight[k].append(float(0))

        # self.layer_weight = []
        # level-1 * size
        for k in range(1, self.level):
            self.layer_weight.append([])
            for j in range(self.size):
                self.layer_weight[k].append([])
                for l in range(self.size):
                    self.layer_weight[k][j].append(float(0))

        # ---------------------data----------------------
        self.input_data = []
        for k in range(self.input):
            self.input_data.append(float(0))

        self.hidden_node_data = []
        for k in range(self.level):
            self.hidden_node_data.append([])
            for j in range(self.size):
                self.hidden_node_data[k].append(float(0))

        self.output_data = []
        for k in range(self.output):
            self.output_data.append(float(0))

        # ---------------------data_in----------------------
        self.input_data_in = []
        for k in range(self.input):
            self.input_data_in.append(float(0))

        self.hidden_node_data_in = []
        for k in range(self.level):
            self.hidden_node_data_in.append([])
            for j in range(self.size):
                self.hidden_node_data_in[k].append(float(0))

        self.output_data_in = []
        for k in range(self.output):
            self.output_data_in.append(float(0))

        # ---------------------error----------------------

        self.hidden_node_error = []
        for k in range(self.level):
            self.hidden_node_error.append([])
            for j in range(self.size):
                self.hidden_node_error[k].append(float(0))

        self.output_error = []
        for k in range(self.output):
            self.output_error.append(float(0))

    def update_network(self, data_in, data_ans):
        y = self.run_network(data_in)
        for j in range(len(self.output_error)):
            self.output_error[j] = data_ans[j] - y[j]

        for k in range(self.output):
            for j in range(self.size):
                self.output_weight[k][j] += self.rate * self.output_error[k] * \
                                           self.g_d(self.output_data_in[k]) * data_ans[k]

        print self.layer_weight
        for k in range(self.level-1, 0, -1):
            for j in range(self.size):
                if k == (self.level-1):
                    # last layer
                    count = float(0)
                    for x in range(len(self.output_error)):
                        count += self.output_weight[x][j] * (data_ans[x] - y[x])
                    self.hidden_node_error[k][j] = count
                else:
                    # mid layer
                    count = float(0)
                    for x in range(len(self.layer_weight[k+1])):
                        # self.layer_weight[layer_num][num][pre_num]
                        count += self.layer_weight[k+1][x][j] * self.hidden_node_error[k+1][x]
                    self.hidden_node_error[k][j] = count

                for l in range(self.size):
                    self.layer_weight[k][j][l] += self.rate * self.hidden_node_error[k][j] * \
                                           self.g_d(self.hidden_node_data_in[k][j]) * self.hidden_node_data[k][j]
        print self.layer_weight
        k = 0
        for j in range(self.size):

            count = float(0)
            for x in range(len(self.layer_weight[k + 1])):
                # self.layer_weight[layer_num][num][pre_num]
                count += self.layer_weight[k + 1][x][j] * self.hidden_node_error[k + 1][x]
            self.hidden_node_error[k][j] = count
            self.layer_weight[k][j][0] += self.rate * self.hidden_node_error[k][j] * self.g_d(self.hidden_node_data_in[k][j]) * self.hidden_node_data[k][j]

        # ------------------------clean up------------------------
        # TODO
        print self.layer_weight
        print self.output_weight

    def save_network(self):
        time_string = time.strftime('%Y-%m-%d%X', time.localtime(time.time()))
        f = open("network"+time_string+".csv", 'w')
        f.write(str(self.input)+','+str(self.output)+','+str(self.level)+','+str(self.size)+'\n')
        for level in self.layer_weight:
            for neural in level:
                line = ""
                for weight in neural:
                    line += str(weight)+','
                line = line[0:-1] + '\n'
                print line,
                f.write(line)
        for neural in self.output_weight:
            line = ""
            for weight in neural:
                line += str(weight) + ','
            line = line[0:-1] + '\n'
            print line,
            f.write(line)
        f.flush()
        f.close()

    def load_network(self, file_name):
        f = open(file_name, 'r')
        line = f.readline()
        for level in self.layer_weight:
            for neural in level:
                line = f.readline()
                if not line:
                    print "error read file"
                    return
                weight_data = line.rstrip().lstrip().split(",")
                for j in range(len(neural)):
                    neural[j] = float(weight_data[j])

        for neural in self.output_weight:
            line = f.readline()
            if not line:
                print "error read file"
                return
            weight_data = line.rstrip().lstrip().split(",")
            for j in range(len(neural)):
                neural[j] = float(weight_data[j])
        f.close()

    def random_network(self):
        for k in range(self.output):
            for j in range(self.size):
                self.output_weight[k][j] = random.random()
        print self.output_weight
        for k in range(self.size):
            for j in range(self.input):
                self.layer_weight[0][k][j] = random.random()

        for k in range(1, self.level):
            for j in range(self.size):
                for l in range(self.size):
                    self.layer_weight[k][j][l] = random.random()
        print self.layer_weight

    def init_network(self):
        for k in range(self.output):
            for j in range(self.size):
                self.output_weight[k][j] = float(1)
        print self.output_weight
        for k in range(self.size):
            for j in range(self.input):
                self.layer_weight[0][k][j] = float(1)

        for k in range(1, self.level):
            for j in range(self.size):
                for l in range(self.size):
                    self.layer_weight[k][j][l] = float(1)
        print self.layer_weight

    def g(self, input_data):
        # def sigmoid(x):
        # return 1 / (1 + math.exp(-input_data))
        # do some thing
        if input_data < 0:
            return float(0.2)*input_data
        else:
            return input_data

    def g_d(self, input_data):
        # tmp = self.g(input_data)
        # return tmp*(1-tmp)
        # do some thing
        if input_data < 0:
            return float(0.2)
        else:
            return float(1)

    def run_node(self, layer_num, num):
        if layer_num == self.level:
            # is output layer
            input_weight = self.output_weight[num]
            input_sum = float(0)
            previous_layer_data = self.hidden_node_data[layer_num-1]
            for j in range(self.size):
                input_sum += input_weight[j] * previous_layer_data[j]
            output_data = self.g(input_sum)
            self.output_data_in[num] = input_sum
            self.output_data[num] = output_data

        elif layer_num == 0:
            # is first hidden layer
            input_weight = self.layer_weight[layer_num][num]
            input_sum = float(0)
            previous_layer_data = self.input_data
            for j in range(self.input):
                input_sum += input_weight[j] * previous_layer_data[j]
            output_data = self.g(input_sum)
            self.hidden_node_data[0][num] = output_data
            self.hidden_node_data_in[0][num] = input_sum

        else:
            # is hidden layer
            input_weight = self.layer_weight[layer_num][num]
            input_sum = float(0)
            previous_layer_data = self.hidden_node_data[layer_num-1]
            for j in range(self.size):
                input_sum += input_weight[j] * previous_layer_data[j]
            output_data = self.g(input_sum)
            self.hidden_node_data[layer_num][num] = output_data
            self.hidden_node_data_in[layer_num][num] = input_sum

    def run_network(self, input_data):
        for j in range(len(self.input_data)):
            self.input_data[j] = input_data[j]
        # run hidden layer
        for x in range(self.level):
            for y in range(self.size):
                # print x,y
                self.run_node(x,y)
        x = self.level
        for y in range(self.output):
            # print x, y
            self.run_node(x, y)

        # print self.hidden_node_data

        return copy.copy(self.output_data)


if __name__ == '__main__':
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]

    network = network(1, 1, 2, 2)
    # network.load_network("network2017-12-1012:14:10.csv")
    network.random_network()
    # network.init_network()
    r = network.run_network([float(1)])
    print "1 ", r
    r = network.run_network([float(2)])
    print "2 ", r
    # r = network.run_network([float(0.75)])
    # print "3 ", r
    # r = network.run_network([float(1)])
    # print "4 ", r
    for i in range(100):
        network.update_network((float(1),), (float(2),))
        network.update_network((float(2),), (float(1),))
        # network.update_network((float(0.50),), (float(0.50),))
        # network.update_network((float(0.75),), (float(0.50),))
        # network.update_network((float(1),), (float(0.75),))
        r = network.run_network([float(1)])
        print "1 ", r
        r = network.run_network([float(2)])
        print "2 ", r
        # r = network.run_network([float(0.75)])
        # print "3 ", r
        # r = network.run_network([float(1)])
        # print "4 ", r

    # network.save_network()
    # network.random_network()
    #
    # network.save_network()
    #
    # r = network.run_network([1])
    # print r
    # r = network.run_network([2])
    # print r
    # r = network.run_network([3])
    # print r
    # r = network.run_network([4])
    # print r













