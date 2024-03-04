#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@FILE Name  : 多文件放在一个excel中.py
@Time       : 2022/9/28 10:57 上午
@Author     : liutao
'''

import os
import pandas as pd

# 金服宝数据存放地址
path2 = "/Users/hxq/Documents/工作项目/同盾/浙商项目/金服宝项目/金服宝项目/9.26号导出/"
#path = "/Users/hxq/Documents/工作项目/同盾/浙商项目/金服宝项目/9.26号导出/"
file = os.listdir(path2)
print(file)

file_list = [i for i in file if '.xlsx' in i]
print('excel文件列表：', file_list)

# 创建结果文件
from openpyxl import load_workbook
writer = pd.ExcelWriter(path2+'res.xlsx',engine='openpyxl')

# 循环excel数据存放在res结果表中
for i in file_list:
    j = i.split(".")[0]
    print(i,j)
    dt = pd.read_excel(path2+i)
    dt.to_excel(excel_writer=writer, sheet_name=j)
writer.save()
writer.close()