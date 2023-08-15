#1.生活中的循环
"""
每天都去向小美告白，直到成功为止

做的事情：告白
执行条件：未告白成功
就是未告白成功前，就会不停的告白
"""

#2.while循环 语法
"""
while 条件:
    条件满足时，做的事情1
    条件满足时，做的事情2
    。。。
#需要设置循环终止的条件，flower+=1,配合flower<101就能保证100次后停止
"""

#向小美告白100次（循环打印100次'小美，我喜欢你'）
flower=0 #初始告白数为0，统计告白次数
while flower<101: #条件是告白100次，不停的说100次'小美，我喜欢你‘，在此前，告白不会停止。
    print('小美，我喜欢你')
    flower+=1 #每告一次白，就会循环次数加1
#需要设置循环终止的条件，flower+=1,配合flower<101就能保证100次后停止



#4.无限循环
"""
当while的条件表达式为 True时，就变成了一个无限循环。
"""

#从1循环到100
num=0 #循环的初始化条件
while num<=100: #num循环到100前，num为true
    print(num)
    num+=1 #对num进行迭代;每循环一次num就开始加1
    
"""
解析
num为0时开始印刷，每循环一次num的值就加1.
num为100时，循环条件满足，停止循环num

"""

#从0加到100的和
num=1
i=0
while i<=100:
    i+=1
    num+=i
    print('结果是{}'.format(num))
    
    
#比大小    
import random
x=random.randint(1,100) #猜的随机数字被设定在1到100以内


while True : #无限循环
    y=int(input('请输入数字'))
#以下是判定大小的代码
    if y==x:
        print('恭喜你，猜对了')
        
    elif y<x:
        print('太小了')
        
    elif y>x:
        print("太大了")    