# coding=utf-8
from PIL import Image, ImageOps

'''
    1. pip install PIL
    2. PIL(Python Imaging Library)这是Python下非常强大的处理图像的工具库
'''
im = Image.open('image2016-5-27 10-18-3.png')
print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')