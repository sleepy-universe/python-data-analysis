from  collections import defaultdict 
n = 100000

#按时间将评论读入，以字典形式实现
def day_read(fileaddress):
    document=defaultdict(list)
    with open(fileaddress,"r",encoding='utf-8') as f:
        line=f.readlines()
    for i in range(n):
        line[i]=line[i].split('\t')#把每一行的字符按照'\t'分开,存入一个列表
        line[i][2]=line[i][2].split(' ')
        line[i][2][-1]=line[i][2][-1].strip()#将每行评论最后的'\n'去掉
        day = str(''.join(line[i][2][0:3])+str(line[i][2][5]))#将day作为字典的键
        document[day].append(line[i][1])#按day将该列表中的第二块，即文本内容存入字典
    return document
if __name__=='__main__':
    day_read()
