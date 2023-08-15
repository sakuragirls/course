import os
import time
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

# 设置请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 设置要爬取的标签和页数
tag = '美女'
page_count = 20

# 创建文件夹
if not os.path.exists(tag):
    os.mkdir(tag)

# 循环爬取每一页的数据
for i in range(1, page_count + 1):
    # 构造url
    url = f'https://www.pixiv.net/tags/{tag}/artworks?p={i}'

    # 发送请求
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # 获取标签所在页面的所有图片链接并保存到本地
        for img_tag in soup.find_all('img', class_=' _thumbnail ui-scroll-view'):
            img_url = img_tag['data-src']
            # 解析图片链接获取文件名
            filename = os.path.basename(urlparse(img_url).path)

            # 发送请求下载图片并保存到本地
            response = requests.get(img_url, headers=headers)
            if response.status_code == 200:
                with open(os.path.join(tag, filename), 'wb') as f:
                    f.write(response.content)
                    print(f'Successfully downloaded {filename}')
            else:
                print(f'Failed to download {filename}')

            # 随机延迟一段时间再继续下载下一张图片
            delay_time = round(time.time() % 3 + 1, 2)
            time.sleep(delay_time)
    else:
        print(f'Request {url} failed')
        