#1.类方法
#1.1.含义
"""
类方法就是针对类对象定义的方法

在类方法内部可以直接访问类属性或者调用其它的类方法

"""
#1.2.语法
"""
@claasmehod
def 类方法名(cls):
    pass
"""

"""
类方法需要用修饰器@classmethod来标识，告诉解释器这是一个类方法
类方法的第一个参数是cls
"""

#1.3.在方法内部
"""
可以通过.cls访问类的属性
可以通过.cls访问其它的类方法
"""
class student:
    count=1999 #定义类变量count,初始值为1999
    def __init__(self):
        student.count+=1 #调用类变量count,并自增1
    #定义类变量student_count
    @classmethod
    def student_count(cls):
        print('学生数量为%d个'%(cls.count)) #cls.count在方法内部调用类变量
        
    
student1=student()
student1.student_count()

#结果
"""
学生数量为2000个
"""


#2.静态方法
#2.1.语法
"""
@staticmehod
def 静态方法名():
    pass
"""
#2.2.调用静态方法
"""
使用类名.调用静态方法
"""
 
class dog():
    def run(self):
        print('狗会跑')
dog.run() #通过类名.调用静态方法

#结果
"""
狗会跑
"""


#确定方法类型的套路
"""
类方法：方法内部只需要访问类属性
静态方法：方法内部不需要访问类属性与实例属性
实例方法：方法内部需要访问实例属性

如果方法内部既需要访问类属性，又需要访问实例属性，就应该定义实例方法
"""


 
        
#文献资料        
"""
https://blog.csdn.net/lihao21/article/details/79762681
"""