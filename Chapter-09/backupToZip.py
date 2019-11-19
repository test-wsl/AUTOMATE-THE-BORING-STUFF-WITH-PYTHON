#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('start')
import os
import zipfile


def backupToZip(folder):
    # backu the entire contents of folder into zip file
    folder = os.path.abspath(folder)
    print(folder)
    # Figure out the filename this code
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

        # create zip file
    print("creating {}...".format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # walk eht entire folder tree  and copress the files
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding the current folder to zip file')
        backupZip.write(foldername, compress_type=zipfile.ZIP_DEFLATED)
        logging.info('foldername {}'.format(foldername))
    # add all file in zip file
        for file in filenames:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, file), compress_type=zipfile.ZIP_DEFLATED)
    backupZip.close()
    print('Done.')

logging.debug('end')


backupToZip('Python编程快速上手++让繁琐工作自动化')
