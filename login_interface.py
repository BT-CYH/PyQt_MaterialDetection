from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
#加载其它界面
from main_interface import*
from DeepLearning import*


class Ui_login_interface(QtWidgets.QDialog):    #QMainWindow
    def setupUi(self, login_interface):
        login_interface.setObjectName("login_interface")
        login_interface.resize(1100, 700)
        login_interface.setFixedSize(1100, 700)

        '''
        优化窗口设计
        '''
        login_interface.setWindowOpacity(1)
        login_interface.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        #添加界面的背景图片
        #login_interface.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #login_interface.setStyleSheet("#login_interface{border-image:url(pic/monster.jpg)}")
        #background: orange
        #border-image:url(pic/sand.jpg)

        login_interface.setStyleSheet('''#login_interface{
                                                          border-top-left-radius:15px;
                                                          border-top-right-radius:15px;
                                                          border-bottom-left-radius:15px;
                                                          border-bottom-right-radius:15px;
                                                          border-image:url(pic/back1.png)
                                                          }
                                        ''')


        self.pushButton = QtWidgets.QPushButton(login_interface)
        self.pushButton.setGeometry(QtCore.QRect(970, 600, 111, 45))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(login_interface)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 600, 121, 45))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(login_interface)
        self.label.setGeometry(QtCore.QRect(40, 460, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(login_interface)
        self.label_2.setGeometry(QtCore.QRect(70, 520, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(login_interface)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setFamily('微软雅黑')
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(login_interface)
        self.lineEdit.setGeometry(QtCore.QRect(145, 480, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(login_interface)
        self.lineEdit_2.setGeometry(QtCore.QRect(145, 540, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")


        #登入按钮
        self.pushButton_3 = QtWidgets.QPushButton(login_interface)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 600, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setFamily('宋体')
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.textEdit = QtWidgets.QTextEdit(login_interface)
        self.textEdit.setGeometry(QtCore.QRect(145, 600, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")


        self.retranslateUi(login_interface)
        self.pushButton.clicked.connect(login_interface.close)
        self.pushButton_3.clicked.connect(self.slot_login)
        self.pushButton_2.clicked.connect(self.slot_openlog)


        #用户名与密码
        self.UserName = "cyh"
        self.Password = "1234"

    def retranslateUi(self, login_interface):
        _translate = QtCore.QCoreApplication.translate
        login_interface.setWindowTitle(_translate("login_interface", "Login"))
        self.pushButton.setText(_translate("login_interface", "关闭系统"))
        self.label.setText(_translate("login_interface", "用户名："))
        self.label_2.setText(_translate("login_interface", "密码："))
        self.label_3.setText(_translate("login_interface", "v1.0 智能缺陷检测系统"))
        self.pushButton_2.setText(_translate("login_interface", "工作日志"))
        self.pushButton_3.setText(_translate("login_interface", "登入"))



    #退出系统并写入工作日志
    def slot_close(self):
        self.slot_worklog_out()
        login_interface.close()

    #每次登入成功时，自动写入工作日志
    def slot_worklog(self):
        f = "./log.txt"
        a = 1
        Strid = self.lineEdit.text()
        Strpwd = self.lineEdit_2.text()
        id = str(Strid)
        pwd = str(Strpwd)
        t = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        with open(f, "a") as file:
            for i in range(a):
                file.write("操作员：" + id + " 于" + t + "登入主界面"  + "\n")
            a += 1
            file.close()

    def slot_worklog_out(self):
        f = "./log.txt"
        a = 1
        Strid = self.lineEdit.text()
        Strpwd = self.lineEdit_2.text()
        id = str(Strid)
        pwd = str(Strpwd)
        t = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        with open(f, "a") as file:
            for i in range(a):
                file.write("操作员：" + id + " 于" + t + "退出操作界面"  + "\n")
                # 退出界面后 记录log.txt中进行分割
                file.write("—— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——" + "\n")
                file.write(" " + "\n")
                file.write(" " + "\n")
            a += 1
            file.close()

    #打开工作日志
    def slot_openlog(self):
        pass


    def slot_readme(self):
        res = QMessageBox.information(self, '操作说明',
                                '预处理工具用于图片格式转换dcm--png\n'
                                '检测方法包括四种：手动拉伸对比度、传统算法、机器学习、深度学习\n'
                                '未完待续 - -'
                                '请点击Yes结束该对话框', QMessageBox.Yes | QMessageBox.No)

        if(res == 65536):  #选择了no
            QMessageBox.warning(self, '警告', '', QMessageBox.Yes)

    #用户名与密码匹配函数
    def slot_login(self):
        if (self.lineEdit.text() == self.UserName and self.lineEdit_2.text() == self.Password):
            self.textEdit.setText("登陆成功")
            self.slot_worklog() #登入成功，即写入工作日志
            #隐藏登入界面控件，显示主画面控件
            self.jump_main_interface()



        elif (self.lineEdit.text() != self.UserName):
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.textEdit.setText("帐户错误")
        elif (self.lineEdit_2.text() != self.Password):
            self.lineEdit_2.setText("")
            self.textEdit.setText("密码错误")


    def jump_main_interface(self):
        login_interface.hide()
        #ui_main_interface.show()
        #ui_main_interface.exec_()
        #login_interface.show()
        subprocess.Popen('python main_interface.py', shell=True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_interface = QtWidgets.QDialog()


    ui = Ui_login_interface()
    ui_main_interface = Ui_main_interface()




    ui.setupUi(login_interface)


    login_interface.show()
    sys.exit(app.exec_())
