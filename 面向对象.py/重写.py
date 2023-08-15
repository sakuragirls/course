#1.重写
"""
子类在继承父类的成员属性与成员方法后，如果对它们不满意，可以对它们进行修改

即在子类中重新定义同名的属性或方法即可
"""

#2.实现方法
"""
在子类定义一个与父类同名的方法或变量并且实现
"""
"""
class phone11:
    def __init__(self):
       self.sign='4g'

    def signnow(self):
        print('现在信号为%s'%(self.sign))    
    
    
    
class phone12(phone11):
    def __init__(self):
        self.sign='5g'

    
phone=phone12()
phone.signnow()         
"""

#3.super()
#3.1.作用
"""
对父类方法进行扩充
如果定义子类的方法需要父类的方法时，就可以使用super.父类方法()

""" 

#3.2.子类调用构造函数
"""
def __init__(self,...):
    super().__init__(...)
"""

       
class student():
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
       
    def introdunce(self):
        print('大家好，我是%s,今年%d岁'%(self.name,self.sex))
        

class teacher(student):
    def __init__(self,name,sex):
        super().__init__(name,sex)#调用student类的构造方法
   
        
    def introdunce(self):
        print('大家好')
        super().introdunce()
        
        
teacher1=teacher('李亚军',30)
teacher1.introdunce()

#结果
"""
大家好
大家好，我是李亚军,今年30岁
"""        
        
    
#参考资料    
# http://c.biancheng.net/view/2290.html   
    