#!/usr/bin/env python
# -*- coding: utf-8 -*-


def Comma(list):
    str = ''
    for i in range(len(list)):
        if i == 0:
            str = str + list[i]
        elif i == len(list) - 2:
            str = str + ' and ' + list[i]
        else:
            str = str + ' , ' + list[i]
    return str

def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(Comma(spam))


if __name__ == '__main__':
    main()
