# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:16:57 2023

@author: modey
"""
import os
import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import ImageFilter
import functools
image="C:\\Users\\modey\\Desktop\\suop.png"
#image=Image.open("C:\\Users\\modey\\Desktop\\suop.png")
path="C:\\Users\\modey\\Desktop\\img"
class pretreatment:
    def __init__(self,image):
        self._image=image
    def __call__(self,filter):
        @functools.wraps(filter)
        def wrapper(image,path):
            img = cv.imread(self._image)
            height, width, channels = img.shape
            print(f'{height},{width},{channels}')#图像的大小
            hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)#将图像颜色空间转换为HSV格式
            avgh, avgs, avgv = cv.mean(hsv)[:-1]#计算h，s，v的平均值
            print('亮度v:',avgv,'饱和度s:',avgs)#亮度v和饱和度s
            return filter(image,path)
        return wrapper
#装饰器函数，判断文件夹地址是否存在，若不存在则系统自动新建一个
def log(path):
    def path_check(filter):
        def wrapper(self):
            if not os.path.exists(path):
                print("The path of file does not exist.")
                os.makedirs(path)
            return filter(self)
        return wrapper
    return path_check

@pretreatment("C:\\Users\\modey\\Desktop\\suop.png")
class filter:
    def __init__(self, image,path):
        self._image = image
        self._path = path
        
    def load(self):
        self._image = Image.open(self._image)
        return self._image
    #灰度化处理
    @log(path)
    def convert(self):
        new_image = self._image.convert('L')
        new_image.save(path+'\\' + '1.jpg')
        new_image.show()
           
    #裁剪,其中参数代表(left, upper, right, lower)
    def crop(self):
        region = self._image.crop((10, 10, 1000, 1000))#裁剪图片
        region.show()
        region.save=(self._path+'\\'+'2.jpg')
    #旋转
    def resolve(self):
        angle = 45 #逆时针
        rotate = self._image.rotate(angle)#旋转
        rotate.show()
        rotate.save(self._path+'\\'+'3.jpg')
    #缩放        
    def resize(self):
        resize = self._image.resize((128,128))
        resize.show()
        resize.save(self._path+'\\'+'4.jpg')

    #模糊,处理之后的图像会整体变得模糊
    def blur(self):
        blur = self._image.filter(ImageFilter.BLUR) 
        blur.show()
        blur.save(self._path+'\\'+'5.jpg')
        
        #边缘提取,找轮廓，将图像中的轮廓信息全部提取出来。
    def sharpen(self):
        #锐化滤波，补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰。
        sharpen = self._image.filter(ImageFilter.SHARPEN)
        #为深度边缘增强滤波，会使得图像中边缘部分更加明显
        eem = sharpen.filter(ImageFilter.EDGE_ENHANCE_MORE)
        #提取轮廓
        con = eem.filter(ImageFilter.CONTOUR)
        con.show()
        con.save(self._path+'\\'+'6.jpg')

c=filter(image,path)
c.load()
c.convert()