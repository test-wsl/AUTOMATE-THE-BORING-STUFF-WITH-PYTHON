#!/usr/bin/env python
# -*- coding: utf-8 -*-


SUBWORDLIST = [
    'ADJECTIVE', 'NOUN', 'VERB', 'NOUN',
]

with open('1.txt', 'r', encoding='utf-8') as rf:
    # : 将源文件导入新文件中
    wf = open('new.txt', 'w', encoding='utf-8')
    for line in rf:
        for word in line.split():
            if word in SUBWORDLIST:
                line = line.replace(word, input('请输入{}\n'.format(word.lower())))
            if word[:-1] in SUBWORDLIST:
                line = line.replace(word[:len(word)-1], input('请输入{}\n'.format(word[:len(word)-1].lower())))
        wf.write(line)
    wf.close()

# 读取文本文件，找出需要替换的单词位置


#  读取需要更改的单词
