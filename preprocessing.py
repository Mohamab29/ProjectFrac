"""
Created on Sun Sep 20 11:10:27 2020

@author: Mohamed nedal abomokh
"""
### importing different libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import label
from skimage.transform import resize
from tqdm import tqdm
import os
from skimage.filters import sobel
from time import time

# We take the path of the masks and the train images
MASKS_PATH = "dataset/train/masks"
TRAIN_PATH = "dataset/train/images"


def calculate_time(start_time):
    """
    calculates the time from start to current time and returns it in secedes
    :param start_time: this is the time from which we want to calculate how much time has passed since this time
    :returns:the current time
    """
    return round(time() - start_time, 2)


def print_time(s_time, msg):
    """
    This function prints the time in seconds and minutes, for example it will print "msg" in 3:45 meaning the
    operation has ended in 3 minutes and 45 seconds
    :param msg: the msg we want to print the time
    :param s_time: the stating time just before starting the operation
    """
    m, s = divmod(calculate_time(s_time), 60)
    print(" --- " + msg + f" in {int(m):02d}:{int(s):02d}  --- ")


def prepare2train():
    """
    this is the main function in this script , eventually it should return all the augmented images and masks to the
    main script
    :returns: Augmented train image and Augmented masks
    """

    return None
