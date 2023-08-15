#要使用的函数
"""
使用datetime模块中的datetime.now()函数获取当前日期与时间

使用strftime()将通过datetime.now()获取的日期与时间格式化
"""


import datetime
datetime1=datetime.datetime.now() #获取当前日期与时间
str_datetime=datetime1.strftime("%Y-%m-%d %H:%M:%S") #将获取的日期与时间格式化。要使用双引号
print(str_datetime)