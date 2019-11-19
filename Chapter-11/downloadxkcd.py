#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable()
import bs4
import requests
logging.debug('start debug')
url = 'http://xkcd.com'
os.makedirs('img', exist_ok=True)

while not url.endswith('#'):
    # : download the page
    print("downloading the page %s..."%url)
    res = requests.get(url)
    res.raise_for_status()
    logging.info(type(res))
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    # : find the url of the comic image
    comicElem = soup.select('#comic img')
    logging.info(comicElem)
    if comicElem == []:
        print('Could not find comic img')
    else:
        comiurl =r'http:' + comicElem[0].get('src')
        logging.info(comiurl)

        print('Downloading img {}...'.format(comiurl))
        res = requests.get(comiurl)
        res.raise_for_status()
        if os.path.exists(os.path.join('img', os.path.basename(comiurl))):
            continue
    # : download the image
        else:
            with open(os.path.join('img', os.path.basename(comiurl)), 'wb') as imgf:
                for chunk in res.iter_content(100000):
                    imgf.write(chunk)

        prevlink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com'+ prevlink.get('href')

    # ； save image to ./img

    # : get the prev button's url

print('Done.')

logging.debug('end')