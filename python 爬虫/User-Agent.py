#User-Agent是什么
"""
中文名是用户代理，简称UA。是一个特殊的字符串头。使得服务器能识别用户使用的操作系统，cpu类型，浏览器及版本，浏览器插件，浏览器语言等等
"""

#User-Agent的作用
"""
使爬虫伪装成浏览器，以免触碰网站的反爬虫机制，以获取网站的相关信息。
"""

#重构爬虫ua信息
"""
使用ullib的Request方法对UA进行重构
"""

#使用urllib获取百度首页的源码
import urllib.request

#定义一个url
url='https://www.baidu.com'

#将User-Agant封装到header中
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
urllib.request.Request(url=url,headers=header)

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)

#获取响应中的页面的源码
content=response.read()
html=content.decode('utf-8')

#打印数据
print(content)


#文献资料
"""
http://c.biancheng.net/python_spider/user-agent.html
"""