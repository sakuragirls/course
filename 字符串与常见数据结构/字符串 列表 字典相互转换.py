#字符串转列表
commend='i love you'
s1=commend.split(' ') #split()会将处理后的字符串存入列表中，也就是以空格作为切割线
print(s1)
#结果：['i', 'love', 'you']

#列表转字符串
list2=['i','love','you']
print(' '.join(list2)) #用空格作为连接字符串的字符