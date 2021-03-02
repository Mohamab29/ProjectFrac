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


def patch_making(no_of_iters):
    """
    :arg no_of_iters: in the main loop we want to iterate no_of_iters times and at each iteration we create
    batch_size images.
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

    len_images = loaded_images.shape[0]
    for inx in tqdm(range(len_images), total=len_images):
        resized_images.append(image_resize(loaded_images[inx], d_size=1024))
        resized_masks.append(image_resize(loaded_masks[inx], d_size=1024))
    resized_images = np.asarray(resized_images)
    resized_masks = np.asarray(resized_masks)

    print_time(start_time, f"done resizing images and masks")
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

    # print_time(start_time, f"done making patches from images and masks")
    #
    # # and now the most time consuming thing , making augmentations
    # image_gen, mask_gen = creating_augmented_patches(patched_images, patched_masks)
    #
    # # we zip each mask with the image
    # generator = my_image_mask_generator(image_gen, mask_gen)
    #
    # train_images, train_masks = generate_from_(gen=generator, noi=no_of_iters)

    print_time(s_time=start_time, msg="done generating images and masks for training")

    return patched_images, patched_masks