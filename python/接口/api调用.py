#如何调用api
"""
使用python的requests库进行访问，基本上是get或post请求，也就是http请求方法。

有些api会加密，然后必须使用对方提供的密钥对api继续解密或加密。

api返回的请求通常使用json格式的解密，所以使用python的requests库的json进行解析，然后提取我们所需要的数据。
"""
#注意
"""
使用api前先看一下api文档
"""


#爬取每日鸡汤
import json
import requests

def chicken_soup():
    url='http://open.iciba.com/dsapi/' #金山词霸的api
    soup=requests.get(url) #使用get请求api返回数据
    soups=json.loads(soup.text) #将api返回的数据进行json解析
    english=soups['content'] #提取 api的英文鸡汤
    translate=soups['note'] #提取 api的中文鸡汤
    print(english)
    print(translate)


chicken_soup()
#结果
"""
All l've ever done in my life was making my way here to you.
我今生的所做的一切都是为了找到你。
"""
    
#api 返回值
"""
{
    "sid": "3318",
    "tts": "http://news.iciba.com/admin/tts/2019-03-06-day1.mp3",
    "content": "Try to be a rainbow in someone’s cloud. ",
    "note": "努力成为别人乌云里的一道彩虹。",
    "love": "1215",
    "translation": "小编的话：当雨过天晴时，太阳照在云雨之中，你就是那天边的一抹彩色的虹，自然、纯净，美不胜收。",
    "picture": "http://cdn.iciba.com/news/word/20190306.jpg",
    "picture2": "http://cdn.iciba.com/news/word/big_20190306b.jpg",
    "caption": "词霸每日一句",
    "dateline": "2019-03-06",
    "s_pv": "0",
    "sp_pv": "0",
    "tags": [
        {
            "id": "",
            "name": ""
        }
    ],
    "fenxiang_img": "http://cdn.iciba.com/web/news/longweibo/imag/2019-03-06.jpg"
}


"""    


"""
1.收集了一些每日一句的接口与网站。
https://github.com/vv314/quotes

2.40行Python代码实现天气预报和每日鸡汤推送功能
https://www.jb51.net/article/181482.htm
"""