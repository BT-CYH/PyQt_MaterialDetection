import cv2
import numpy as np

def invert(img):
    test = img.copy()
    rows, cols = test.shape
    new = test.copy()
    for i in range(rows):
        for j in range(cols):
            new[i][j] = 255 - test[i][j]
    cv2.imwrite("test.png", new)