#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import webbrowser

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('start ')
import sys

import bs4
import requests

print('Baiduing...')
res = requests.get('https://cn.bing.com/search?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.info(type(res))
# logging.info(res.text)
# : reterieve top search result links
soup = bs4.BeautifulSoup(res.text, features='html.parser')
# logging.info(soup)
# logging.info(soup.text)
# : open a browser tab for each result
linkEliems = soup.select('h2 a')
logging.info(linkEliems)
numOpen = min(5, len(linkEliems))
for i in range(numOpen):
    webbrowser.open(linkEliems[i].get('href'))


logging.debug('end')