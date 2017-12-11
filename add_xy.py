#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

fr = open("input.csv", 'r')
fw = open("inputxy.csv", 'a')
length = 281
width = 174
x = 0
y = 0
for line in fr:

    if x == length:
        y += 1
        x = 0
        count = 0
    # print line.rstrip()+','+str(y)+','+str(x)+'\n',
    fw.write(line.rstrip()+','+str(y)+','+str(x)+'\n')
    x += 1
fw.flush()
fw.close()
fr.close()