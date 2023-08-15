#if-elif-else 作用
"""
判断多个条件的语句，if为真则执行if后的语句
如果eilf的语句是真的，则执行elif的语句，后面的语句就不执行
如果elif与if都为假，则执行else语句
"""
#elif-if语法
"""
if 判断语句:
    代码块
eilf 判断语句:
    代码块
else:
    代码块
    
"""

grade=float(input('请输入分数'))
if grade>=90:
    print('great good')

elif grade>=80:
    print('good')
    

elif grade>=70:
    print('common')
    

elif grade>=60:
    print('pass')
    
else:
    print('bad')
    
