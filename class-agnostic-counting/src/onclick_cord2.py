# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:51:06 2019

@author: IJR2KOR
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
y = x**2
coords = []

def onclick(event):
    click = event.xdata, event.ydata
    if None not in click: # clicking outside the plot area produces a coordinate of None, so we filter those out. 
        print('x = {}, y = {}'.format(*click))
        coords.append(click)
        
plt.plot(x,y)
plt.gca().figure.canvas.mpl_connect('button_press_event', onclick)
plt.show() # stops the CLI until the user closes the graph window
print("The clicked coordinates were: {}".format(coords))