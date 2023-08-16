# 1.urllib库的使用

## 1.1.urlopen()

### 1.1.1.含义

 表示向网站发起请求并获取响应对象

### 1.1.2.语法

```
urllib.request.urlopen(url,timeout)
```

1. urlopen() 有两个参数，说明如下：

2. url：表示要爬取数据的 url 地址。

3. timeout：设置等待超时时间，指定时间内未得到响应则抛出超时异常。

## 1.2.Request()

### 1.2.1.含义

该方法用于创建请求对象、包装请求头，比如重构 User-Agent（即用户代理，指用户使用的浏览器）使程序更像人类的请求，而非机器。

### 1.2.2.语法

urllib.request.Request(url,headers)
参数说明如下：

1. url：请求的URL地址。

2. headers：重构请求头。

## 1.3.html响应对象方法

```
bytes = response.read() # read()返回结果为 bytes 数据类型
string = response.read().decode() # decode()将字节串转换为 string 类型
url = response.geturl() # 返回响应对象的URL地址
code = response.getcode() # 返回请求时的HTTP响应码
```

## 1.4.编码解码操作

```
#字符串转换为字节码
string.encode("utf-8") 
#字节码转换为字符串
bytes.decode("utf-8") 
#使用urllib获取百度首页的源码
import urllib.request
#定义一个url
url='https://www.baidu.com'
#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)
#获取响应中的页面的源码
content=response.read()
html=content.decode('utf-8')
#打印数据
print(content)
```
