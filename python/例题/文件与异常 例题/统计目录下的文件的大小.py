#使用的函数
"""
os.path.getsize(path)#返回文件的大小,path指要读取大小的文件
os.listdir(path)#返回目录下所有文件的名称
os.path.isfile(path)#判断该对象为文件

"""

import os
def content(file,sum_size=0):
    for i in os.listdir(file):
        if os.path.isfile(i):
            sum_size+=os.path.getsize(i)
    print('该目录下的文件大小为%dMB'%(sum_size/1000))

files=input('请输入路径')
content(files)
        