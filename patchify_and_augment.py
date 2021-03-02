from patchify import patchify
from preprocessing import *


# the desired size for an image and a mask for the training model

def patches_from_(image):
    """
    :arg image: is an image that we would like create patches from currently for each image of size 1024*1024
    we create (7,7,256,256) array which means 49 patches for each image
    :returns: patches of a given image
    """
    assert image.shape[0] != 2, "the image needs to be an numpy array of shape (height,width)"

    patches = patchify(image, patch_size=(256, 256), step=128)

    return np.reshape(patches, (49, 256, 256))


def threshold_(img):
    """
    :param img: an image that we want to threshold
    :returns: an array of same shape as input image and contains only two values 255 and 0
    """
    _, threshold_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return threshold_img


def augment(images, is_mask=False):
    """
    :param is_mask: if we enter masks we don't want to apply blur on them so we don't lose vlaues
    :param images: is a parameter that will take a numpy array of images and apply on each image a
    geometric transformation and blurring
    returns: An array containing augmented and original images
    """
    augmented = []

    for img in images:
        # first the original img
        augmented.append(img)
        # we flip the img horizontally and vertically and apply gaussian blur and threshold it, if it is mask .
        flip_both = cv2.flip(img, -1)

        flip_both = cv2.GaussianBlur(flip_both, (5, 5), 0)

        if is_mask:
            flip_both = threshold_(flip_both)

        augmented.append(flip_both.copy())

        # we flip the img horizontally and apply median blur and threshold it, if it is mask .
        flip_horizontal = cv2.flip(img, 1)

        flip_horizontal = cv2.medianBlur(flip_horizontal, 5)

        if is_mask:
            flip_horizontal = threshold_(flip_horizontal)

        augmented.append(flip_horizontal.copy())

    return np.asarray(augmented)


def patch_making():
    """
    :returns:
    patched and augmented images and masks
    """
    start_time = time()
    # first we load the images
    loaded_images = load_images(TRAIN_PATH, re_size=False)
    # second we load the masks
    loaded_masks = load_images(MASKS_PATH, re_size=False)

    # now we need to resize each mask and image to the desired size
    resized_images = []
    resized_masks = []

    # resizing the images and the masks
    len_images = loaded_images.shape[0]
    for inx in tqdm(range(len_images), total=len_images):
        resized_images.append(image_resize(loaded_images[inx], d_size=1024))
        resized_masks.append(image_resize(loaded_masks[inx], d_size=1024))

    # from list to a numpy array
    resized_images = np.asarray(resized_images)
    resized_masks = np.asarray(resized_masks)

    print_time(start_time, f"done resizing images and masks")

    augmented_images = augment(resized_images)
    augmented_masks = augment(resized_masks, is_mask=True)

    print_time(start_time, f"done augmenting images and masks")

    images_patches = []
    masks_patches = []
    # making patches from each image and mask
    for inx in tqdm(range(len_images), total=len_images):
        images_patches.append(patches_from_(resized_images[inx]) / 255)
        mask = patches_from_(resized_masks[inx])
        # iterating through each patch of a mask and making it a binary image
        for i in range(mask.shape[0]):
            _, thresh = cv2.threshold(mask[i], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            mask[i] = thresh // 255
        masks_patches.append(mask)

    images_patches = np.asarray(images_patches)
    masks_patches = np.asarray(masks_patches)

    patched_images = np.reshape(images_patches.copy(), (len_images * 49, 256, 256, 1))
    patched_masks = np.reshape(masks_patches.copy(), (len_images * 49, 256, 256, 1))

    print_time(s_time=start_time, msg="done generating images and masks for training")

    return patched_images, patched_masks
