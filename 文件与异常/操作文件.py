#1.os 介绍
"""
python中的os模块，可以对文件/文件夹进行操作
"""

#2.os 语法
"""
import os
"""


#3.os 常见用法

#3.1.目录操作
"""
#3.1.1. os.mkdir() //创建目录
import os
name='d://tc' #在d盘创建名为tc的文件夹
os.mkdir(name) #mkdir()创建目录，但只能创建一级目录，而不能创建多级目录

#3.1.2. os.makedirs() #创建多重目录
import os
os.makedirs(d://s1/s2)


#3.1.3. os.rmdir() //删除目录
import os
os.rmdir('d://s1')



"""

#3.2.文件操作
"""
#3.2.1. os.listdir() //列出文件夹中所有的文件
import os
filename=os.listdir("E://futa") //列出futa文件夹中的所有文件
print(filename)
#结果
【good.txt】


#3.2.2. os.rename('旧名字', '新名字') //重命名文件名
import os
os.rename('good.txt','bird.txt')   # 将good.txt重命名为bird.txt  
 

#3.2.3. os.remove('要删除的文件的路径') //删除文件    
import os
os.remove('good.txt') #删除e盘的good.txt

"""


#4.shutil模块
""" 
4.1.介绍
用于对文件的复制，移动（并重命名）

4.2.语法
import shutil

4.3.使用方法

4.3.1.复制
#4.3.1.1. shutil.copy('被复制的文件','目标文件') //将文件内容剪切到目标文件上
import shutil
shutil.copy('e://bad.txt','e://noting.txt')

#4.3.1.2. shutil.copyfile('被剪切的文件','目标文件') //将文件内容剪切到目标文件上
import shutil
filename=shutil.copyfile('e://good.txt','e://bad.txt') 将good.txt的内容复制到bad.txt上



4.3.2. 移动
4.3.2.1. shutil.move() //移动文件或文件夹

#将文件夹移动到另一个文件夹中
import shutil
filename=shutil.move('e://good','e://bads')

#将文件移动到一个文件夹中
import shutil
filename=shutil.move('e://good.txt','e://good') //将good.txt移动到good中

"""


#5.os.path
"""
5.1.介绍
获取文件属性

5.2.语法
import os.path

5.3.使用方法

print(path.exists('jk.txt')) #path.extists()得知文件是否存在 
"""

