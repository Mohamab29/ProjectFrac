"""
Created on Sun Sep 20 11:10:27 2020

@author: Mohamed nedal abomokh
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import label
from skimage.transform import resize
from tqdm import tqdm
import os
from skimage.filters import sobel