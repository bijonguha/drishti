# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:57:09 2019

@author: Sri
"""

import os
from PIL import Image

path=r'C:\Users\Sri\Documents\GitHub\class-agnostic-counting\src\path\to\pipe dataset'
path2save = r'C:\Users\Sri\Documents\GitHub\class-agnostic-counting\src\path\to\pipe_dataset_reshaped'
filelist = os.listdir(path)
i=0
for file in filelist:
    i+=1
    file_name = "{0:03}".format(i)+'pipe'
    file_path = os.path.join(path,file)
    img = Image.open(file_path)
    img = img.resize((256,256))
    img.save(os.path.join(path2save,file_name)+'.png')
    