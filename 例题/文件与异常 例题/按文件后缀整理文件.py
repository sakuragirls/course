#所需要的函数
"""
os.path.splitext() 函数将文件名和扩展名分开
os.path.splitext()[0] #获取文件名
os.path.splitext()[1] #获取后缀名
os.listdir() #获取目录中的所有文件名
"""
import os
dir='E://web_clipper_chrome_2'
for file in os.listdir(dir): #遍历dir中所有的文件
    ext=os.path.splitext(file)[-1]#获取每一个文件的后缀
    print(file,ext) #打印所有文件及其后缀