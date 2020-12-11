from sklearn.model_selection import train_test_split
from tensorflow.python.keras.utils.np_utils import to_categorical

from model import unet
from data import *
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2


# load an image and predict the class
def run_example():
    # load the image
    img = load_image('C:/Users/Vladis/Desktop/cell_images/Uninfected/C241NThinF_IMG_20151207_124643_cell_125.png')
    # load model
    model = load_model('unet.h5')
    # predict the class
    result = model.predict(img)
    print('Prediction:', result[0])


# plot diagnostic learning curves
def summarize_diagnostics(history):
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


def load_image(filename):
    # load the image
    img = load_img(filename, color_mode='rgb', target_size=(SIZE, SIZE))
    # convert to np.array
    img = np.array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])
    return img


def train():
    model = unet()
    dataset, label = create_dataset_and_labels('data/membrane/train/', 'image/', 'label/')
    X_train, X_test, y_train, y_test = train_test_split(np.asarray(dataset), np.asarray(label), test_size=0.20)
    print(model.summary())
    history = model.fit(
        x=X_train,
        y=y_train,
        batch_size=10,
        verbose=1,
        epochs=5,
        validation_split=0.1,
    )
    # print("Test_Accuracy: {:.2f}%".format(model.evaluate(np.array(X_test), np.array(y_test))[1] * 100))
    # summarize_diagnostics(history)
    # model.save('unet.h5')


train()