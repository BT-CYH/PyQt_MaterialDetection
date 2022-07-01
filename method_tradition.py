from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from emphasize import*
from invert import*
import time

class Ui_method_tradition(QtWidgets.QDialog):

    def __init__(self):
        super(Ui_method_tradition, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, method_tradition):
        method_tradition.setObjectName("method_tradition")
        method_tradition.resize(1261, 740)
        method_tradition.setFixedSize(1261, 740)
        method_tradition.setStyleSheet('''#method_tradition{

                                                                                  border-bottom-left-radius:15px;
                                                                                  border-bottom-right-radius:15px;
                                                                                  border-image:url(pic/back1.png)
                                                                                  }
                                                                ''')

        self.label = QtWidgets.QLabel(method_tradition)
        self.label.setGeometry(QtCore.QRect(510, 40, 711, 671))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(method_tradition)
        self.pushButton.setGeometry(QtCore.QRect(120, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit = QtWidgets.QTextEdit(method_tradition)
        self.textEdit.setGeometry(QtCore.QRect(70, 530, 421, 130))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("请点击选择文件按钮")
        self.textEdit.append("选择待处理的图片")

        ########################################################
        #为了配合阈值分割功能新建的控件：输入阈值框
        self.lineEdit_2 = QtWidgets.QLineEdit(method_tradition)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 670, 150, 40))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(method_tradition)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 670, 150, 40))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(method_tradition)
        self.label_4.setGeometry(QtCore.QRect(10, 670, 50, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_17 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_17.setGeometry(QtCore.QRect(410, 670, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        ################################################################


        self.pushButton_9 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 340, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 470, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_11.setGeometry(QtCore.QRect(120, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 290, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_14.setGeometry(QtCore.QRect(120, 340, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_15.setGeometry(QtCore.QRect(290, 470, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(method_tradition)
        self.pushButton_16.setGeometry(QtCore.QRect(120, 290, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")

        self.label_2 = QtWidgets.QLabel(method_tradition)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(method_tradition)
        self.label_3.setGeometry(QtCore.QRect(50, 340, 500, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(method_tradition)
        self.pushButton_15.clicked.connect(self.slot_return)
        self.pushButton_8.clicked.connect(self.slot_readimage)
        self.pushButton_6.clicked.connect(self.slot_emphasize)
        self.pushButton_4.clicked.connect(self.slot_blur)
        self.pushButton_3.clicked.connect(self.slot_invert)
        self.pushButton_10.clicked.connect(self.slot_return_origin)
        self.pushButton_2.clicked.connect(self.slot_sharpen)
        self.pushButton_5.clicked.connect(self.slot_threshold)
        self.pushButton_17.clicked.connect(self.slot_confirm)
        self.pushButton_7.clicked.connect(self.slot_findcontours)
        self.pushButton.clicked.connect(self.slot_readme)

        # self.pushButton_2.hide()
        # self.pushButton_3.hide()
        # self.pushButton_4.hide()
        # self.pushButton_5.hide()
        # self.pushButton_6.hide()
        # self.pushButton_7.hide()

        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.label_4.hide()
        self.pushButton_17.hide()

        self.img = cv2.imread("./test.png", 0)
        self.img_copy = cv2.imread("./test_copy.png", 0)
        QtCore.QMetaObject.connectSlotsByName(method_tradition)

        self.pushButton_9.hide()
        self.pushButton_11.hide()
        self.pushButton_12.hide()
        self.pushButton_13.hide()
        self.pushButton_14.hide()
        #self.pushButton_16.hide()


    def slot_return(self):
        method_tradition.close()

    def slot_readme(self):
        QMessageBox.warning(self, '警告', '你不会自己看下边框里的提示嘛？？', QMessageBox.Yes)

    def slot_readimage(self):
        file = QFileDialog()
        file.setDirectory('E:\\leetcode\\pyqt_defect_detection\\png\\')  # 初始路径
        file.setNameFilter('图片文件(*.png)')
        file.exec_()
        image_path = file.selectedFiles()[0]  # 选择的png文件路径
        self.img = cv2.imread(image_path, 0)
        self.img_copy = cv2.imread(image_path, 0)
        cv2.imwrite("test.png", self.img)
        cv2.imwrite("test_copy.png", self.img_copy)
        print(image_path)
        self.textEdit.clear()
        if(image_path):
            pix = QtGui.QPixmap(image_path)
            self.label.setPixmap(pix)
            self.label.setScaledContents(True)

            self.pushButton_2.show()
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.pushButton_5.show()
            self.pushButton_6.show()
            self.pushButton_7.show()
            self.textEdit.append("请继续点击您想进行的操作")

    def slot_emphasize(self):
        #QMessageBox.warning(self, '警告', '该过程可能耗时10秒左右', QMessageBox.Yes)
        #QMessageBox.warning(self, '警告', '请耐心等待程序提示，再进行下一步操作', QMessageBox.Yes)
        self.textEdit.append("正在增强对比度")
        self.textEdit.append("请不要关闭系统")
        test = cv2.imread("./test.png", 0)
        emphasize(test)
        self.set_image()

    def slot_sharpen(self):
        self.textEdit.append("正在锐化")
        self.textEdit.append("请不要关闭系统")
        test = cv2.imread("./test.png", 0)
        lapmask = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], np.float32)
        src_lap = cv2.filter2D(test, -1, kernel=lapmask)
        cv2.imwrite("test.png", src_lap)
        self.set_image()

    def slot_findcontours(self):
        self.textEdit.append("正在搜索边缘")
        self.textEdit.append("请不要关闭系统")
        test = cv2.imread("./test.png", 0)

        contours, hierarchy = cv2.findContours(test, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if(contours):
            src = cv2.imread("./test_copy.png", 0)
            src_rgb = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
            cv2.drawContours(src_rgb, contours, -1, (255, 0, 0), 2)
            cv2.imwrite("./test_res.png", src_rgb)
            pix = QtGui.QPixmap("./test_res.png")
            self.label.setPixmap(pix)
            self.label.setScaledContents(True)
            self.textEdit.clear()
            self.textEdit.append("结果已保存，请重新选择文件")
        else:
            self.textEdit.clear()
            self.textEdit.append("没有找到合适的边缘轮廓")
            self.set_image()


    def slot_threshold(self):
        self.textEdit.clear()
        self.textEdit.append("请在框中输入阈值条件")
        self.textEdit.append("输入完成后点击确定")
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.pushButton_17.show()
        self.label_4.show()
        #test = cv2.imread("./test.png", 0)


    def slot_invert(self):
        self.textEdit.append("正在进行反色操作")
        self.textEdit.append("请不要关闭系统")
        test = cv2.imread("./test.png", 0)
        invert(test)
        self.set_image()

    def set_image(self):
        pix = QtGui.QPixmap("./test.png")
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)
        self.img = cv2.imread("./test.png", 0)

    def slot_blur(self):
        self.textEdit.append("正在对图像均值滤波")
        self.textEdit.append("请不要关闭系统")
        test = cv2.imread("./test.png", 0)
        img_blur = cv2.blur(test, (3, 3))
        cv2.imwrite("test.png", img_blur)
        self.set_image()

    #图片还原初始
    def slot_return_origin(self):
        cv2.imwrite("test.png", self.img_copy)
        self.set_image()

    #用户输入完阈值后，进行阈值分割
    def slot_confirm(self):
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.pushButton_17.hide()
        self.label_4.hide()
        min = int(self.lineEdit_2.text())
        max = int(self.lineEdit_3.text())
        test = cv2.imread("./test.png", 0)
        ret, th = cv2.threshold(test, min, max, cv2.THRESH_BINARY)
        cv2.imwrite("test.png", th)
        self.set_image()

    def retranslateUi(self, method_tradition):
        _translate = QtCore.QCoreApplication.translate
        method_tradition.setWindowTitle(_translate("method_tradition", "传统数字图像处理"))
        self.label.setText(_translate("method_tradition", "Image"))
        self.pushButton.setText(_translate("method_tradition", "操作说明"))
        self.pushButton_2.setText(_translate("method_tradition", "锐化"))
        self.pushButton_3.setText(_translate("method_tradition", "反色处理"))
        self.pushButton_4.setText(_translate("method_tradition", "均值滤波"))
        self.pushButton_5.setText(_translate("method_tradition", "阈值分割"))
        self.pushButton_6.setText(_translate("method_tradition", "增强对比度"))
        self.pushButton_7.setText(_translate("method_tradition", "轮廓提取"))
        self.pushButton_8.setText(_translate("method_tradition", "选择文件"))
        self.pushButton_9.setText(_translate("method_tradition", "备用4"))
        self.pushButton_10.setText(_translate("method_tradition", "还原"))
        self.pushButton_11.setText(_translate("method_tradition", "备用5"))
        self.pushButton_12.setText(_translate("method_tradition", "备用2"))
        self.pushButton_13.setText(_translate("method_tradition", "备用6"))
        self.pushButton_14.setText(_translate("method_tradition", "备用3"))
        self.pushButton_15.setText(_translate("method_tradition", "返回主界面"))
        self.pushButton_16.setText(_translate("method_tradition", "保存"))
        self.pushButton_17.setText(_translate("method_tradition", "确定"))
        #self.label_2.setText(_translate("method_tradition", "v1.0"))
        self.label_3.setText(_translate("method_tradition", "v1.0 智能缺陷检测系统"))
        self.label_4.setText(_translate("method_tradition", "阈值："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    method_tradition = QtWidgets.QDialog()
    ui = Ui_method_tradition()
    ui.setupUi(method_tradition)
    method_tradition.show()
    sys.exit(app.exec_())
