#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pw.py - An insecure password locker program
import pyperclip as pyperclip

PASSWORDS = {
    'email': '',
    'blog': '',
    'luggage': ''
}

import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # 第一个参数为账户名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)


