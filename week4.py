from lda_python import week4day_read
from lda_python import week4pre_disposition
from lda_python import week4words_fre_matrix
from lda_python import week4lda
from lda_python import week4pickle
n_top_words = 8
fileaddress = "C:\\Users\\modey\\Desktop\\python数据分析\\weibo.txt"
stopwords_address="C:\\Users\\modey\\Desktop\\python数据分析\\stop_words.txt"
dic1=week4day_read.day_read(fileaddress)
days = list(dic1.keys())
for i in days:
    document=dic1[i]
    new_document=week4pre_disposition.cut_words(document)
    stopwords=week4pre_disposition.stopwordslist(stopwords_address)
    new_document1=week4pre_disposition.stopwords_filter(new_document, stopwords)
    lis_document=week4pre_disposition.string_document(new_document1)
    print('{}'.format(i))
    tv_fit,feature_words=week4words_fre_matrix.word_tf_idf(lis_document)
    #week4words_fre_matrix.word_fre_matrix()
    lda=week4lda.lda_topic(tv_fit)
    week4lda.print_top_words(lda, feature_words, n_top_words)
    week4pickle.xuliehua(lda, tv_fit, feature_words)
    
    
    