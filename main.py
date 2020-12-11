from model import unet
from preprocessing import *
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2


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
        batch_size=100,
        verbose=1,
        epochs=15,
        validation_split=0.1,
    )
    print_time(s_time=start_time, msg="done training the U-net model")
    print("saving the model")
    model.save('Unet.h5')

    summarize_diagnostics(history)
    print_time(s_time=start_time, msg="finished running the script")


if __name__ == "__main__":
    train(40)
