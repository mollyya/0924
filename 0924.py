# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:17:51 2023

@author: molly
"""

import os

os.mkdir('CS')
file=open('homework.txt','w')
file.write('4112029031_王遙')
file=open('homework.txt','r')
content=file.read()
file.close()
os.remove('homework.txt')
    
os.rmdir('cs')
    


