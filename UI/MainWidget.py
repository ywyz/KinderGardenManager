# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainFunction(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainFunction):
        MainFunction.setObjectName("MainFunction")
        MainFunction.resize(1108, 858)
        self.pushButton = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton.setGeometry(QtCore.QRect(190, 180, 231, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 300, 231, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 430, 231, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 570, 231, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 180, 231, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 300, 231, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 430, 231, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=MainFunction)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 570, 231, 71))
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(MainFunction)
        QtCore.QMetaObject.connectSlotsByName(MainFunction)

    def retranslateUi(self, MainFunction):
        _translate = QtCore.QCoreApplication.translate
        MainFunction.setWindowTitle(_translate("MainFunction", "Form"))
        self.pushButton.setText(_translate("MainFunction", "账号管理"))
        self.pushButton_2.setText(_translate("MainFunction", "学生（幼儿园）信息管理"))
        self.pushButton_3.setText(_translate("MainFunction", "食堂管理"))
        self.pushButton_4.setText(_translate("MainFunction", "后勤管理"))
        self.pushButton_5.setText(_translate("MainFunction", "后勤管理"))
        self.pushButton_6.setText(_translate("MainFunction", "教学管理"))
        self.pushButton_7.setText(_translate("MainFunction", "导入导出数据"))
        self.pushButton_8.setText(_translate("MainFunction", "退出"))


