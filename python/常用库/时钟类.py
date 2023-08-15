#1.datetime模块
#1.导入datetime模块
"""
import datetime
"""

#1.2.datetime 类
"""
它有四个类：
datetime
date
time
timedelta
"""

#1.3.dates
"""
使用datetime.date()来表示日历日期
"""
#1.3.1.today()方法
"""
today()方法用于获取当前的日期
"""
from datetime import date
s1=date.today()
print(s1)
#结果
"""
2022-11-11
"""

#1.3.2.创建date对象
"""
日期类遵循以下语法:date(year,mouth,date)
"""
from datetime import date
s1=date(2022,11,11)
print(s1)
#结果
"""
2022-11-11
"""


#1.3.3.自定义日期格式
"""
使用strftime()定义日期格式。它将日期转换为字符串
"""
#常用格式
"""
%y:两位数的年份显示
%Y:四位数的年份显示
%m:指月
%d:指天
"""
from datetime import date
s1=date.today()
s2=s1.strftime('%y年.%m月.%d日')
print(s2)
#结果
"""
22年.11月.11日
"""


#1.4.time()
"""
时间值使用datetime.time()定义。

语法为datetime.time(hour,minute,second)
"""
#时间格式
"""
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
"""

#1.5.同时处理日期与时间
"""
datetime 库有另一个名为 datetime.datetime 的类，用于表示日期加时间。你可以称之为时间戳。
 datetime 类的now() 或 today() 方法可用于提取当前日期和时间。
"""