#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MapIt - launches a map in the browser using an address from the command line or clipboard
import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    # get address from command line.
    address = ' '.join(sys.argv[1:])
else:
# get from clipboard
    address = pyperclip.paste()

webbrowser.open('https://ditu.amap.com/search?query='+address)
