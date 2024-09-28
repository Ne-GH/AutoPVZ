import sys
from time import sleep
from turtledemo.clock import datum
import cv2

import win32gui

from GetDataset import GetDataset

if __name__ == '__main__':
    dataset = GetDataset()

    while (True):
        dataset.get_dataset()
        sleep(1)

