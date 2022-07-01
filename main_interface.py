# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *

from func_dcmtopng import*
from emphasize import*

from DeepLearning import*
from manual_operation import*
from method_tradition import*

import cv2

class Ui_main_interface(QtWidgets.QDialog):

    def __init__(self):
        super(Ui_main_interface, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, main_interface):
        main_interface.setObjectName("main_interface")
        main_interface.resize(1102, 655)

        main_interface.setStyleSheet('''#main_interface{
                                                                  
                                                                  border-bottom-left-radius:15px;
                                                                  border-bottom-right-radius:15px;
                                                                  border-image:url(pic/back1.png)
                                                                  }
                                                ''')

        self.pushButton_3 = QtWidgets.QPushButton(main_interface)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 100, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(main_interface)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 250, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_6 = QtWidgets.QPushButton(main_interface)
        self.pushButton_6.setGeometry(QtCore.QRect(740, 250, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(main_interface)
        self.pushButton_7.setGeometry(QtCore.QRect(530, 370, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(main_interface)
        self.pushButton_8.setGeometry(QtCore.QRect(740, 100, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_10 = QtWidgets.QPushButton(main_interface)
        self.pushButton_10.setGeometry(QtCore.QRect(530, 100, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(main_interface)
        self.pushButton_11.setGeometry(QtCore.QRect(320, 370, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")

        self.label = QtWidgets.QLabel(main_interface)
        self.label.setGeometry(QtCore.QRect(20, 100, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(main_interface)
        self.label_2.setGeometry(QtCore.QRect(80, 250, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton_9 = QtWidgets.QPushButton(main_interface)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 250, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton = QtWidgets.QPushButton(main_interface)
        self.pushButton.setGeometry(QtCore.QRect(890, 570, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.label_3 = QtWidgets.QLabel(main_interface)
        self.label_3.setGeometry(QtCore.QRect(80, 370, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton_15 = QtWidgets.QPushButton(main_interface)
        self.pushButton_15.setGeometry(QtCore.QRect(890, 500, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")

        self.label_5 = QtWidgets.QLabel(main_interface)
        self.label_5.setGeometry(QtCore.QRect(50, 530, 491, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.pushButton_16 = QtWidgets.QPushButton(main_interface)
        self.pushButton_16.setGeometry(QtCore.QRect(320, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(main_interface)
        self.pushButton_17.setGeometry(QtCore.QRect(530, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")

        self.pushButton_18 = QtWidgets.QPushButton(main_interface)
        self.pushButton_18.setGeometry(QtCore.QRect(740, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")

        self.retranslateUi(main_interface)
        QtCore.QMetaObject.connectSlotsByName(main_interface)

        #
        self.pushButton_18.clicked.connect(self.slot_onebutton)
        self.pushButton_6.clicked.connect(self.slot_DeepLearning)
        self.pushButton_7.clicked.connect(self.slot_OpenResultTxt)
        self.pushButton_11.clicked.connect(self.slot_ViewResult)
        self.pushButton_9.clicked.connect(self.slot_ManualOperation)
        self.pushButton_4.clicked.connect(self.slot_MethodTradition)
        self.pushButton.clicked.connect(self.slot_Close)

    def retranslateUi(self, main_interface):
        _translate = QtCore.QCoreApplication.translate
        main_interface.setWindowTitle(_translate("main_interface", "Welcome"))
        self.pushButton_3.setText(_translate("main_interface", "数据格式转换"))
        self.pushButton_4.setText(_translate("main_interface", "传统数字图像处理"))
        self.pushButton_6.setText(_translate("main_interface", "深度学习检测"))
        self.pushButton_7.setText(_translate("main_interface", "检测报告查询"))
        self.pushButton_8.setText(_translate("main_interface", "标签去噪"))
        self.pushButton_10.setText(_translate("main_interface", "图像增强"))
        self.pushButton_11.setText(_translate("main_interface", "结果可视化"))
        self.label.setText(_translate("main_interface", "图像预处理工具库："))
        self.label_2.setText(_translate("main_interface", "缺陷检测方法："))
        self.pushButton_9.setText(_translate("main_interface", "手动对比度拉伸"))
        self.pushButton.setText(_translate("main_interface", "关闭系统"))
        self.label_3.setText(_translate("main_interface", "检测结果查询："))
        self.pushButton_15.setText(_translate("main_interface", "操作说明"))
        self.label_5.setText(_translate("main_interface", "V1.0 智能缺陷检测系统"))
        self.pushButton_16.setText(_translate("main_interface", "数据增强"))
        self.pushButton_17.setText(_translate("main_interface", "姿态矫正"))
        self.pushButton_18.setText(_translate("main_interface", "一键预处理"))

    def slot_worklog_out(self):
        f = "./log.txt"
        a = 1
        t = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        with open(f, "a") as file:
            for i in range(a):
                file.write("操作员：" + "cyh" + " 于" + t + "退出操作界面"  + "\n")
                # 退出界面后 记录log.txt中进行分割
                file.write("—— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——" + "\n")
                file.write(" " + "\n")
                file.write(" " + "\n")
            a += 1
            file.close()


    def slot_Close(self):
        self.slot_worklog_out()
        main_interface.close()

    def slot_onebutton(self):
        #第一步将 dcm 转成 png 放在了同目录png文件夹下
        PNG_generate()
        #第二步将 图像增强 保存至empha文件夹下
        emphasize()
        QMessageBox.warning(self, '提示', '预处理已完成', QMessageBox.Yes)

    def slot_ManualOperation(self):
        main_interface.hide()
        ui_manual_operation.show()
        ui_manual_operation.exec_()
        main_interface.show()

    def slot_DeepLearning(self):
        main_interface.hide()
        ui_DeepLearning.show()
        ui_DeepLearning.exec_()
        main_interface.show()

    def slot_OpenResultTxt(self):
        file = QFileDialog()
        file.setDirectory('E:\\leetcode\\pyqt_defect_detection\\')  # 初始路径
        file.setNameFilter('文本文件(*.txt)')
        file.exec_()

    def slot_ViewResult(self):
        file = QFileDialog()
        file.setDirectory('E:\\leetcode\\pyqt_defect_detection\\result\\')  # 初始路径
        file.setNameFilter('图片文件(*.jpg)')
        file.exec_()
        image_path = file.selectedFiles()[0]  # 选择的png文件路径
        print(image_path)
        img_res = cv2.imread(image_path)
        cv2.imshow("result", img_res)
        cv2.waitKey(0)

    def slot_MethodTradition(self):
        main_interface.hide()
        ui_method_tradition.show()
        ui_method_tradition.exec_()
        main_interface.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_interface = QtWidgets.QDialog()
    ui = Ui_main_interface()

    ui_DeepLearning = Ui_DeepLearning()
    ui_manual_operation = Ui_manual_operation()
    ui_method_tradition = Ui_method_tradition()

    ui.setupUi(main_interface)
    main_interface.show()
    sys.exit(app.exec_())
