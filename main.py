from model import unet
from preprocessing import *
from keras.models import load_model
import cv2
import tensorflow as tf
import pandas as pd
from patchify_and_augment import patch_making, patches_for_prediction, repatch_prediction
from sklearn.model_selection import train_test_split

TEST_IMAGES_PATH = './dataset/test/images/'
TEST_MASKS_PATH = './dataset/test/masks/'
TEST_PREDS_PATH = './dataset/test/predictions/'
RECORDS_FILE = 'unet_model_records.csv'


# plot diagnostic learning curves
def summarize_diagnostics(history, model_record):
    """
    printing the summary of of model and updating the model record dictionary
    :param history: takes models history, and we can't get relevant data from it.
    :param model_record: is a dictionary that contains metadata about the model
    :returns model_record: updated dictionary with the relevant data.
    """
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    t = f.suptitle('Hand-made and regular masks Performance with augmentation - at least 50 epochs', fontsize=11)
    # f.subplots_adjust(top=0.85, wspace=0.3)

    max_epoch = len(history.history['accuracy']) + 1
    epoch_list = list(range(1, max_epoch))
    ax1.plot(epoch_list, history.history['accuracy'], label='Train Accuracy')
    ax1.plot(epoch_list, history.history['val_accuracy'], label='Validation Accuracy')
    ax1.set_xticks(np.arange(1, max_epoch, 5))
    ax1.set_ylabel('Accuracy Value')
    ax1.set_xlabel('Epoch')
    ax1.set_title('Accuracy')
    ax1.legend(loc="best")

    ax2.plot(epoch_list, history.history['loss'], label='Train Loss')
    ax2.plot(epoch_list, history.history['val_loss'], label='Validation Loss')
    ax2.set_xticks(np.arange(1, max_epoch, 5))
    ax2.set_ylabel('Loss Value')
    ax2.set_xlabel('Epoch')
    ax2.set_title('Loss')
    ax2.legend(loc="best")

    ax2.figure.savefig(f'accuracy_loss_graphs/accuracy_loss_{model_record["name"]}.png')

    model_record["num_of_epochs"] = max_epoch - 1
    model_record["train_accuracy"] = round(history.history['accuracy'][-1] * 100, 2)
    model_record["val_accuracy"] = round(history.history['val_accuracy'][-1] * 100, 2)
    model_record["train_loss"] = round(history.history['loss'][-1], 4)
    model_record["val_loss"] = round(history.history['val_loss'][-1], 4)

    return model_record


def save_record(model_record):
    """
    :param model_record: a model record we want to append to models records csv file.
    """

    df = pd.read_csv(RECORDS_FILE)
    df = df.append(model_record, ignore_index=True)
    df.to_csv(RECORDS_FILE, index=False)


def train():
    """
    we first load the Unet model and then create the training data that we want to fit to our model
    and print the summary.

    :var model_record: is a dictionary that contains {
        name : model_{time of start}_{date of start} .
        num_of_epochs : total epochs the model trained  .
        num_of_training_images: total number of images used for training of the model
        num_of_training_masks: total number of masks used for training of the model , must be same as number of training images.
        num_of _val_images: total number of images used for the validation of the model.
        num_of _val_masks: total number of masks used for training of the model , must be same as number of training images.
        train_loss: the loss score at the last epoch during the training .
        train_accuracy: the accuracy score at the last epoch during the training.
        val_loss: the loss score on the validation data.
        val_accuracy: the accuracy score on the validation data.
        augmented: no/yes.
    }
    """
    start_time = time()  # this is to show how many seconds or minutes have passed to run some block of code
    curr_time, curr_date = get_current_date_time()  # time and date of when the script was run

    model_name = f"model_{curr_time}_{curr_date}"
    augmented = "Yes"  # Yes / No

    model_record = {
        "name": model_name,
        "num_of_epochs": "number",
        "num_of_training_images": "number",
        "num_of_training_masks": "number",
        "num_of_val_images": "number",
        "num_of_val_masks": "number",
        "train_accuracy": "number",
        "val_accuracy": "number",
        "train_loss": "number",
        "val_loss": "number",
        "augmented": augmented
    }

    print("loading the model")
    model = unet(input_size=(desired_size, desired_size, 1))

    print("preparing the data for training")
    x_train, y_train = patch_making()
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

    # adding the number of images in the training dataset
    model_record['num_of_training_images'] = x_train.shape[0]
    model_record['num_of_training_masks'] = y_train.shape[0]
    model_record['num_of_val_images'] = x_val.shape[0]
    model_record['num_of_val_masks'] = y_val.shape[0]

    print(model.summary())

    # For evaluating the model
    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=8, monitor='val_loss'),
        tf.keras.callbacks.TensorBoard(log_dir=f'logs/logs_{model_name}')
    ]

    # fitting the model
    history = model.fit(
        x=x_train,
        y=y_train,
        batch_size=24,
        verbose=1,
        epochs=50,
        validation_data=(x_val, y_val),
        callbacks=callbacks
    )
    print_time(s_time=start_time, msg="done training the U-net model")
    print("saving the model")

    model.save(f'trained_models/{model_name}.h5')

    print(f"saving the record of the trained model: {model_name}")
    model_record = summarize_diagnostics(history, model_record)
    save_record(model_record=model_record)

    print_time(s_time=start_time, msg="finished running the script")


