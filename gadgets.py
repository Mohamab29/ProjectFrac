"""
This script will contain Lots of useful gadgets (algorithms) that will be used
through out the this project ...
@author: Mohamed Nedal Abo-Mokh
"""
from time import time
import matplotlib.pyplot as plt


def calculate_time(start_time):
    """
    calculates the time from start to current time and returns it in secedes
    :param start_time: this is the time from which we want to calculate how much time has passed since this time
    :returns:the current time
    """
    return round(time() - start_time, 2)


def print_time(s_time, msg):
    """
    This function prints the time in seconds and minutes, for example it will print "msg" in 3:45 meaning the
    operation has ended in 3 minutes and 45 seconds
    :param msg: the msg we want to print the time
    :param s_time: the stating time just before starting the operation
    """
    m, s = divmod(calculate_time(s_time), 60)
    if s <= 1.0 and m <= 0.0:
        print(" --- " + msg + f" in less than a second  --- ")
    else:
        print(" --- " + msg + f" in {int(m):02d}:{int(s):02d}  --- ")


def display(img, title, cmap='gray'):
    """
    :arg img:an image we want to display
    :type title: str
    :arg cmap: using grayscale colo map to show gray scale images
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    plt.title(title)
    ax.imshow(img, cmap=cmap)
    plt.show()

