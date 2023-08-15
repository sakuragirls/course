#TCP服务端程序开发流程
"""
1.创建服务端套接字对象
2.绑定ip地址与端口号
3.设置监听
4.等待接收服务器的连接请求
5.接收数据
6.发送数据
7.关闭套接字

"""


#2.socket类的介绍
"""
导入socket模块
import socket

创建socket对象使用socket类
socket.socket(Addressfamily,Type)

Addressfamily:IP地址类型，分为ipv4与ipv6
Type:传输协议类型
"""

#3.tcp服务端程序开发相关函数
"""
bind:绑定ip地址与端口号
listen:设定监听
accept:等待接收客户端的连接请求
send:发送数据
recv:接收数据
"""

