#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

f1 = open('data.csv', 'r')
size = 231401
length = 641
width = (int)(size/length + 1)
img = Image.new("L", (length,width))
x = 0
y = 0
for line in f1:
    data = line.strip().split(',')

    if x == length:
        y += 1
        x = 0
        count = 0
    # print x,y
    img.putpixel((x, y), int(data[4]))
    x += 1
# rows, cols, dims = img.shape
img.show()
# img.save('data.png',"PNG")
# rows, cols = length, width
# plt.figure("beauty")
# plt.imshow(img)
# plt.axis('off')
# plt.show()
f1.close()

# --------------------------------------
f1 = open('input.csv', 'r')

size = 48894
length = 281
width = (int)(size/length + 1)
img = Image.new("L", (length,width))
x = 0
y = 0
for line in f1:
    data = line.strip().split(',')

    if x == length:
        y += 1
        x = 0
        count = 0
    # print x,y
    img.putpixel((x, y), int(data[4]))
    x += 1
# rows, cols, dims = img.shape
img.show()
# rows, cols = length, width
# plt.figure("beauty")
# plt.imshow(img)
# plt.axis('off')
# plt.show()
f1.close()
# --------------------------------------
#
f1 = open('color.csv', 'r')

size = 48894
length = 281
width = (int)(size/length + 1)
img = Image.new("RGBA", (length,width), (0,0,0))
x = 0
y = 0
for line in f1:
    data = line.strip().split(',')

    if x == length:
        y += 1
        x = 0
        count = 0
    # print x,y
    img.putpixel((x, y), (int(data[0]), int(data[1]), int(data[2])))
    x += 1
# rows, cols, dims = img.shape
plt.figure("beauty")
plt.imshow(img)
plt.axis('off')
plt.show()
f1.close()



# 随机生成5000个椒盐
# img = np.array(Image.open('1327.jpg'))
# rows, cols, dims = img.shape
# for i in range(5000):
#     x = np.random.randint(0, rows)
#     y = np.random.randint(0, cols)
#     img[x, y, :] = 255
#
# plt.figure("beauty")
# plt.imshow(img)
# plt.axis('off')
# plt.show()
