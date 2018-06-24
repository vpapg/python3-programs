#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 13:28:28 2018

@author: vpapg
"""

import os, errno
from shutil import copyfile

src = input("[+] Enter the full directory path: ")

dst = os.path.join(src, 'Copied')

if not os.path.exists(dst):
    try:
        os.makedirs(dst)
    except OSError as e:
        if e.errno != errno.EEXIST: raise

for file in os.listdir(src):
    if file[-4:].lower()=='.jpg' or file[-4:].lower()=='.mp4':
        copyfile(os.path.join(src, file), os.path.join(dst, file))