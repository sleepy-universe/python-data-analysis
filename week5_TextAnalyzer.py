# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 10:44:28 2023

@author: mo
"""
import jieba
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
n=10000
path = "C:\\Users\\modey\\Downloads\\python5-pre-trained-weibo-word2vec\\python5-pre-trained-weibo-word2vec\\weibo_59g_embedding_200.model"
class TextAnalyzer:
    #初始化类的属性
    def __init__(self,fileaddress,size,window,min_count,sentense,model_name,font,stopaddress,keyword):
        self._fileaddress=fileaddress
        self._size=size
        self._window=window
        self._min_count=min_count
        self._sentense=sentense
        self._modelname=model_name
        self._font=font
        self._stopaddress=stopaddress
        self._keyword=keyword
        
    #预处理,定义语料库
    def set_corpus(self):
        #创建停用词
        stopset = [line.strip() for line in open(self._stopaddress,encoding='UTF-8').
                   readlines()]
        with open(self._fileaddress,'r',encoding='utf-8') as f:
            for line in f:
                sen = [w for w in jieba.cut(line.strip().split('\t')[1]) if w 
                       not in stopset]
                #print(sen)
                self._sentense.append(sen)
        print(f'load {len(self._sentense)} tweets...')
        return self._sentense
    
    #Word2Vec模型的建立
    def set_word2vec(self):
        model = Word2Vec(self._sentense, size=self._size, window=self._window,
                         min_count=self._min_count)
        return model
    
    # 获取最相关的10个词和最不相关的10个词
    def correlation(self):
        model = TextAnalyzer.set_word2vec(self)
        most_similar = model.wv.most_similar(self._keyword, topn=10)
        least_similar = model.wv.most_similar(negative=[self._keyword], topn=10)
        '''print("最相似:\n",most_similar)
        print("最不相似:\n",least_similar)'''

    # 模型的保存
    def save_model(self):
        model = TextAnalyzer.set_word2vec(self)
        model.save(self._modelname)
    #预训练模型的加载
    def load_model(self):
        model = Word2Vec.load(self._modelname)
        return model
    #weibo_59g_embedding_200. model预训练模型
    def load_model1(self):
        model1 = Word2Vec.load(path)
        return model1
    
    # 再次获取最相关的10个词和最不相关的10个词
    def correlation1(self):
        model = TextAnalyzer.load_model(self)
        #model = TextAnalyzer.load_model1(self)
        most_similar = model.wv.most_similar(self._keyword, topn=10)
        least_similar = model.wv.most_similar(negative=[self._keyword], topn=10)
        print("最相似:\n",most_similar)
        print("最不相似:\n",least_similar)
        return most_similar,least_similar
    
    def merge(self):
    # 将最相关和最不相关的词汇向量合并为一个数组
        model = TextAnalyzer.load_model(self)
        most_similar,least_similar=TextAnalyzer.correlation1(self)
        vectors = np.array([model.wv[word] for word, similarity in most_similar+ 
                            least_similar])
        words = [word for word, similarity in most_similar + least_similar]
        return vectors,words
    
    # 使用t-SNE算法对词向量进行降维
    def t_sne(self):
        vectors,_=TextAnalyzer.merge(self)
        tsne = TSNE(n_components=2, perplexity=10)
        #print(vectors)
        vectors_tsne = tsne.fit_transform(vectors)
        return vectors_tsne
    
    #可视化降维后的词向量
    def visualization(self):
        _,words = TextAnalyzer.merge(self)
        vectors_tsne =TextAnalyzer.t_sne(self)
        fig, ax = plt.subplots()
        ax.set_title('春天', fontproperties = self._font)
        ax.scatter(vectors_tsne[:10, 0], vectors_tsne[:10, 1], color='blue')
        ax.scatter(vectors_tsne[10:, 0], vectors_tsne[10:, 1], color='red')
        for i, word in enumerate(words):
            ax.annotate(word, (vectors_tsne[i, 0], vectors_tsne[i, 1]),
                        fontproperties = self._font)
        plt.show()
    
    
    
        
        
        
        

