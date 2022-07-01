import cv2
import numpy as np
import time
import os

#定义分析夹杂缺陷的函数
def analysis_inclusion(address=None, cls=None, ord=None, na=None):

    img0 = cv2.imread(address)

    # 获取操作时间
    localtime = time.asctime(time.localtime(time.time()))

    # 预处理
    img1 = cv2.medianBlur(img0, 3)  # 中值滤波
    b, g, r = cv2.split(img1)  # 通道划分
    ret, thresh1 = cv2.threshold(b, 235, 255, cv2.THRESH_BINARY)  # 阈值分割

    # 轮廓检索
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 计算获得轮廓的长度
    length = np.arange(len(contours))
    for i in range(len(contours)):
        length_temp = cv2.arcLength(contours[i], True)
        length[i] = length_temp

    # 找到轮廓周长最大的即为缺陷位置
    index = np.argmax(length)
    area = cv2.contourArea(contours[index])
    M = cv2.moments(contours[index])  # 图像矩
    cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']  # cx cy轮廓的质心坐标

    # 输出缺陷信息
    print("图片路径 %s" % address)
    print("缺陷类型：%s" % cls)
    print("夹杂质心坐标： %f , %f" % (int(cx), int(cy)))
    print("此处夹杂缺陷的周长是 %f" % length[index])
    print("此处夹杂缺陷的面积是 %f" % area)

    # 文件写入
    fo = open("./result.txt", "a")
    fo.write("%s \n" % localtime)
    fo.write("Image Path: %s \n" % address)
    fo.write("Type of Defect: %s \n" % cls)
    fo.write("Centroid Coordinates: %f , %f \n" % (int(cx), int(cy)))
    fo.write("Perimeter: %f \n" % length[index])
    fo.write("Area: %f \n" % area)
    fo.write("\n")
    fo.write("\n")
    fo.close()


# 读入图片
input_path = "./temp/"
file_name = os.listdir(input_path)

for file in file_name:
    cls_name = file.split('_')[0][:-5]  #当前图片的缺陷类别
    name = file.split('_')[2]   #当前图片的原始名字
    order = file.split('_')[1]  #当前图片的第几个缺陷
    print(cls_name)

    if cls_name == 'inclusion':
        img_path = "./temp/" + file
        analysis_inclusion(address=img_path, cls=cls_name, ord=order, na=name)


