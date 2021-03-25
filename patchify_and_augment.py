from patchify import patchify
from preprocessing import *
import random
from scipy.ndimage.interpolation import map_coordinates
from scipy.ndimage.filters import gaussian_filter


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


def rotate_image(img, degree):
    """
    :param img: an image we want to rotate.
    :param degree: we rotate a given image to certain degree.
    """
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), degree, 1.0)
    return cv2.warpAffine(img, M, (w, h))


def elastic_transform(image, alpha, sigma, random_state=None, is_mask=False):
    """
    credits for this code goes to :
    https://gist.github.com/chsasank/4d8f68caf01f041a6453e67fb30f8f5a

    """
    assert len(image.shape) == 2

    if random_state is None:
        random_state = np.random.RandomState(None)

    shape = image.shape

    dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha
    dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma, mode="constant", cval=0) * alpha

    x, y = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]), indexing='ij')
    indices = np.reshape(x + dx, (-1, 1)), np.reshape(y + dy, (-1, 1))
    final_res = map_coordinates(image, indices, order=1).reshape(shape)  # image transformed
    if is_mask:
        final_res[final_res != 0] = 255  # because the values change

    return final_res


def threshold_(img):
    """
    :param img: an image that we want to threshold
    :returns: an array of same shape as input image and contains only two values 255 and 0
    """
    _, threshold_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return threshold_img


def choose_an_augmentation(num, img, is_mask=False):
    """
    :param is_mask: if it's a mask we want to keep the values to only 255 and 0.
    :param num: the parameter will take a random INT  which will be between 1-6,
     and depending on the number , the image will have an augmentation applied to it
    :param img: An image we want to apply to some form of augmentation .
    :returns: an augmented image or the image itself without change
    types of augmentations :
    Transformation , shearing , elastic deformation ...
    """
    # the elastic transformation takes sigma and alpha which can have different values that will give different shapes
    switcher = {
        1: elastic_transform(img, img.shape[1] * 8, img.shape[1] * 0.09, is_mask=is_mask),
        2: elastic_transform(img, img.shape[1] * 5, img.shape[1] * 0.07, is_mask=is_mask),
        5: elastic_transform(img, img.shape[1] * 7, img.shape[1] * 0.08, is_mask=is_mask),
        6: cv2.flip(img, 1),
        7: cv2.flip(img, -1),
        3: rotate_image(img, 45),
        4: rotate_image(img, -90)
    }
    return switcher.get(num)


def choose_(img, mask, rand_num_):
    """
    since this is a a code that repeats itself throughout the loop in the augment function , I made it look better
    by using this function
    """
    return choose_an_augmentation(rand_num_, img), choose_an_augmentation(rand_num_, mask, is_mask=True)


# random numbers end range e.g: 1 to 7
END_RANGE = 7


def randomize(old_num):
    """to generate a new random number that isn't the same as the old one"""
    num = old_num
    while old_num == num:
        num = random.randint(1, END_RANGE)
    return num


def augment(images, masks):
    """
    :param images: is a parameter that will take a numpy array of images and apply on each image an augmentation
    :param masks: is a parameter that will take a numpy array of masks and apply on each masks an augmentation
    :returns: An array containing augmented and original images
    We take them both because we want to have the same augmentation on both the image and it's mask ...
    """
    # creating lists that will contain all the augmented images and masks
    augmented_images, augmented_masks = [], []
    num_of_images = images.shape[0]
    rand_num = 0
    for inx in tqdm(range(num_of_images), total=num_of_images):

        # first we add the original image and mask
        augmented_images.append(images[inx])
        augmented_masks.append(masks[inx])

        # first augmentation for them both ,
        # temp1 = is an augmented image , temp2 = is augmented mask .
        rand_num = random.randint(1, END_RANGE)
        temp1, temp2 = choose_(images[inx], masks[inx], rand_num_=rand_num)
        augmented_images.append(temp1)
        augmented_masks.append(temp2)

        # add more images if lucky
        if rand_num % 3 == 0:
            rand_num = randomize(rand_num)
            temp1, temp2 = choose_(images[inx], masks[inx], rand_num_=rand_num)
            augmented_images.append(temp1)
            augmented_masks.append(temp2)

        elif rand_num % 2 == 0:
            rand_num = randomize(rand_num)
            temp1, temp2 = choose_(images[inx], masks[inx], rand_num_=rand_num)
            augmented_images.append(temp1)
            augmented_masks.append(temp2)

    return np.asarray(augmented_images), np.asarray(augmented_masks)


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

    # if we want to augment
    # augmented_images, augmented_masks = augment(resized_images, resized_masks)

    # No Augmentation
    augmented_images, augmented_masks = resized_images, resized_masks

    len_images = augmented_images.shape[0]

    print_time(start_time, f"done augmenting images and masks")

    images_patches = []
    masks_patches = []
    # making patches from each image and mask and scaling them to 1-0
    for inx in tqdm(range(len_images), total=len_images):
        images_patches.append(patches_from_(augmented_images[inx]) / 255)
        # we take a mask then we threshold it in order to have only 255 and 0 values,
        # then we normalize it and scale it back to be 0 to 1
        # we patchify each mask to 49 little images/patches
        masks_patches.append(patches_from_(threshold_(augmented_masks[inx])) / 255)

    images_patches = np.asarray(images_patches)
    masks_patches = np.asarray(masks_patches)

    patched_images = np.reshape(images_patches.copy(), (len_images * 49, 256, 256, 1))
    patched_masks = np.reshape(masks_patches.copy(), (len_images * 49, 256, 256, 1))

    print("########################################################")
    print(f"Number of original images is: {augmented_images.shape[0]}\n"
          f"Number of original masks is: {augmented_masks.shape[0]}")
    print("########################################################")
    print(f"Number of pachified images is: {patched_images.shape[0]}\n"
          f"Number of pachified masks is: {patched_masks.shape[0]}")
    print("########################################################")

    print_time(s_time=start_time, msg="done generating images and masks for training")

    return patched_images, patched_masks
