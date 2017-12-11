#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import math
import sys
from PIL import Image


class dir_mapping(object):
    def distance(self,v1,v2):
        count = float(0)
        for j in range(len(v1)):
            count += (v1[j]-v2[j])*(v1[j]-v2[j])
        return math.sqrt(count)

    def run(self):
        data = []
        grey_num = 32
        color_num = 32
        for j in range(grey_num):
            data.append([])
            for k in range(color_num):
                data[j].append(0)

        fg = open("gray32_idx.csv", 'r')
        fc = open("rgb32_idx.csv", 'r')
        pair_list = []
        for i in range(48894):
            line1 = fg.readline()
            line2 = fc.readline()
            pair_list.append((int(line1.rstrip())-1, int(line2.rstrip())-1))
        fg.close()
        fc.close()
        for pair in pair_list:
            # print pair
            data[pair[0]][pair[1]] += 1

        # print data

        mapping = []
        for j in range(grey_num):
            mapping.append(0)
        for j in range(grey_num):
            max = 0
            index = 0
            for k in range(color_num):
                if data[j][k] > max:
                    max = data[j][k]
                    index = k
            mapping[j] = index

        print mapping

        fdata = open("data.csv", 'r')
        fclass = open("gray32_C.csv", 'r')
        fw = open("data32.csv", 'a')
        fcolor = open("rgb32_C.csv", 'r')
        color_class2color = []
        for line in fcolor:
            data = line.rstrip().split(',')
            t = []
            for d in data:
                t.append(int(float(d) + 0.5))
            color_class2color.append(t)

        class_list = []
        for line in fclass:
            data = line.rstrip().split(',')
            v = []
            for num in data:
                v.append(int(num))
            class_list.append(v)

        result = []
        for line in fdata:
            data = line.rstrip().split(',')
            v = []
            for num in data:
                v.append(int(num))
            min = float(-1)
            index = 0
            for j in range(len(class_list)):
                dis = self.distance(v, class_list[j])
                if min == -1:
                    min = dis
                    index = j
                elif min > dis:
                    min = dis
                    index = j
            # print index+1
            # fw.write(str(index+1)+'\n')
            color_class = mapping[index]
            color = color_class2color[color_class]
            result.append(color)

        length = 641
        width = 361
        img = Image.new("RGBA", (length, width), (0, 0, 0))
        x = 0
        y = 0
        for line in result:

            if x == length:
                y += 1
                x = 0
                count = 0
            # print x,y
            img.putpixel((x, y), (int(line[0]), int(line[1]), int(line[2])))
            x += 1
        # rows, cols, dims = img.shape
        img.show()

        fw.flush()
        fw.close()
        fdata.close()
        fclass.close()




if __name__ == '__main__':
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    dir_mapping = dir_mapping()
    dir_mapping.run()












# class mapping(object):
#     def __init__(self, r_input, r_output):
#         self.mapping = dict()
#         f_r_input = open("input.csv",'r')
#         f_r_output = open("color.csv", 'r')
#         for line in f_r_input:
#             r_line = f_r_output.readline()
#             data_in = line.rstrip().split(',')
#             r_line = r_line.rstrip()
#             key =
#             for
#             key =
#             if
#
#     def h


