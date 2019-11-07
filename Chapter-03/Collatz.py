#!/usr/bin/env python
# -*- coding: utf-8 -*-


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main():
    number = int(input('输入一个整数'))
    while True:
        number = collatz(number)
        if number != 1:
            print(number)
        else:
            print(1)
            break



if __name__ == '__main__':
    main()

