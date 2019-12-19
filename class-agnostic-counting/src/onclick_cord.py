# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:36:12 2019

@author: IJR2KOR
"""
import matplotlib.pyplot as plt
from PIL import Image
from skimage.io import imsave
import numpy as np

from label_images import image2dots, dot_image_visualize

import os

def dot_annotate_image(image_path):
    
#    image_path = r'C:\Users\Sri\Documents\GitHub\drishti\class-agnostic-counting\src\path\to\pipe_dataset_reshaped\005pipe.png'
    img = Image.open(image_path)
    img = np.asarray(img)
    ax = plt.gca()
    fig = plt.gcf()
    implot = ax.imshow(img)
    
    dot_cords = []
    
    def onclick(event):
        global dot_cords
        if event.xdata != None and event.ydata != None:
    #        print(int(event.xdata), int(event.ydata), event.x)
            dot_cords.append([int(event.xdata),int(event.ydata)])
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    
    plt.show()
    
    return dot_cords


def save_annot_dot(image_path, dot_cords):
    
    dot_image = image2dots(dot_cords)
    plt.imshow(dot_image)
    b1=np.asarray(dot_image[:,:,0]>0)
    coords = np.column_stack(np.where(b1 == 1))
    print(len(coords))
    save_path = os.path.join(os.path.dirname(image_path),os.path.basename(image_path).replace('pipe','dots'))
    imsave(save_path,dot_image)
    img = Image.open(save_path)
    img = np.asarray(img)
    b1=np.asarray(img[:,:,0]>0)
    coords = np.column_stack(np.where(b1 == 1))
    print(len(coords))

    return dot_image
#plt.savefig(r'C:\Users\Sri\Documents\GitHub\drishti\class-agnostic-counting\src\path\to\pipe_dataset_reshaped\pic.png')
def save_amp_dot(image_path, dot_image):
        
    dot_image_vis = dot_image_visualize(dot_image)
    plt.imshow(dot_image_vis)
    save_path = os.path.join(os.path.dirname(image_path),os.path.basename(image_path).replace('pipe','dots_amp'))
    imsave(save_path,dot_image_vis)
    return dot_image_vis

image_path = r'C:\Users\Sri\Documents\GitHub\drishti\class-agnostic-counting\src\path\to\pipe_dataset_reshaped\005pipe.png'
dot_cords = dot_annotate_image(image_path)
dot_image = save_annot_dot(image_path,dot_cords)
dot_image_vis = save_amp_dot(image_path,dot_image)

