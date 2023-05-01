from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
def word_fre_matrix(lis_document):
    cv = CountVectorizer()#创建词袋数据结构
    cv_fit=cv.fit_transform(lis_document)#拟合模型，并返回文本矩阵
    '''print(cv_fit)#返回形式为：（第0个列表元素，元素对应词典中的索引）  词频
    print(cv.get_feature_names())#通过get_feature_names()可看到所有文本的特征词
    print(cv.vocabulary_)#返回特征词字典（value对应该词的索引）
    print(cv_fit.toarray())#通过toarray()可看到词频矩阵的结果'''
    return cv_fit,cv.get_feature_names()
if __name__=='__main__':
    word_fre_matrix()
#类似地，用TfidfVectorizer输出文本-词频矩阵
def word_tf_idf(lis_document):
    tv=TfidfVectorizer()
    tv_fit = tv.fit_transform(lis_document)
    '''print(tv_fit)
    print(tv.get_feature_names())
    print(tv_fit.toarray())'''
    return tv_fit,tv.get_feature_names()
if __name__=='__main__':
    word_tf_idf()