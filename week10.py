# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:50:51 2023
@author: mo
"""
import math
import os
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from abc import ABCMeta, abstractmethod
import numpy as np
import random
import librosa
import jieba
import collections
import librosa.display
from mpl_toolkits.mplot3d import Axes3D
text="C:\\Users\\modey\\Desktop\\网易云评论.txt"
im="C:\\Users\\modey\\Desktop\\python数据分析\\Aaron_Peirsol"
music='C:\\CloudMusic\\沈以诚 - 水瓶.mp3'

class Plotter(metaclass=ABCMeta):
    def __init__(self,data,*args,**kwargs):
        self._data=data
        self._args=args
        self._kwargs=kwargs
    @abstractmethod
    def plot(self):
        pass
    
#数据点类Point  
class Point(object):
    def __init__(self,xParam = 0.0,yParam = 0.0):
        self.x = xParam
        self.y = yParam
 
    def __tuple__(self):
        return (self.x ,self.y)
    
#数据点型数据绘制   
class PointPlotter(Plotter):
    def __init__(self, data,*args,**kwargs):
        super().__init__(data,*args,**kwargs)
    def plot(self):
        xpoints=[]
        ypoints=[]
        for i in range(len(self._data)):
            xpoints.append(self._data[i][0])
            ypoints.append(self._data[i][1])
        x=np.array(xpoints)
        y=np.array(ypoints)
        plt.plot(x,y)
        plt.show()
        
#多维数组型数据的绘制       
class ArrayPlotter(Plotter):
    def __init__(self,data,*args,**kwargs):
        super().__init__(data,*args,**kwargs)
    def plot(self):
        #定义图像和三维格式坐标轴
        fig=plt.figure()
        ax1 = Axes3D(fig)
        ax1.scatter3D(self._data[0],self._data[1],self._data[2], cmap='Blues')  #绘制散点图
        ax1.plot3D(self._data[0],self._data[1],self._data[2],'gray')    #绘制空间曲线
        #plt.plot(self._data[0],self._data[1])
        plt.show()
        
#文本型数据的绘制
class TextPlotter(Plotter):
    def __init__(self,data,*args,**kwargs):
        super().__init__(data,*args,**kwargs)
    def plot(self):
        #用jieba分词
        new_document=[]
        for line in self._data:
            new_line=jieba.cut(line,cut_all=False,HMM=True)#使用精确模式对文本分词
            new_document.extend(new_line)
        #创建停用词
        stopwords = [line.strip() for line in open("C:\\Users\\modey\\Desktop\\python数据分析\\stop_words.txt",encoding='UTF-8').readlines()]
        #停用词过滤
        new_document1=[]
        for word in new_document:
            if word not in stopwords:#过滤“噪音”
                new_document1.append(word)#将过滤后的词语存入新的列表
        #统计词频
        word_frequency={}
        for word in new_document1:
            count=word_frequency.get(word,0)#使用字典进行词频统计
            word_frequency[word]=count+1
        #将统计词频后的字典变为有序字典
        sorted_freq = collections.OrderedDict(sorted(word_frequency.items(),key=lambda dc:dc[1],reverse=True))
        words = list(sorted_freq.keys())
        #将词频前50的词语构成的词频字典单独抽取出来以制作词云图
        sorted_freq_50={}
        for i in words[0:50]:
            sorted_freq_50[i]=sorted_freq[i]
        #制作词云图
        w = WordCloud(font_path='msyh.ttc',background_color='white', width=4000, 
                        height=2000, margin=10, 
                        max_words=200).fit_words(sorted_freq_50) #mysh.ttc微软雅黑
        plt.imshow(w)
        plt.show()
        w.to_file("C:\\Users\\modey\\Desktop\\词云图.png")
        
#图片型数据的绘制
class ImagePlotter(Plotter):
    def __init__(self,data,*args,**kwargs):
        super().__init__(data,*args,**kwargs)
    def plot(self):
        n=0
        lis=[]
        for filename in os.listdir(self._data):
            n+=1
            im_address=os.path.join(self._data,filename)
            pic = Image.open(im_address)
            lis.append(pic)
        for i in range(n):
            plt.subplot(math.ceil(n/3),3,i+1)
            plt.imshow(lis[i])
            
#声音数据的绘制      
class MusickPlotter(Plotter):
    def __init__(self,data,*args,**kwargs):
        super().__init__(data,*args,**kwargs)
    def plot(self):
        y, sr = librosa.load(self._data,sr=44100)
        print(f'sampling rate:{sr}')
        print(f'sound time series shape:{y.shape}')
        print(librosa.get_duration(y=y,sr=sr))#音频的长度190秒
        #绘制波形图
        librosa.display.waveshow(y, sr=sr, x_axis='time', offset=0.0, ax=None)
        #①线性频率能谱图
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        img = librosa.display.specshow(D, y_axis='linear', x_axis='time', sr=sr, ax=ax[0],cmap='Greens')
        ax[0].set(title='Linear-frequency power spectrogram')
        ax[0].label_outer()
        
        #②对数频率能谱图
        hop_length = 1024
        D2 = librosa.amplitude_to_db(np.abs(librosa.stft(y, hop_length=hop_length)), ref=np.max)
        librosa.display.specshow(D2, y_axis='log', sr=sr, hop_length=hop_length, x_axis='time', ax=ax[1],cmap='Greens')
        ax[1].set(title='Log-frequency power spectrogram')
        ax[1].label_outer()
        fig.colorbar(img, ax=ax, format="%+2.f dB")
        plt.show()
        plt.close()
        
def main():
    '''#数据点型数据输入
    lis1=[]
    for i in range(10):
        #利用random函数生成随机数，并且每一组随机数是Point类的一个实例
        po = Point(random.random(),random.random())
        element=po.__tuple__()
        lis1.append(element)
    p = PointPlotter(lis1)
    p.plot()
    
    #多维数组型数据输入
    x1=[]
    y1=[]
    z1=[]
    s=[]
    for i in range(10):
        x1.append(random.random())#生成三组随机数
        y1.append(random.random())
        z1.append(random.random())
    s.append(x1)
    s.append(y1)
    s.append(z1)
    ap = ArrayPlotter(s)
    ap.plot()
    
    #文本型数据输入
    document=[]
    #读入
    with open(text,"r",encoding='utf-8') as f:
        line=f.readlines()
        for i in line:
            document.append(i)#将文本内容逐行存入一个列表
    tp=TextPlotter(document)
    tp.plot()
    
    #图片型数据输入
    ip = ImagePlotter(im)
    ip.plot()'''
    
    #声音型数据输入
    mp=MusickPlotter(music)
    mp.plot()
    
if __name__ == '__main__':
    main()

    
    
    
        