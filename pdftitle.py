#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:04:36 2018

@author: vpapg
"""

import os, re
from pdfrw import PdfReader

#path = r'/Users/varvarapapazoglou/Desktop/pdfs'


def renamePDFwithTitle(path, filename):
    
    errormsg = "[!] Unable to rename this file.\n"
    
    try:
        fullpath = os.path.join(path, filename)
        print("\n[*] CURRENT FILE:", filename)
        newname = PdfReader(fullpath).Info.Title
        
        if newname:
            newname = re.sub(r'[^\w\s]',' ',newname) # remove punctuation
            newname = re.sub(r'  ',' ',newname) # remove excess spaces
            newname = newname.strip('()') + '.pdf' # remove brackets
            if len(newname)>4:  # if the name is not just ".pdf"
                if newname[0] == ' ':   # if it starts with space, remove it
                    newname = newname[1:]
                    if newname[-5] == ' ': # if there's a space before the extension, remove it
                        newname = newname[:-5]+newname[-4:]
                        print("[*] NEW NAME:",newname)
                        newfullpath = os.path.join(path, newname)
                        os.rename(fullpath, newfullpath)
            else: print(errormsg) # if filename contains only ".pdf" (no title)
        else: print(errormsg) # if no title
    except Exception: # if other problem
        print(errormsg)
        pass # proceed to the next pdf


path = input("[+] Give the path of the directory with the PDFs to be renamed: ")

for filename in os.listdir(path):
    fullpath = os.path.join(path, filename)
    if not os.path.isfile(fullpath) or not filename[-4:]=='.pdf': continue
    renamePDFwithTitle(path, filename)