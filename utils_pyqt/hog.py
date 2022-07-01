"""
func:提取hog特征，并且写入txt中
注意：可以修改resize函数中的值，调整读入尺寸（目前是64x64）
      文件的命名方式，必须属于同一缺陷的词尾要一致，举例：1_缺陷1.jpg 2_缺陷1.jpg...
"""
import numpy as np
import os
from skimage import feature as ft
import cv2

# img_label = {"straight": 0, "left": 1, "right": 2, "stop": 3, "nohonk": 4, "crosswalk": 5, "background": 6}
img_label = {"jz": 0, "ck": 1, "bg": 2}
img_dir = "./svm/data/samples/All"
write_txt = "./svm/hog_features.txt"


def hog_feature(img_array, resize=(64, 64)):
    """extract hog feature from an image.
    Args:
        img_array: an image array.
        resize: size of the image for extracture.
    Return:
    features:  a ndarray vector.
    """
    img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, resize)
    bins = 9
    cell_size = (8, 8)
    cpb = (2, 2)
    norm = "L2"
    features = ft.hog(img, orientations=bins, pixels_per_cell=cell_size,
                      cells_per_block=cpb, block_norm=norm, transform_sqrt=True)
    return features


def extra_hog_features_dir():
    resize = (64, 64)
    img_names = os.listdir("./svm/data/samples/All")
    img_names = [os.path.join("./svm/data/samples/All", img_name) for img_name in img_names]
    # print(img_names)
    if os.path.exists("./svm/hog_features.txt"):
        os.remove("./svm/hog_features.txt")

    with open("./svm/hog_features.txt", "a") as f:
        index = 0
        for img_name in img_names:
            img_array = cv2.imread(img_name)
            features = hog_feature(img_array, resize)
            print(img_name)
            '''
            根据自己命名样本的方式，提取出 最后 属于哪一类的标签
            '''
            label_name = img_name.split("\\")[-1].split("_")[-1].split(".")[0]
            print(label_name)

            label_num = img_label[label_name]

            row_data = img_name + "\t" + str(label_num) + "\t"

            for element in features:
                row_data = row_data + str(round(element, 3)) + " "
            row_data = row_data + "\n"
            f.write(row_data)

            if index % 100 == 0:
                print("total image number = ", len(img_names), "current image number = ", index)
            index += 1




