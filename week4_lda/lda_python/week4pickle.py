import pickle
def xuliehua(lda,tv_fit,feature_words):
    s1= pickle.dumps(lda)
    s2 = pickle.dumps(tv_fit)
    s3 = pickle.dumps(feature_words)
    return s1,s2,s3
    
    
