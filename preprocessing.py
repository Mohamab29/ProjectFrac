"""
Created on Sun Sep 20 11:10:27 2020

@author: Mohamed Nedal Abo-Mokh
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
from keras.preprocessing.image import ImageDataGenerator

# We take the path of the masks and the train images
MASKS_PATH = "./dataset/train/masks0"
TRAIN_PATH = "./dataset/train/images0"
batch_size = 40
SEED = 42
# the desired size for an image and a mask for the training model
desired_size = 256


def my_image_mask_generator(image_data_generator, mask_data_generator):
    """
    iterating through the sets of images and masks and zip them together so that we can have for each image a fitting
    label
    """
    train_generator = zip(image_data_generator, mask_data_generator)
    for img, mask in train_generator:
        yield img, mask


def creating_augmented_data():
    """
    this function uses keras image generator in order to generate random images with different shapes
    batch size is the number of bathes each time we want to generate an image
    """

    image_data_generator = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='reflect', rescale=1 / 255.
    ).flow_from_directory(TRAIN_PATH,
                          batch_size=batch_size,
                          target_size=(desired_size, desired_size)
                          , color_mode='grayscale',
                          shuffle=False,
                          seed=SEED
                          )

    mask_data_generator = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='wrap',
        rescale=1 / 255.
    ).flow_from_directory(MASKS_PATH,
                          batch_size=batch_size,
                          target_size=(desired_size, desired_size)
                          , color_mode='grayscale',
                          shuffle=False,
                          seed=SEED
                          )
    return image_data_generator, mask_data_generator


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
    if s <= 1.0 and m <= 0.0:
        print(" --- " + msg + f" in less than a second  --- ")
    else:
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
    print(f"Loading images from the {folder_name} folder")
    for n, img_name in tqdm(enumerate(images_names), total=len(images_names)):
        image = cv2.imread(path + img_name, 0)
        images.append(image)
    print_time(s_time, f"done loading images from {folder_name} folder")
    return np.asarray(images)


def prepare2train(no_of_iters):
    """
    this is the main function in this script , eventually it should return all the augmented images and masks to the
    main script
    :arg no_of_iters: in the main loop we want to iterate no_of_iters times and at each iteration we create
    batch_size images.
    :returns: Augmented train image and Augmented masks
    """
    # images = load_images(TRAIN_PATH)
    # masks = load_images(MASKS_PATH)
    # print(images.shape)
    start_time = time()
    # first we use image generator from keras to augment the images in the data set
    print("creating two generators,one for the image and one for the mask")
    image_gen, mask_gen = creating_augmented_data()

    # we zip each images mask with the image
    generator = my_image_mask_generator(image_gen, mask_gen)

    train_images = []
    train_masks = []
    i = 0
    # in this loop we generate batch_size*no_of_iters augmented images and masks
    print("creating the images and masks from the generators")
    for iters, data in enumerate(generator):
        aug_imgs, aug_msks = data
        aug_imgs = aug_imgs[0]
        aug_msks = aug_msks[0]
        for j in range(len(aug_imgs)):
            img = aug_imgs[j]
            img = (np.reshape(img, (img.shape[0], img.shape[1])) * 255).astype(np.uint8)
            train_images.append(img)
            img = aug_msks[j]
            img = (np.reshape(img, (img.shape[0], img.shape[1])) * 255).astype(np.uint8)
            train_masks.append(img)
        i += 1
        if i == no_of_iters:
            break
    print_time(s_time=start_time, msg="done generating images and masks for training")
    return np.asarray(train_images), np.asarray(train_masks)


x_train, y_train = prepare2train(40)
print(x_train.shape)
print(y_train.shape)
