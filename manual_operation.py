
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
import cv2
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_manual_operation(QtWidgets.QDialog):

    def __init__(self):
        super(Ui_manual_operation, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, manual_operation):
        manual_operation.setObjectName("manual_operation")
        manual_operation.resize(721, 349)
        manual_operation.setFixedSize(721, 349)

        manual_operation.setStyleSheet('''#manual_operation{

                                                                          border-bottom-left-radius:15px;
                                                                          border-bottom-right-radius:15px;
                                                                          border-image:url(pic/back1.png)
                                                                          }
                                                        ''')

        self.label = QtWidgets.QLabel(manual_operation)
        self.label.setGeometry(QtCore.QRect(20, 0, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton_5 = QtWidgets.QPushButton(manual_operation)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 70, 219, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(manual_operation)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 219, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(manual_operation)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 170, 219, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(manual_operation)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 220, 219, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(manual_operation)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 270, 219, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(manual_operation)
        self.textEdit.setGeometry(QtCore.QRect(250, 70, 441, 231))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(manual_operation)
        self.pushButton.clicked.connect(self.slot_readimage)
        self.pushButton_2.clicked.connect(self.slot_return)
        self.pushButton_5.clicked.connect(self.slot_readme)
        QtCore.QMetaObject.connectSlotsByName(manual_operation)

        self.pushButton_4.hide()
        self.pushButton_3.hide()

    def retranslateUi(self, manual_operation):
        _translate = QtCore.QCoreApplication.translate
        manual_operation.setWindowTitle(_translate("manual_operation", "手动拉伸对比度"))
        self.label.setText(_translate("manual_operation", "v1.0 智能缺陷检测系统"))
        self.pushButton_5.setText(_translate("manual_operation", "操作说明"))
        self.pushButton.setText(_translate("manual_operation", "选择文件"))
        self.pushButton_4.setText(_translate("manual_operation", "备用1"))
        self.pushButton_3.setText(_translate("manual_operation", "备用2"))
        self.pushButton_2.setText(_translate("manual_operation", "返回"))
        self.textEdit.setHtml(_translate("manual_operation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">点击选择文件按钮，进入图像操作视图</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">功能包括：对比度拉伸、图片局部缩放</span></p></body></html>"))

    def slot_readimage(self):
        file = QFileDialog()
        file.setDirectory('E:\\leetcode\\pyqt_defect_detection\\png\\')  # 初始路径
        file.setNameFilter('图片文件(*.png)')
        file.exec_()
        image_path = file.selectedFiles()[0]  # 选择的png文件路径
        print(image_path)

        # 调用pyqtgraph库中的函数实现 对比度拉伸
        pg.setConfigOptions(imageAxisOrder='row-major')
        imv = pg.ImageView()
        img = np.array(cv2.imread(image_path))
        pg.image(img)
        # 将上述窗口放到一个网格布局中
        grid = QGridLayout()
        grid.addWidget(imv, 0, 0)

    def slot_return(self):
        self.close()

    def slot_readme(self):
        QMessageBox.warning(self, '警告', '', QMessageBox.Yes)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manual_operation = QtWidgets.QDialog()
    ui = Ui_manual_operation()
    ui.setupUi(manual_operation)
    manual_operation.show()
    sys.exit(app.exec_())
