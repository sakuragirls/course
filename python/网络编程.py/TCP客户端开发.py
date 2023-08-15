#1.TCP网络应用开发分为
"""
1.1.TCP客户端程序开发

1.2.TCP服务端程序开发
"""

#2.客户端程序与服务端程序
"""
客户端程序：运行在用户设备上的程序

服务端程序：运行在服务器设备上的程序

"""


#3.TCP客户端开发流程
"""
3.1.创建客户端套接字对象
3.2.与服务套接字建立连接
3.3.发送数据
3.4.接收数据
3.5.关闭客户套接字对象

"""

#4.socket类的介绍
"""
导入socket模块
import socket

创建socket对象使用socket类
socket.socket(Addressfamily,Type)

Addressfamily:IP地址类型，分为ipv4与ipv6
Type:传输协议类型
"""

#5.开发TCP客户端所使用的函数
"""
connect:与服务器套接字创建连接
send:发送数据
recv:接收数据
close:关闭连接

"""