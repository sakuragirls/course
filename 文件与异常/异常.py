#1.异常是什么
"""
异常是程序在运行过程中出现了错误。
"""

#2.捕获异常
#2.1.捕获异常是什么
"""
对可能出现的异常。提前准备解决这个异常的处理方案
"""

#2.2.语法
"""
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
#要求用户输入整数
try:
    num=int(input('请输入数字'))

except:
    print('输入错误，请再输入一遍') #假如输入的不是整数，就会执行except语句来报错
    
#结果
"""
请输入数字w
输入错误，请再输入一遍
"""

#2.3.错误类型捕获
#2.3.1.含义
"""
在执行程序时，可能出现不同类型的异常，那就要根据不同类型的异常，做出不同的响应
"""
#2.3.2.语法
"""
try:
    可能发生错误的代码
except 错误类型1:
    如果出现异常执行的代码
    
except 错误类型2:
    如果出现异常执行的代码
"""
def sum(a,b):
    try:
        return a/b       
    except ZeroDivisionError:
        print('输入错误，请再输入一遍')

   
try:     
    a=int(input('请输入第一个数字'))
    b=int(input('请输入第二个数字'))
    sum1=sum(a,b)
    print(sum1)
except ValueError: #捕获输入类型的错误
    print('输入类型错误') 
    
    
#2.4.捕获未知错误
#2.4.1.含义
"""    
在开发时，要预判到所有可能出现的错误，还是有一定难度的

如果希望程序无论出现什么错误，不会因为抛出异常而被终止，可以再增加except
"""
#2.4.2.语法
"""
except Exception as result:
    print("未知错误 %s"%(result))
"""
def sum(a,b):
    try:
        return a/b       
    except ZeroDivisionError:
        print('输入错误，请再输入一遍')
    except Exception as result:
        print('未知错误%s'%(result))

   
try:     
    a=int(input('请输入第一个数字'))
    b=int(input('请输入第二个数字'))
    sum1=sum(a,b)
    print(sum1)
except ValueError: #捕获输入类型的错误
    print('输入类型错误') 
except Exception as result:
    print('未知错误%s'%(result))


#异常捕获完整代码
"""
try:
    #尝试执行的代码
    pass
except 错误类型1:
    #根据错误类型1，对应的代码处理
except 错误类型2:
    #根据错误类型2，对应的代码处理
except (错误类型3,错误类型4):
    #根据错误类型3与4，对应的代码处理
except Expection  as result:
    print(result)

else:
    pass #没有异常才会执行的代码
    
finally:
    #无论是否出现异常，都会执行的代码
    print("无论是否出现异常，都会执行的代码")
"""
def sum(a,b):
    try:
        return a/b       
    except ZeroDivisionError:
        print('输入错误，请再输入一遍')
    except Exception as result:
        print('未知错误%s'%(result))

   
try:     
    a=int(input('请输入第一个数字'))
    b=int(input('请输入第二个数字'))
    sum1=sum(a,b)
    print(sum1)
except ValueError: #捕获输入类型的错误
    print('输入类型错误') 
except Exception as result:
    print('未知错误%s'%(result)) 