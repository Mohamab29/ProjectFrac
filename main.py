from model import unet
from preprocessing import *
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
from pre_w_patches import patches_from_, patch_making
import tensorflow as tf
import random
from patchify import unpatchify

TEST_IMAGES_PATH = './dataset/test/images/'
TEST_MASKS_PATH = './dataset/test/masks/'
TEST_PREDS_PATH = './dataset/test/predictions/'


# plot diagnostic learning curves
def summarize_diagnostics(history):
    """
    printing the summary of of model
    :arg history:the model and it's history basically
    """
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    t = f.suptitle('CNN Performance', fontsize=12)
    f.subplots_adjust(top=0.85, wspace=0.3)

    max_epoch = len(history.history['accuracy']) + 1
    epoch_list = list(range(1, max_epoch))
    ax1.plot(epoch_list, history.history['accuracy'], label='Train Accuracy')
    ax1.plot(epoch_list, history.history['val_accuracy'], label='Validation Accuracy')
    ax1.set_xticks(np.arange(1, max_epoch, 5))
    ax1.set_ylabel('Accuracy Value')
    ax1.set_xlabel('Epoch')
    ax1.set_title('Accuracy')
    l1 = ax1.legend(loc="best")

    ax2.plot(epoch_list, history.history['loss'], label='Train Loss')
    ax2.plot(epoch_list, history.history['val_loss'], label='Validation Loss')
    ax2.set_xticks(np.arange(1, max_epoch, 5))
    ax2.set_ylabel('Loss Value')
    ax2.set_xlabel('Epoch')
    ax2.set_title('Loss')
    l2 = ax2.legend(loc="best")


def train(no_of_iters):
    """
    we first load the Unet model and then create the training data that we want to fit to our model
    and print the summary
    """
    start_time = time()
    print("loading the model")
    model = unet(input_size=(desired_size, desired_size, 1))
    print("preparing the data for training")
    x_train, y_train = patch_making(no_of_iters)
    print(model.summary())
    checkpointer = tf.keras.callbacks.ModelCheckpoint('FracUnet.h5', verbose=1, save_best_only=True)

    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=2, monitor='val_loss'),
        tf.keras.callbacks.TensorBoard(log_dir='logs')]

    history = model.fit(
        x=x_train,
        y=y_train,
        batch_size=10,
        verbose=1,
        epochs=10,
        validation_split=0.1,
        callbacks=callbacks
    )
    print_time(s_time=start_time, msg="done training the U-net model")
    print("saving the model")
    model.save('Unet1.h5')

    summarize_diagnostics(history)
    print_time(s_time=start_time, msg="finished running the script")


def test():
    """
    We read each image in the test folder and predict a mask for each image
    """
    start_time = time()
    print("Loading the model")
    model = load_model('Unet.h5')
    print("Finished Loading the model")
    random_index = random.randint(0, 4)
    test_images = load_images(TEST_IMAGES_PATH)
    test_masks = load_images(TEST_MASKS_PATH)

    print("predicting a mask for a test image")
    image = image_resize(test_images[random_index], d_size=1024)
    mask = image_resize(test_masks[random_index], d_size=1024)

    # making a patches for random image
    image_patched = patches_from_(image)
    image_patched = np.reshape(image_patched, (49, 256, 256, 1))

    # we use a 4-d shape because that's what our model takes
    y_pred = np.zeros((49, 256, 256, 1))

    # we predict a mask for each patch

    y_pred = model.predict(x=image_patched, verbose=1, use_multiprocessing=True)

    print_time(s_time=start_time, msg="done predicting mask")

    if not os.path.exists(TEST_PREDS_PATH):
        os.makedirs(TEST_PREDS_PATH)

    # unpatchifying that predictions into one image
    print("writing the images to the predictions folder")
    y_pred = (np.reshape(y_pred, (7, 7, 256, 256)) * 255).astype(np.uint8)
    unpatched_pred = unpatchify(y_pred, (1024, 1024))

    _, image_pred = cv2.threshold(unpatched_pred, 0, 255, cv2.THRESH_BINARY
                                  | cv2.THRESH_OTSU)
    cv2.imwrite(TEST_PREDS_PATH + str(0) + ".png", image_pred)

    plt.subplot(131), plt.imshow(test_images[random_index], cmap='gray'), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(image_pred, cmap='gray'), plt.title('prediction')
    plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(test_masks[random_index], cmap='gray'), plt.title('Mask')
    plt.xticks([]), plt.yticks([])
    plt.show()
    print_time(s_time=start_time, msg="finished testing and predicting")


def contrastStretching(im):
    b = im.max()
    a = im.min()
    # Converting im1 to float.
    c = im.astype(float)
    # Contrast stretching transformation.
    im1 = 255.0 * (c - a) / (b - a + 0.0000001)
    return im1


def enhance_preds(d_size):
    """
    :arg d_size: what size we desire to enhance the images to
    """
    start_time = time()
    print("enhancing the prediction images")
    images = load_images(TEST_PREDS_PATH)
    kernel = np.ones((5, 5), np.uint8)
    for i in range(len(images)):
        img = images[i]
        img = image_resize(img=img, d_size=d_size)
        img = np.reshape(img, (d_size, d_size))

        contrast_image = contrastStretching(img) / 255
        img = np.round_(contrast_image * 255).astype(np.uint8)

        _, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY
                                        | cv2.THRESH_OTSU)

        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        cv2.imwrite(TEST_PREDS_PATH + str(i) + ".png", img)

    print_time(s_time=start_time, msg="finished writing enhanced prediction ")


"""


"""
if __name__ == "__main__":
    test()
