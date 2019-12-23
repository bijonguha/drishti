# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:55:37 2019

@author: IJR2KOR
"""

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

def image2dots(dots_list):
    
    dot_image = np.zeros((256,256,3))
    
    for i in range(len(dots_list)):
        dot_image[dots_list[i][1],dots_list[i][0],0] = 255
    
    return dot_image


def dot_image_visualize(dot_image):
    
    dot_image_vis = ndimage.gaussian_filter(
            dot_image, sigma=2, mode='constant')
    
    dot_image_vis*10 # if you needed to amplify
    return dot_image_vis



    
    
    

    
    