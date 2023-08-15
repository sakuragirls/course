#1. in 与 not in是什么
"""
if x in list1 用于检查特定值x是否包含在列表list1中

if x not in list2 用于检查特定值x是否不包含在列表list2中
如果条件为真，则就会执行紧跟在if语句后面的代码
"""



list1=[1,2,3,4,5] #定义一个列表
a=list1[3]          #取列表中的第4个元素并赋值给变量a
if a>3 in list1:   #若a>3则执行语句print,若条件不满足则不输出值
    print(a)
#输出的结果如下 :true

