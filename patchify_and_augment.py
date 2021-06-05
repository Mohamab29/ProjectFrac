from typing import Tuple

from preprocessing import *
import random
from scipy.ndimage.interpolation import map_coordinates
from scipy.ndimage.filters import gaussian_filter
from skimage.util.shape import view_as_windows


def repatch_prediction(prediction: np.ndarray, original_shape: tuple) -> np.ndarray:
    """
    When thee model makes a prediction for an image it takes patches made form the same image and returns a predicted mask
    with the same amount of patches, so we want to repatch back the prediction into the original shape of the image
    before we made patches from it.

    :param prediction: a numpy array of the shape(number of patches,desired size,desired size,1).
    :param original_shape: a tuple containing the original shape of the image before pachifying.
    :returns: a numpy array of the mask with the original shape.
    """
    rows, cols = int((prediction.shape[0] * desired_size) / original_shape[1]), int(
        (prediction.shape[0] * desired_size) / original_shape[0])
    y_pred = prediction.reshape((rows, cols, desired_size, desired_size))
    pred = np.zeros((original_shape[0], original_shape[1]))
    h, w = desired_size, desired_size
    for i in range(rows):
        for j in range(cols):
            pred[i * h:(i + 1) * h, j * w:(j + 1) * w] = y_pred[i][j]
    return pred


# the desired size for an image and a mask for the training model
def patches_for_prediction(image: np.ndarray) -> Tuple[np.ndarray, tuple]:
    """
    the model takes in 2d array in shape (desired_size,desired_size),so in order to predict a mask for a given images,
    we need to make patches for that image where each patch doesn't overlap with its neighbors.

    we first take an image and then we increase it's shape so that it can be dividable by the desired_size , we then
    use view_as_widows method and make patches.

    :param image: a 2D numpy array.
    :returns: patches of a given image, and the shape of the image with the new added borders
    """
    d_size = desired_size  # getting the global value into a local variable

    original_height, original_width = image.shape
    h_border = original_height - d_size - 1
    w_border = original_width - d_size - 1
    i = 0
    j = 0
    while j <= h_border:
        j += d_size
    while i <= w_border:
        i += d_size

    black_h_border = (j + d_size) - original_height
    black_w_border = (i + d_size) - original_width

    new_image = np.zeros((black_h_border + original_height, black_w_border + original_width))

    new_image[:original_height, :original_width] = image
    patches = view_as_windows(new_image, (d_size, d_size), step=d_size).astype(np.float32)
    rows, cols = patches.shape[0], patches.shape[1]

    patches = patches.reshape((rows * cols, d_size, d_size, 1)) / 255

    return patches, new_image.shape


def create_patches(image: np.ndarray, d_size=desired_size, stride=128) -> np.ndarray:
    """
Makes patches from a given 2D image where each patch is size of d_sizeXd_size and each patch is far 1*stride away.

    :param image: a 2d numpy array.
    :param d_size: the size of the width and height of the patch.
    :param stride: how many pixels to stride from patch to another.
    :return: a 3d numpy array that contains all the patches.
    """
    original_height, original_width = image.shape  # taking the original height and size
    patches = []
    # because each patch is size of desired size then we have a limit to how many times we can stride until we reach the
    # image border, so we calculate that border and use it as condition for when to stop patch making.
    h_border = original_height - d_size - 1
    w_border = original_width - d_size - 1
    i = 0
    j = 0
    last_patch_height = True
    last_patch_width = True
    ### patch making for training
    while i <= h_border:
        while j <= w_border:
            patches.append(image[i:i + d_size, j:j + d_size])
            j += stride
            if j > w_border and last_patch_width:
                j = w_border
                last_patch_width = False
        i += stride
        j = 0
        last_patch_width = True
        if i > h_border and last_patch_height:
            i = h_border
            last_patch_height = False

    return np.asarray(patches)


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
        4: elastic_transform(img, img.shape[1] * 5, img.shape[1] * 0.07, is_mask=is_mask),
        5: elastic_transform(img, img.shape[1] * 7, img.shape[1] * 0.08, is_mask=is_mask),
        3: cv2.flip(img, 1),
        2: cv2.flip(img, -1)
        # 3: rotate_image(img, 45),
        # 4: rotate_image(img, -90)
    }
    return switcher.get(num)


def choose_(img, mask, rand_num_):
    """
    since this is a a code that repeats itself throughout the loop in the augment function , I made it look better
    by using this function
    """
    return choose_an_augmentation(rand_num_, img), choose_an_augmentation(rand_num_, mask, is_mask=True)


# random numbers end range e.g: 1 to 7
END_RANGE = 5


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
    num_of_images = images.__len__()
    rand_num = 0
    for inx in tqdm(range(num_of_images), total=num_of_images):

        # first we add the original image and mask
        if np.random.random() > 0.7:
            augmented_images.append(images[inx])
            augmented_masks.append(masks[inx])

        # first augmentation for them both ,
        # temp1 = is an augmented image , temp2 = is augmented mask .
        # rand_num = random.randint(1, END_RANGE)
        # temp1, temp2 = choose_(images[inx], masks[inx], rand_num_=rand_num)
        # augmented_images.append(temp1)
        # augmented_masks.append(temp2)
        if 0.4 < np.random.random() <= 0.7:
            # rand_num = randomize(rand_num)
            temp1, temp2 = cv2.flip(images[inx], -1), cv2.flip(masks[inx], -1)
            augmented_images.append(temp1)
            augmented_masks.append(temp2)

        # add more images if lucky
        if np.random.random() <= 0.4:
            # rand_num = randomize(rand_num)
            temp1, temp2 = cv2.flip(images[inx], 1), cv2.flip(masks[inx], 1)
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

    # if we want to augment
    augmented_images, augmented_masks = augment(loaded_images, loaded_masks)
    len_images = augmented_images.shape[0]

    # No Augmentation
    # augmented_images, augmented_masks = loaded_images, loaded_masks
    # len_images = augmented_images.__len__()

    print_time(start_time, f"done augmenting images and masks")

    images_patches = []
    masks_patches = []
    # making patches from each image and mask and scaling them to 1-0
    number_of_patches = 0
    for inx in tqdm(range(len_images), total=len_images):
        image_patched = create_patches(augmented_images[inx], stride=72)
        # we take a mask then we threshold it in order to have only 255 and 0 values,
        mask_patched = create_patches(threshold_(augmented_masks[inx]), stride=72)
        number_of_patches += image_patched.shape[0]  # this is just to count how many patches we created
        for i in range(image_patched.shape[0]):
            images_patches.append(image_patched[i].copy() / 255)
            masks_patches.append(mask_patched[i].astype(np.uint8).copy() / 255)

    images_patches = np.asarray(images_patches)
    masks_patches = np.asarray(masks_patches)

    patched_images = np.reshape(images_patches, (number_of_patches, 256, 256, 1))
    patched_masks = np.reshape(masks_patches, (number_of_patches, 256, 256, 1))

    print("########################################################")
    print(f"Number of original images is: {augmented_images.shape[0]}\n"
          f"Number of original masks is: {augmented_masks.shape[0]}")
    print("########################################################")
    print(f"Number of pachified images is: {patched_images.shape[0]}\n"
          f"Number of pachified masks is: {patched_masks.shape[0]}")
    print("########################################################")

    print_time(s_time=start_time, msg="done generating images and masks for training")

    return patched_images, patched_masks
