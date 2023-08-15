# 1.python 继承 含义
"""
子类继承于父类，可以直接调用父类中的方法与属性，不需要再次开发。
"""

# 2.继承 语法
"""
class 子类(父类名):
  #执行代码
"""



# 3.继承的传递性
"""
c类从b类继承，b类又从a类继承，那么c类就可以调用B与A的属性与方法
"""

#4.子类继承父类单个变量，方法

class name1:
  def __init__(self):
    self.name=18
    
  def hi_name(self):
    print('大家好,我是%s'%(self.name))
    
class name2(name1):
  def __init__(self, age):
    self.age=age
    
 
  def ages(self):
    print('大家好,我是%s,我今年%d岁'%(self.name,self.age))
    
  

name3=name2('李明',18)
name3.ages()
 
  

    
    




# 5.多继承






