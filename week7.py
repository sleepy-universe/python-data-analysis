# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:27:56 2023

@author: modey
"""
from PIL import Image
import os
import cv2
import numpy as np
import scipy.stats
im = "C:\\Users\\modey\\Desktop\\cunzi.png"
im1 = Image.open("C:\\Users\\modey\\Desktop\\mjj和crt_1.jpg")
im2 = Image.open("C:\\Users\\modey\\Desktop\\mjj和crt_1.jpg")
class ImageQueryError(Exception):
	def __init__(self,image):
		self._image=image       
class File_NotFoundError(ImageQueryError):
    def __init__(self,image):
        self._image=image
        self._message='No such file or directory: {}'.format(self._image)
        
class UnidentifiedImageError(ImageQueryError):
    def __init__(self, image):
        self._image=image
        self._message='Unable to open and recognize images: {}'.format(self._image)

class ImageQueryShapeNotMatchError(ImageQueryError):
    def __init__(self, image1,image2):
        self._image1=image1
        self._image2=image2
        self._message='The height{} and width{} of image1 do not match The height{} and width{} of image2'.format(image1.height , image1.width,
        image2.height,image2.width)
class ImageQuery:
    def __init__(self,image,image1,image2):
        self._image = image
        self._image1 = image1
        self._image2 = image2
    def _create_and_image(self):
        try:
            if not  (os.path.exists(self._image)):
                raise File_NotFoundError(self._image)
            if not (cv2.imread(self._image,-1)):
                raise UnidentifiedImageError(self._image)            
        except File_NotFoundError as error1:
            print(error1._message)
        except UnidentifiedImageError as error2:
            print(error2._message)
        else:
            print('successfully opened and identified')
    def pixel_difference(self):
        pixel1=[]
        pixel2=[]
        similarity=0
        try:
            if(self._image1.height!=self._image2.height)or(self._image1.width
                                                           !=self._image2.width):
                raise ImageQueryShapeNotMatchError(self._image1,self._image2)
        except ImageQueryShapeNotMatchError as error3:
            print(error3._message)
        else:
            print('The two images are successfully matched')
            '''如果不使用.convert('RGB')进行转换的话，读出来的图像是RGBA四通道的，
            A通道为透明通道，该对深度学习模型训练来说暂时用不到，
            因此使用convert('RGB')进行通道转换。'''
            rgb_image1 = self._image1.convert('RGB')
            for i in range(self._image1.height):
                for j in range(self._image1.width):
                    lis1 = tuple(rgb_image1.getpixel((i, j)))#r,g,b
                    pixel1.append(lis1)
            rgb_image2 = self._image2.convert('RGB')
            for i in range(self._image2.height):
                for j in range(self._image2.width):
                    lis2 = tuple(rgb_image2.getpixel((i, j)))#r,g,b
                    pixel2.append(lis2)
            for k in range(len(pixel2)):
                for n in range(3):
                    s=abs(pixel1[k][n]-pixel2[k][n])
                    similarity+=s
            similarity = similarity/(3*len(pixel1))
        print(similarity)
    def pixel_difference_new(self):
        zhifangtu1 = self._image1.histogram()
        zhifangtu2 = self._image2.histogram()
        print(scipy.stats.spearmanr(zhifangtu1, zhifangtu2))
        print(scipy.stats.pearsonr(zhifangtu1, zhifangtu2))
        
c = ImageQuery(im,im1,im2)
c._create_and_image()   
c.pixel_difference_new()         




            
            
            
        
        
        
        

