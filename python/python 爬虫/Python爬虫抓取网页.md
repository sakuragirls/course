## 1.首先我们对要编写的爬虫程序进行简单地分析，该程序可分为以下三个部分：

拼接 url 地址
发送请求
将照片保存至本地

## 2.parse模块

### 2.1.parse模块是什么

一个工具模块，提供了许多URL处理方法，比如拆分、解析、合并等。

### 2.2.调用parse模块

```
import urllib.parse
```

### 2.3.quote()

将内容转化为URL编码的格式或进行URL解码。

```
from urllib import request
from urllib import parse
```

### 2.4.拼接url

```
s1=input('请输入要搜索的东西')
geturl=parse.quote(s1) #将字符串s1转换成url编码，字符串直接跟url拼接会报错
url='https://www.baidu.com/s?wd={}'
fullget=url.format(geturl)#url与geturl进行拼接
#获取百度页面源码
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req=request.Request(url=fullget,headers=headers)
response=request.urlopen(req)
html=response.read().decode('utf-8')
#将源码保存在创建的文件中
filename=s1+'.html'#创建文件名
with open('e://filename','w',encoding='utf-8') as f: #创建文件
    f.write(html)
    f.close()
```