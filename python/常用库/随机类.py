#1.random模块
"""
python的random模块可生成随机数
"""
#2.创建random模块
"""
import random
"""

#3.random的常用方法
#3.1.random.randint(a,b)
"""
用于生成一个指定范围的整数.其中a为下限,b为上限
"""
import random
s1=random.randint(1,100) #生成一个1到100之间的随机整数
print(s1)
#结果
"""
74
"""

#3.2.random.choice(sequence)
"""
从序列中获取一个随机元素,参数sequence指列表，元组，字符串，字典
"""
import random
list=[1,3,5,67,8]
s1=random.choice(list) #从列表list中随机获取一个元素
print(s1)

#结果
"""
5
"""

#3.3.random.shuffle()
"""
将一个列表中的元素打乱
"""
import random
list=[1,3,5,67,8]
s1=random.shuffle(list) #将列表list的元素打乱
print(list)
#结果
"""
[3, 1, 67, 5, 8]
"""

#3.4.random.random()
"""
随机生成在[0,10)范围内的实数
"""
import random
s1=random.random()
print(s1)
#结果
"""
0.7619046797410938
"""

#3.5.random.uniform(a,b)
"""
用于生成一个指定的随机浮点数.a为下限，b为上限
"""
import random
s1=random.uniform(100000,999999)
print(s1)
#结果
"""
136365.38248255523
"""