def crop_image(img):
    # cropping black borders from a given image
    mask = img > 0
    return img[np.ix_(mask.any(1), mask.any(0))]


def test():
    """
    We read each image in the test folder and predict a mask for each image
    """
    start_time = time()
    models_records = pd.read_csv(RECORDS_FILE)
    model_name: str = models_records["name"][24]  # a model name to run - in csv file index - 2

    print("Loading the model")
    model = load_model(f'trained_models/{model_name}.h5')
    print("Finished Loading the model")
    # random_index = 3  # random.randint(0, 4)
    test_images = load_images(TEST_IMAGES_PATH)
    test_masks = load_images(TEST_MASKS_PATH)
    for index in range(test_images.__len__()):
        print(f"predicting a mask for a test image with index {index}")

        # image = image_resize(test_images[random_index], d_size=1024)
        # # mask = image_resize(test_masks[random_index], d_size=1024)
        #
        # # splitting an image into (4,4,256,256) => meaning we will have 16 images each is (256,256)
        # split_images = view_as_windows(image, window_shape=(256, 256), step=256)
        #
        # # we use a 4-d shape because that's what our model takes
        #
        # split_images = np.reshape(split_images, (16, 256, 256, 1))
        # y_pred = np.zeros((16, 256, 256, 1))

        # we predict a mask for each patch
        split_images, new_shape = patches_for_prediction(test_images[index])
        y_pred = model.predict(x=split_images, verbose=1, use_multiprocessing=True)
        pred = repatch_prediction(y_pred, new_shape)

        print_time(s_time=start_time, msg="done predicting mask")

        # unpatchfying that predictions into one image
        print("writing the images to the predictions folder")
        pred = (pred * 255).astype(np.uint8)
        # histogram, bin_edges = np.histogram(pred, bins=5)

        th, image_pred = cv2.threshold(pred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #
        # # image_pred = cv2.adaptiveThreshold(pred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        # #                                    cv2.THRESH_BINARY_INV, 7, 0)
        # # kernel = np.ones((3, 3), np.uint8)
        # # image_pred = cv2.morphologyEx(image_pred, cv2.MORPH_CLOSE, kernel)
        # image_pred = cv2.medianBlur(image_pred, 1)
        # th, image_pred = cv2.threshold(image_pred, 0, 255, cv2.THRESH_BINARY)

        image_pred = crop_image(image_pred)
        # contours, hierarchy = cv2.findContours(image_pred, cv2.RETR_CCOMP,
        #                                        cv2.CHAIN_APPROX_SIMPLE)  # Use cv2.CCOMP for two level hierarchy
        # mask = np.zeros(image_pred.shape, dtype=np.uint8)
        # for i, cnt in enumerate(contours):
        #     # if the contour has no other contours inside of it
        #     if cv2.contourArea(cnt) > 300:
        #         # if hierarchy[0][i][3] == -1:  # basically look for holes
        #         # if the size of the contour is less than a threshold (noise)
        #
        #         # Fill the holes in the original image
        #         cv2.drawContours(mask, [cnt], 0, 255, 2)
            # image_pred = cv2.dilate(image_pred, kernel, iterations=1)
        # image_pred = pred.copy()
        # image_pred[pred > 0.5] = 255
        # mask = crop_image(mask)
        # mask = crop_image(mask)

        cv2.imwrite(TEST_PREDS_PATH + str(index) + f"_{model_name}.png", image_pred)

    # display(test_images[random_index], 'Original Image')
    # # display(test_masks[random_index], 'Ground truth Mask')
    # display(image_pred, 'Prediction')

    # configure and draw the histogram figure
    # plt.figure()
    # plt.title("Grayscale Histogram")
    # plt.xlabel("grayscale value")
    # plt.ylabel("pixels")
    # plt.xlim([0.0, 255.0])  # <- named arguments do not work here
    # plt.ylim([0.0, 100000.0])  # <- named arguments do not work here
    #
    # plt.plot(bin_edges[0:-1], histogram)  # <- or here
    # plt.show()
    """
    plt.subplot(131), plt.imshow(test_images[random_index], cmap='gray'), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(image_pred, cmap='gray'), plt.title('prediction')
    plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(test_masks[random_index], cmap='gray'), plt.title('Mask')
    plt.xticks([]), plt.yticks([])
    plt.figure(figsize=(20, 10))
    plt.show()
    """
    print_time(s_time=start_time, msg="finished testing and predicting")


if __name__ == "__main__":
    test()
