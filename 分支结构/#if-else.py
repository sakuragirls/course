#if-else 作用
"""
当If判断为true时，执行if下的语句,当if判断为false,执行else下的语句
"""

#用户身份验证
usename=input('请输入账号')
password=input('请输入密码')

if usename=='admin'and password==123456:
    print('登录成功')
else:
    print('请再输入一遍')
    