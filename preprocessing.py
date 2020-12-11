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


def load_images(path):
    """
     we load the images of the training set or the masks from the data set
     :returns: training images or masks after loading them
    """
    # loading train images or the masks
    # and checking the right name of the file to write the exception
    s_time = time()
    if "masks" in path:
        folder_name = "masks"
    elif "images" in path:
        folder_name = "images"
    else:
        folder_name = "Unknown"
    try:
        images_names = next(os.walk(path))[2]
    except FileNotFoundError:
        print(f"Something went wrong with reading the {folder_name} folder path\n"
              "Please check that you have entered the right path.")
    # and now we read each image from the specified folder
    images = []
    # reading the train images or the mask images and converting them to grayscale
    for n, img_name in tqdm(enumerate(images_names), total=len(images_names)):
        image = cv2.imread(path + img_name, 0)
        images.append(image)
    print(s_time, f"done loading images from {folder_name}")
    return np.asarray(images)


def prepare2train():
    """
    this is the main function in this script , eventually it should return all the augmented images and masks to the
    main script
    :returns: Augmented train image and Augmented masks
    """

    return None
