#1.input()
"""
使用​input()​ 可以接收来自键盘的一个字符串（多个数据可以通过多个 ​input(​) 进行数据输入）
"""

#2.强制类型转换
x=input('请输入一个数字')
print(type(x)) #x的数据类型为str,只能接受字符串，如果存入数字等其它数据类型的东西的话，就会出现错误

msg = int(input("请输入你的值："))  # msg接受int类型的数值
msg =float(input("请输入你的值："))  # msg接受float类型的数值