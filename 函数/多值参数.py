#1.含义
"""
函数有时可能需要处理的参数个数不确定，这时就需要使用多值参数


Python中有两种多值参数：
参数名前增加一个*可以接收元组，
参数名前增加两个*可以接收字典，

一般给多值参数命名时，习惯用以下两个名字
**kwargs存放字典参数，kw是keyword缩写
*args存放元组参数，args是arguments缩写


"""


def sum(*num,**list): #num传入元组，list传入字典
    print(num)
    print(list)
       
sum(1,2,3,4,5,name='小明') #1,2,3,4,5传入num;name='小明'传入list

#结果
"""
(1, 2, 3, 4, 5)
{'name': '小明'}
"""

#2.元组与字典的拆包
"""
调用带有多值参数的函数时，如果希望：
将一个元组变量，直接传递给args
将一个字典变量，直接传递给kwargs

就可以用拆包来简化参数的传递：
在元组变量前，加入一个*
在字典变量前，加入两个*
"""
def sum(*nums,**list):
    print(nums)
    print(list)
    
nums = (1,2,3,4,5)
list={"name":"小明"}

sum(*nums, **list)
#等同于sum(1,2,3,4,5,name='小明') 

#结果
"""
(1, 2, 3, 4, 5)
{'name': '小明'}
"""