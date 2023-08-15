#定义函数
#定义一个函数要用def语句
#def语法：def 函数名(参数1,参数2...):
#写完def语句后，需要缩进然后编写函数体，函数的返回值用return语句编写

#函数调用
#指执行函数，就是使用该函数
#基本语法:返回值=函数名(形参值)

def sum(x,y): #定义函数sum,并赋予sum两个参数a与b
    if x>y: #如果x的值大于y，则返回x
        return x
    else: #如果y的值大于x，则返回y
        return y
    
c=sum(2,3)#调用sum函数,给sum中的两个参数赋值为2与3
print(c)
    
    
    
        
    