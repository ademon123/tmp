#!/usr/bin/python
# coding:utf-8
#https://blog.csdn.net/dnxbjyj/article/details/70236332
import requests
import re

# 根据url获取网页html内容
def getHtmlContent(url):
    page = requests.get(url)
    return page.text

# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg, html)
    # filenames="/users/liutao/desktop/网址.xls"
    # with open(filenames, 'w') as f:
    #         f.write(str(jpgs))
    #print(jpgs)
    return jpgs


#jgp=re.compile(r'img.+?src="(.+?\.jpg)" width')
#jpgs=re.findall(jgp,html)

# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    # 可自动关闭请求和响应的模块
    from contextlib import closing
    with closing(requests.get(imgUrl, stream=True)) as resp:
        with open(fileName, 'wb') as f:
            for chunk in resp.iter_content(128):
                f.write(chunk)

#保存图片网址到本地电脑
#filenames="/users/liutao/desktop/图片网址.xls"  #生成excel
#filenames="/users/liutao/desktop/图片网址.doc"  #生成word
filenames="/Users/liutao/Desktop/data/爬虫相关数据/download/图片网址.pdf"
# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls, path='/Users/liutao/Desktop/data/爬虫相关数据/download/'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        with open(filenames, 'a+', encoding='gbk') as f:
            f.write(url+"\n")
        print(('保存第{0}个连接:'.format(count)),url)
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        print('下载完成第{0}张图片'.format(count))
        count = count + 1

# 封装：从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)


def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)

if __name__ == '__main__':
    main()

