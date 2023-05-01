import jieba
import week4day_read
#使用jieba分词
def cut_words(document):
    new_document=[]
    for line in document:
        new_line=jieba.cut(line,cut_all=False,HMM=True)#使用精确模式对文本分词
        new_document.extend(new_line)
    return new_document
if __name__=='__main__':
    cut_words()

#创建停用词
def stopwordslist(stopwords_address):#引入从网上下载的停用词表，存入停用词列表
    stopwords = [line.strip() for line in open(stopwords_address,encoding='UTF-8').readlines()]
    return stopwords
if __name__=='__main__':
    stopwordslist()

#停用词过滤
def stopwords_filter(new_document,stopwords):
    new_document1=[]
    for word in new_document:
        if word not in stopwords:#过滤“噪音”
            new_document1.append(word)#将过滤后的词语存入新的列表
    return new_document1
if __name__=='__main__':
    stopwords_filter()

#预处理后的词语用空格连接为字符串
def string_document(new_document1):
    lis_document=[]
    #使用空格将每个文档的词连接为字符串，实现文档的字符串表示
    new_document2=' '.join(new_document1)
    lis_document.append(new_document2)#将连接好的字符串放入一个列表，以便于后续词频矩阵的生成
    return lis_document
if __name__=='__main__':
    string_document()
    