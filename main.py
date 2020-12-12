from model import unet
from preprocessing import *
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
import tensorflow as tf

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
    x_train, y_train = prepare2train(no_of_iters)
    print(model.summary())
    history = model.fit(
        x=x_train,
        y=y_train,
        batch_size=20,
        verbose=1,
        epochs=10,
        validation_split=0.1,
    )
    print_time(s_time=start_time, msg="done training the U-net model")
    print("saving the model")
    model.save('Unet.h5')

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

    x_test = load_images(TEST_IMAGES_PATH, resize=True)
    y_true = load_images(TEST_MASKS_PATH, resize=True)

    print("predicting a mask for each test image")
    y_pred = model.predict(x=x_test, verbose=1, use_multiprocessing=True)
    print_time(s_time=start_time, msg="done predicting masks")

    if not os.path.exists(TEST_PREDS_PATH):
        os.makedirs(TEST_PREDS_PATH)

    print("writing the images to the predictions folder")
    for i in range(len(y_pred)):
        image = y_pred[i]
        image = (np.reshape(image, (desired_size, desired_size)) * 255).astype(np.uint8)
        cv2.imwrite(TEST_PREDS_PATH + str(i) + ".png", image)

    print_time(s_time=start_time, msg="finished testing and predicting")


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
        _, image_result = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY
                                        | cv2.THRESH_OTSU)

        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        cv2.imwrite(TEST_PREDS_PATH + str(i) + ".png", img)

    print_time(s_time=start_time, msg="finished writing enhanced prediction ")


if __name__ == "__main__":
    enhance_preds(680)
