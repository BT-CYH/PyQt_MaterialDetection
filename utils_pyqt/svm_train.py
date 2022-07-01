import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib


def load_hog_data(hog_txt):

    img_names = []
    labels = []
    hog_features = []
    with open(hog_txt, "r") as f:
        data = f.readlines()
        for row_data in data:
            row_data = row_data.rstrip()
            img_path, label, hog_str = row_data.split("\t")
            img_name = img_path.split("/")[-1]
            hog_feature = hog_str.split(" ")
            hog_feature = [float(hog) for hog in hog_feature]
            #print "hog feature length = ", len(hog_feature)
            img_names.append(img_name)
            labels.append(int(label))
            hog_features.append(hog_feature)
    return img_names, np.array(labels), np.array(hog_features)


def svm_train():
    """ SVM train
    C惩罚函数松弛变量
    tol停止训练的误差值
    probability是否显示置信度

    """
    img_names, labels, hog_features = load_hog_data("./svm/hog_features.txt")
    #clf = SVC(C=10, tol=1e-3, probability = True)
    clf = SVC(C=1, tol=1e-3, probability=True)
    #clf = svm.LinearSVC(max_iter=1000000)
    clf.fit(hog_features, labels)

    joblib.dump(clf, "./svm/svm_model.pkl")
    print ("finished.")









