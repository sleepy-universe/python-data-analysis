# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:07:34 2023

@author: mo
"""
from matplotlib.font_manager import FontProperties
path = "C:\\Users\\modey\\.spyder-py3\\week5_word2vec\\week5_TextAnalyzer.py"
fileaddress = 'C:\\Users\\modey\\Desktop\\python数据分析\\weibo.txt'
Heiti = FontProperties(fname='C:/WINDOWS/Fonts/SIMHEI.TTF')
model_name = "word2vec.model"
stopaddress="C:\\Users\\modey\\Desktop\\python数据分析\\stop_words.txt"
keyword = '春天'
from week5_TextAnalyzer import TextAnalyzer
my = TextAnalyzer(fileaddress, 300, 5, 1, [], model_name, Heiti, stopaddress, keyword)
#my.set_corpus()
#my.correlation()#训练得以的word2vec模型来推断相似词汇
#my.save_model()#保存
my.load_model1()#加载
my.correlation1()#预训练模型推断相似词汇
#my.t_sne()# 使用t-SNE算法对词向量进行降维
#my.visualization()#可视化降维后的词向量'''