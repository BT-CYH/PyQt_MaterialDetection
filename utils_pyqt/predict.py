import os
import numpy as np
import cv2
from skimage import feature as ft
from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from sklearn import svm

cls_names = ["Inclusion", "Crack", "Background"]
img_label = {"jz": 0, "ck": 1, "bg": 2}

def draw_rects_on_img(img, rects):
    img_copy = img.copy()
    for rect in rects:
        x, y, w, h = rect
        cv2.rectangle(img_copy, (x,y), (x+w,y+h), (0,255,0), 2)
    return img_copy

def hog_extra_and_svm_class(proposal, clf, resize = (64, 64)):
    '''
    用于从新输入的图片中提取hog特征
    '''
    img = cv2.cvtColor(proposal, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, resize)
    bins = 9
    cell_size = (8, 8)
    cpb = (2, 2)
    norm = "L2"
    features = ft.hog(img, orientations=bins, pixels_per_cell=cell_size,
                        cells_per_block=cpb, block_norm=norm, transform_sqrt=True)
    print ("feature = ", features.shape)
    features = np.reshape(features, (1,-1))
    cls_prop = clf.predict_proba(features)

    print("type = ", cls_prop)
    print ("cls prop = ", cls_prop)
    return cls_prop

def gen_proposals(img, step, clf):
    cls_names = ["Inclusion", "Crack", "Background"]
    img_label = {"jz": 0, "ck": 1, "bg": 2}
    maxx = 0
    maxy = 0
    maxprop = 0
    clsname = " "
    img_bbx = img.copy()

    for y in range(0, img_bbx.shape[0], step):  #垂直尺寸y
        for x in range(0, img_bbx.shape[1], step):  #水平尺寸x
            proposals = img_bbx[y:y+64, x:x+64]
            cls_prop = hog_extra_and_svm_class(proposals, clf)
            cls_prop = np.round(cls_prop, 2)[0]
            cls_num = np.argmax(cls_prop)
            cls_name = cls_names[cls_num]
            prop = cls_prop[cls_num]

            # 预测分类不是背景且置信度大于某个值，再显示出矩形框
            if cls_name is not "Background" and prop > maxprop:
                maxprop = prop
                maxx = x
                maxy = y
                clsname = cls_name

    return maxx, maxy, maxprop, clsname

def predict_img(img_path):
    #加载模型
    clf = joblib.load("./svm/svm_model.pkl")
    img = cv2.imread(img_path)
    maxscore = 0
    maxscale = 10

    '''
    对输入图片进行缩放，找到预测值最高的情况下的比例，多尺度缩放
    '''
    for i in range(14, 16):
        img_test = img.copy()
        img_test = cv2.resize(img, (i*64, i*64))
        x, y, score, cls_name = gen_proposals(img_test, 64, clf)
        if(score > maxscore):
            maxscore = score
            maxscale = i

    img_res = cv2.resize(img, (maxscale * 64, maxscale * 64))
    x_res, y_res, score_res, cls_name_res = gen_proposals(img_res, 64, clf)

    print(maxscale)
    print(score_res)
    print(cls_name_res)
    '''
    结果可视化
    '''
    cv2.putText(img, cls_name_res + str(maxscore), (x_res, y_res), 1, 1.5, (0, 0, 255), 2)
    cv2.rectangle(img, (x_res, y_res), (x_res+64, y_res+64), (0, 255, 0), 2)
    #cv2.imshow("detect result", img)
    cv2.imwrite("svm_detect_result.jpg", img)
    #cv2.waitKey(0)



