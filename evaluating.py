import cv2
import numpy as np
import pandas as pd
from preprocessing import load_images
from gadgets import *
from patchify_and_augment import patches_for_prediction, repatch_prediction
from keras.models import load_model
from main import crop_image

TEST_IMAGES_PATH = './dataset/test/images/'
TEST_MASKS_PATH = './dataset/test/masks/'

RECORDS_FILE = 'unet_model_records.csv'


def resize_image(left_img, right_img):
    """
    we resize the images while keeping the aspect ration intact
    :param left_img: the image we want to resize
    :param right_img: the image we use it's height and width to resize
    :return: return the left image resized
    the left and image is just for making the names easy, but left can be right and vice versa
    """
    desired_height, desired_width = right_img.shape

    # return the image with the new dims
    resized_image = cv2.resize(left_img, (desired_width, desired_height))
    _, thresh_img = cv2.threshold(resized_image, 0, 255, cv2.THRESH_BINARY
                                  | cv2.THRESH_OTSU)
    return thresh_img


def jaccard_similarity(image1: np.ndarray, image2: np.ndarray) -> float:
    """
        Computes the Jaccard similarity , a measure of set similarity.

        Parameters
        ----------
        image1: array-like, bool
            Any array of arbitrary size. If not boolean, will be converted.
        image2: array-like, bool
            Any other array of identical size. If not boolean, will be converted.
        Returns
        -------
        j_s : float
            Jaccard similarity as a float on range [0,1].
            Maximum similarity = 1,
            No similarity = 0

        Notes
        -----
        The order of inputs for `similarity` is irrelevant. The result will be
        identical if `image1` and `image2` are switched.
    """

    im1 = np.asarray(image1).astype(np.bool)
    im2 = np.asarray(image2).astype(np.bool)
    if im1.shape != im2.shape:
        raise ValueError(
            "Shape mismatch: im1 and im2 must have the same shape.")

    intersection = np.logical_and(im1, im2)
    union = np.logical_or(im1, im2)
    return intersection.sum() / union.sum()


def evaluate_models():
    start_time = time()
    models_records = pd.read_csv(RECORDS_FILE)
    models_names = list(models_records["name"])
    models_evaluated = {
        "name": [],
        "Jaccard_image0": [],
        "Jaccard_image1": [],
        "Jaccard_image2": [],
        "Jaccard_image3": [],
        "Jaccard_image4": [],
        "Jaccard_avg": []
    }
    test_images = load_images(TEST_IMAGES_PATH)
    test_masks = load_images(TEST_MASKS_PATH)

    for name in models_names:
        model = load_model(f'trained_models/{name}.h5')
        jac_sims = 0
        for index in range(test_images.__len__()):
            print(f"predicting a mask for a test image with index {index}")

            split_images, new_shape = patches_for_prediction(test_images[index])
            y_pred = model.predict(x=split_images, verbose=1, use_multiprocessing=True)
            pred = repatch_prediction(y_pred, new_shape)

            print_time(s_time=start_time, msg=f"done predicting mask for image{index}")

            pred = (pred * 255).astype(np.uint8)
            # histogram, bin_edges = np.histogram(pred, bins=5)
            th, image_pred = cv2.threshold(pred, 0, 255, cv2.THRESH_BINARY
                                           | cv2.THRESH_OTSU)
            image_pred = crop_image(image_pred)
            image_pred = resize_image(image_pred, test_masks[index])
            jac_sim = jaccard_similarity(image_pred, test_masks[index])
            jac_sims += jac_sim
            models_evaluated[f"Jaccard_image{index}"].append(jac_sim)
        models_evaluated["Jaccard_avg"].append(jac_sims / 5)
        models_evaluated["name"].append(name)

    df = pd.DataFrame(models_evaluated)
    df.to_csv("evaluated_models.csv", index=False)


evaluate_models()
