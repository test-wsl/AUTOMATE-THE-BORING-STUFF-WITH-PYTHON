#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

# 创建一个正则表达式匹配美国日期格式
import shutil

datePattern = re.compile(r"""
    (.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
""", re.VERBOSE)

# 循环文件夹下的文件名
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # 跳过没有日期的文件
    if mo == None:
        continue
    # print(mo.groups())
    # 得到文件名的不同部分
    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4)
    yearpart = mo.group(6)
    afterpart = mo.group(8)


    # 欧洲格式文件名
    eurofilename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart

    absWorkingdir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingdir, amerFilename)
    eurofilename = os.path.join(absWorkingdir, eurofilename)

    # rename
    print('Renamin %s to %s...'%(amerFilename, eurofilename))
    shutil.move(amerFilename, eurofilename)

# ： 欧洲各式的文件名

# ： 得到完整的文件路径

# : 重命名文件
