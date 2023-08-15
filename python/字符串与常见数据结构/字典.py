#1.字典
"""
用键值对的方式组织数据，利用键来搜索值
"""

#2.语法
"""
{键1:值1,键2:值2,键3:值3,...键n:值n}
"""


#2.1.创建空字典
#2.1.1一个是用花括号
d = {}
 
#2.1.2.另一个是用内置函数dict()
d = dict()



#2.2.添加字典元素
"""
字典名[键] = 值

"""

p={} #创建空字典
p[1]='a' #往字典中添加元素
print(p) 



#2.3.删除字典元素
#2.3.1.pop()
"""
 字典名.pop(键名) //删除字典中指定的键值对
"""
dict1={1:'a',2:'b',3:'c'}
dict1.pop(3)
print(dict1)
# 结果：{1: 'a', 2: 'b'}

#2.3.2.clear()
"""
字典名.clear() //删除字典中所有的键值对
"""
dict2={1:'a',2:'b',3:'c'}
dict2.clear()
print(dict2)
#结果 {}



#2.4.更改字典元素 
"""
字典名[键]=值 
"""
dicts={1:'a',2:'b'}
dicts[1]='c' #将1对应的值改为c
print(dicts)


#2.5.字典遍历
#2.5.1. for循环 //获取字典的所有键
dit={1:'a',2:'b',3:'c'}
for i in dit:
    print(i)


#2.5.2.keys()
"""
字典名.keys() #获取字典的所有键
"""
dit={1:'a',2:'b',3:'c'}
for i in dit.keys(): #遍历dit的所有键
    print(i)
#结果
"""
1
2
3
"""

#2.5.3.values()
"""
字典名.values() #获取字典的所有值
"""
dit={1:'a',2:'b',3:'c'}
for i in dit.values():
    print(i)
       
#2.5.4.ltems()
"""
字典名.items() //同时遍历key与values 
"""
dit={1:'a',2:'b',3:'c'}
for i in dit.items():
    print(i)

#2.5.5.注意
"""
1.字典在被循环的时候不能被循环删除和更新,否则会报错。解决方法就是将字典转换成列表形式就OK了。

2.for i in 字典: 中的i不能调用字典方法，也不能调用字符串方法。只能对i进行加减乘除，与if ，if。。。in语句使用，还有i作为下标使用
"""



#6.字典元素是否存在
"""
语法
key in dic

key：字典的键
dic：字典名

"""
dict={1:'a',2:'b',3:'c'}
if 1 in dict.keys(): #判断dict的键中是否存在1的键；
   print('存在')
else:
    print('不存在')


#2.7.字典合并
"""
使用update()方法
"""
dict1={1:'banana',2:'apple',3:'pear'}
dict2={4:'watermelon'}
dict1.update(dict2)#dict2的元素被合并到了dict1中
print(dict1)
#结果
"""
{1: 'banana', 2: 'apple', 3: 'pear', 4: 'watermelon'}
"""