#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('start')
browser = webdriver.Chrome()

browser.get('http://inventwithpython.com')

try:
    elem = browser.find_elements_by_class_name('nav-item')
    logging.info(elem)
    print('Found <{}> element with that class name '.format(elem.tag_name))
except:
    print('Was not able to find an element with that name')
