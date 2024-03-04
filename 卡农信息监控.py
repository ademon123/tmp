#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@FILE Name    : 卡农信息监控.py
@Time     : 2021/1/6 10:07 
@Author   : liutao
'''
import requests
import re
import time
import datetime
import os
print(os.path.dirname(os.path.abspath(__file__)))
n = 0
while True:
    url = "https://www.51kanong.com/yh-231-1.htm"
    url0 = "https://www.51kanong.com"
    #url = "https://www.51kanong.com/xyk-2965135-1.htm"
    hd = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    res = requests.request('GET', url, headers=hd)
    content = res.text
    # <a href="xyk-2965066-1.htm" onclick="atarget(this)" class="s xst">
    #reg = r'<a href=".*?" onclick=".*?" class="s .*?">(.*?)</a>'
    reg = r'<a href=".*?" onclick=".*?" class="s .*?">(.*?)</a>'
    reg = re.compile(reg, re.S)
    name = re.findall(reg, content)
    reg0 = r'<a href="(.*?)" onclick=".*?" class="s .*?">'
    w = re.compile(reg0)
    ww = re.findall(w, content)
    www = []
    n += 1
    print('---------------------------------第%d次爬取网页内容------------------------------------'%n)
    for j in ww:
        ww0 = url0 + "/"+j
        www.append(ww0)
    for k in www[:10]:
        subres = requests.request('GET', k, headers=hd)
        subcontent = subres.text
        subreg = r'<title>(.*?)</title>'
        subreg = re.compile(subreg, re.S)
        subname = re.findall(subreg, subcontent)

        subreg2 = r'<em id=".*?">(.*?)</em>'
        subreg2 = re.compile(subreg2, re.S)
        sub_time = re.findall(subreg2, subcontent)
        if len(sub_time) > 0:
            print('发帖时间：', sub_time[0])
        for p in subname:
            print('爬取发帖内容：', p.replace("\n", ""))
            print('当前时间：', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            if '安逸花' in p or '立借' in p or '安宜花' in p or '爱又米' in p:
                print('---------------------出现撸贷现象，请及时处理-----------------------')
                print('---------------------出现撸贷现象，请及时处理-----------------------')
                print('---------------------出现撸贷现象，请及时处理-----------------------')
            else:
                continue
        time.sleep(5)