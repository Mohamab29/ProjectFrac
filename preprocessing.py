"""
Created on Sun Sep 20 11:10:27 2020

@author: Mohamed Nedal Abo-Mokh
"""
### importing different libraries
import cv2
import numpy as np
from tqdm import tqdm
import os
from gadgets import *

# We take the path of the masks and the train images
MASKS_PATH = "./dataset/train/masks/"
TRAIN_PATH = "./dataset/train/images/"
batch_size = 10
SEED = 42
# the desired size for an image and a mask for the training model
desired_size = 256


def image_resize(img, d_size=desired_size):
    """
    :arg:the desired size if we want to change it
    making the padding for each image and then resizing it
    :return:the image resized with remaining borders being reflected
    """

    old_size = img.shape[:2]  # old_size is in (height, width) format

    # taking the ration to the original size
    ratio = float(d_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])

    # new_size should be in (width, height) format

    img = cv2.resize(img, (new_size[1], new_size[0]))

    delta_w = d_size - new_size[1]
    delta_h = d_size - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    color = [0, 0, 0]
    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

    return new_img


def load_images(path, re_size=False):
    """
     we load the images of the training set or the masks from the data set
     :param re_size:  if we want to use the resize function
     :arg path: the path of the folder we want to read the images from
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
    images_names.sort()
    # reading the train images or the mask images and converting them to grayscale
    print(f"Loading images from the {folder_name} folder")
    for n, img_name in tqdm(enumerate(images_names), total=len(images_names)):
        image = cv2.imread(path + img_name, 0)
        if re_size:
            image = image_resize(image)

        images.append(image)
    print_time(s_time, f"done loading images from {folder_name} folder")
    return np.asarray(images)
