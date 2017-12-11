#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import math
import sys
from PIL import Image


class color(object):

    def run(self):
        fdata = open("recover5.csv", 'r')
        fcolor = open("rgb32_C.csv", 'r')
        color_class2color = []
        for line in fcolor:
            data = line.rstrip().split(',')
            t = []
            for d in data:
                t.append(int(float(d) + 0.5))
            color_class2color.append(t)

        result = []
        for line in fdata:
            data = line.rstrip()

            c = color_class2color[(int(data)-1) % 32]
            result.append(c)

        # length = 641
        # width = 361

        length = 281
        width = 174
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

        fdata.close()


if __name__ == '__main__':
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    color = color()
    color.run()



