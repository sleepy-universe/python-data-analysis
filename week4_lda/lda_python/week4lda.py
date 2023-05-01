from sklearn.decomposition import LatentDirichletAllocation
import numpy as np

def lda_topic(tv_fit):
    
    # LDA主题模型
    lda = LatentDirichletAllocation(n_components=2,  # 主题个数
                                    # max_iter=5,    # EM算法的最大迭代次数
                                    # learning_method='online',
                                    learning_offset=50., 
            # 仅仅在算法使用online时有意义，取值要大于1。用来减小前面训练样本批次对最终模型的影响
                                    random_state=0)
    # 文档所属每个类别的概率
    lda_topics_probability= lda.fit_transform(tv_fit)
    LDA_corpus = np.array(lda_topics_probability)
    # 每篇文章中对每个特征词的所属概率矩阵：list长度等于分类数量
    print('类别所属概率:\n', LDA_corpus)
    LDA_corpus_one = np.zeros([LDA_corpus.shape[0]])# 构建一个零矩阵
    # 对比所属两个概率的大小，确定属于的类别
    LDA_corpus_one = np.argmax(LDA_corpus, axis=1) # 返回沿轴axis最大值的索引，axis=1代表行
    print('每个文档所属类别：', LDA_corpus_one)
    return lda
if __name__=='__main__':
    lda_topic()
# 输出每个主题对应词语
def print_top_words(model, feature_words, n_top_words):
    #利用model.components得到一个形状为（n_components，n_features）的 n 维数组
    tt_matrix = model.components_
    id = 0
    for n_features in tt_matrix:
        #利用zip()函数将主题对应的词语与其概率写入元组，（再写入列表）
        tt_lis = [(name, tt) for name, tt in zip(feature_words, n_features)]
        #按概率降序排列该由元组组成的列表
        tt_lis = sorted(tt_lis, key=lambda x: x[1], reverse=True)
        #每个主题输出前n_top_words个频率最高的特征词
        tt_lis = tt_lis[:n_top_words]
        print('主题%d:' % (id), tt_lis)
        id += 1

if __name__=='__main__':
    print_top_words()


