# Form implementation generated from reading ui file 'LoginWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
"""
Created on Fri Jun 18 15:00:00 2021
登录界面，用于登录系统，使用信号判断登录是否成功，登录成功即跳转到主界面
"""

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget

from Function.Login import Login


class Ui_Login(QWidget):
    login_success = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920,1080)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(700, 180, 391, 51))
        self.label.setObjectName("label")
        self.label.setText("欢迎使用幼儿园信息管理系统")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(600, 320, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("用户名")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(700, 310, 211, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(600, 420, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("密  码")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(700, 410, 211, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(700, 570, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("登录")
        self.pushButton.clicked.connect(self.login)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def login(self):
        """
        登录
        :return:
        """
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if Login().login(username, password):
            self.login_success.emit()
        else:
            self.label.setText("登录失败")
