#1.使用的函数
"""
re.compile() #生成正则表达式对象
re.findall() #返回string与正则表达式对象相匹配的全部字符串
[a-z]:匹配指定范围内的任意字符。例如“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符
{n,m}最少匹配 n 次且最多匹配 m 次
re.verbose() #可以将正则表达式写成多行
"""
import re
content = '''
    寻隐者12345@qq.com不遇
    朝代：唐asdf12a#abc.com
    作python666@163.com者：贾岛
    松下问童子，言师python-abc@163.com采花去。
    只在python_ant-666@sina.net比山中，云深不知处   
'''
#从字符串中匹配出邮箱地址
patten=re.compile(r"""
    [a-zA-Z0-9]+ 
    \@
    [a-zA-Z0-9]+
    \.
    [a-zA-Z]{2,4}#匹配邮箱地址的末尾，就是2-4个大小写英文字母组成的           
""",re.VERBOSE)

results=patten.findall(content) #匹配与正则表达式相同的字符串
for result in results:
    print(result)