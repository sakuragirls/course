word_count={} #用于统计单词数量

with open('e://word.txt','r',encoding='utf=8') as f: #打开要读取的文件
    for line in f: #一行一行遍历文件内容
        line=line[:-1] #去除每一行的换行符
        words=line.split() #按空格分割，
        for word in words: #遍历被split()成列表的字符串words;双重循环
            if word not in word_count.keys(): #如果word在字典的键中没有，就不自增
                word_count[word]=0 
            else:
                word_count[word]+=1

print(word_count)