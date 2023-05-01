# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:24:16 2023

@author: mo
"""
from PIL import Image
from PIL import ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import os
im = Image.open("C:\\Users\\modey\\Desktop\\puppy.png")
path = "C:\\Users\\modey\\Desktop\\image"# 图片集地址
picture_format = '.png'  # 图片格式
outpath = "C:\\Users\\modey\\Desktop\\output"#输出地址

class ImageProcessor:
    def __init__ (self,image,*parameter_lis):
        self._image = image
        self._parameter_lis = parameter_lis
    def process(self):
        """
        能够对Image实例的特定处理，在子类中具体实现
        """
        pass
    
#灰度化处理
class Convert(ImageProcessor):
    def __init__(self, image, *parameter_lis):
        ImageProcessor.__init__(self,image,*parameter_lis)
    def process(self):
        new_image = self._image.convert('L')
        return new_image
        '''new_image.show()
        new_image.save(self._parameter_lis[1])'''
           
#裁剪,其中参数代表(left, upper, right, lower)
class Crop(ImageProcessor):
    def __init__(self, image, *parameter_lis):
        ImageProcessor.__init__(self,image,*parameter_lis)
    def process(self):
        region = self._image.crop((10, 10, 1000, 1000))#裁剪图片
        return region
        '''region.show()
        region.save(self._parameter_lis[4])'''
        
#缩放        
class Resize(ImageProcessor):
    def __init__(self, image, *parameter_lis):
        ImageProcessor.__init__(self,image,*parameter_lis)
    def process(self):
        resize = self._image.resize((128,128))
        return resize
        '''resize.show()
        resize.save(self._parameter_lis[2])'''

#模糊,处理之后的图像会整体变得模糊
class Obscure(ImageProcessor):
    def __init__(self, image, *parameter_lis):
        ImageProcessor.__init__(self,image,*parameter_lis)
    def process(self):
        blur = self._image.filter(ImageFilter.BLUR) 
        return blur
        '''blur.show()
        blur.save(self._parameter_lis[0])'''
        
#边缘提取,找轮廓，将图像中的轮廓信息全部提取出来。
class Extraction(ImageProcessor):
    def __init__(self, image, *parameter_lis):
        ImageProcessor.__init__(self,image,*parameter_lis)
    def process(self):
        #锐化滤波，补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰。
        sharpen = self._image.filter(ImageFilter.SHARPEN)
        #为深度边缘增强滤波，会使得图像中边缘部分更加明显
        eem = sharpen.filter(ImageFilter.EDGE_ENHANCE_MORE)
        #提取轮廓
        con = eem.filter(ImageFilter.CONTOUR)
        return con
        '''con.show()
        con.save(self._parameter_lis[0])'''

class ImageShop:
    def __init__(self,image_format,file_catalog,image_lis,processed_image):
        self._image_format  = image_format
        self._file_catalog  = file_catalog
        self._image_lis = image_lis
        self._processed_image = processed_image
    def load_images(self):
            imagelist = os.listdir(self._file_catalog)
            return imagelist
    def set_processed_image(self):
            imagelis=ImageShop.load_images(self)
            for file in imagelis:
                if file.endswith(self._image_format):  # 如果file以png结尾
                    # 图片路径
                    im_address=(self._file_catalog + '\\' + file)
                    self._image_lis.append(im_address)
                    im1 = Image.open(im_address)
                    self._processed_image.append(im1)
            return self._processed_image
        
        #内部类的实现
    def __batch_ps(self,processor):
            image_lis = self._processed_image
            #对图片进行批量处理
            for i in range(len(image_lis)):
                #对图片进行某种处理
                #产生一个某种图片处理操作的实例
                s = processor(image_lis[i])
                processed_im = s.process()
                #processed_im.show()
                self._processed_image[i]=processed_im
            #self._image_lis = self._processed_image#更新处理过的图片
        #外部类的实现
    def batch_ps(self,*parameter):
        for j in parameter:
            if 'convert' in j:
                self.__batch_ps(Convert)
            if 'crop' in j:
                self.__batch_ps(Crop)
            if 'resize' in j:
                self._batch_ps(Resize)
            if 'obscure' in j:
                self.__batch_ps(Obscure)
            if 'extraction' in j:
                self.__batch_ps(Extraction)
                    
    def display(self,nrow=2, ncols=3,max_num=50):
        n = len(self._image_lis)
        for i in range(n): # 控制每张子图展示图片数
            img = self._processed_image[i]
            plt.subplot(nrow, ncols, i+1)
            plt.imshow(img,cmap="gray")
        plt.show()
                
    def save(self, path1):
        for i in range(len(self._image_lis)):
            img = self._processed_image[i]
            img.save(path1+str(i+1)+self._image_format)
            
            
class TestImageShop:
    def __init__(self,image_format,file_catalog,image_lis,processed_image):
        self._image_format  = image_format
        self._file_catalog  = file_catalog
        self._image_lis = image_lis
        self._processed_image = processed_image
    def set_self_test(self):
        self._test = ImageShop(self._image_format,self._file_catalog,self._image_lis,
                               self._processed_image)
        return self._test
    def test_imageshop(self, *parameter):
        self._test.load_images()
        self._test.set_processed_image()
        self._test.batch_ps(parameter)
        self._test.display()
        self._test.save(outpath)
    
   
'''
pro1 = Convert(im,('L'))
pro1.process()
pro2 = Crop(im,(10, 10, 800, 800))
pro2.process()
pro3 = Resize(im,(128, 128))
pro3.process()
pro4 = Obscure(im)
pro4.process()
pro5 = Extraction(im)
pro5.process()'''

result = TestImageShop(picture_format,path,[],[])
result.set_self_test()
result.test_imageshop('convert','crop')





