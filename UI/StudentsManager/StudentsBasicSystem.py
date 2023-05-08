# Form implementation generated from reading ui file 'StudentsBasicSystem.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal


class Ui_StudentsBasicManager(QtWidgets.QWidget):
    switched_to_student_manager_page = pyqtSignal()
    switched_to_student_add_page = pyqtSignal()
    switched_to_student_add_many_page = pyqtSignal()
    switched_to_students_find_page = pyqtSignal()
    switched_to_students_delete_page = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        # self.pushButton = QtWidgets.QPushButton(parent=Form)
        # self.pushButton.setGeometry(QtCore.QRect(400, 180, 230, 71))
        # font = QtGui.QFont()
        # font.setFamily("Adobe 黑体 Std R")
        # font.setPointSize(12)
        # self.pushButton.setFont(font)
        # self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 360, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 270, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 540, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 360, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_6.setGeometry(QtCore.QRect(700, 270, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        # self.pushButton_7 = QtWidgets.QPushButton(parent=Form)
        # self.pushButton_7.setGeometry(QtCore.QRect(700, 360, 231, 71))
        # font = QtGui.QFont()
        # font.setFamily("Adobe 黑体 Std R")
        # font.setPointSize(12)
        # self.pushButton_7.setFont(font)
        # self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_5.clicked.connect(self.switch_to_students_find_page)
        self.pushButton_3.clicked.connect(self.switch_to_student_add_page)
        self.pushButton_4.clicked.connect(self.switch_to_student_manager_page)
        self.pushButton_6.clicked.connect(self.switch_to_student_add_many_page)
        self.pushButton_2.clicked.connect(self.switch_to_students_delete_page)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.pushButton.setText(_translate("Form", "查看单名幼儿信息"))
        self.pushButton_2.setText(_translate("Form", "删除幼儿"))
        self.pushButton_3.setText(_translate("Form", "新增单名幼儿"))
        self.pushButton_4.setText(_translate("Form", "返回"))
        self.pushButton_5.setText(_translate("Form", "查看幼儿信息"))
        self.pushButton_6.setText(_translate("Form", "新增多名幼儿信息"))
        # self.pushButton_7.setText(_translate("Form", "删除多名幼儿"))

    def switch_to_student_manager_page(self):
        self.switched_to_student_manager_page.emit()

    def switch_to_student_add_page(self):
        self.switched_to_student_add_page.emit()

    def switch_to_student_add_many_page(self):
        self.switched_to_student_add_many_page.emit()

    def switch_to_students_find_page(self):
        self.switched_to_students_find_page.emit()

    def switch_to_students_delete_page(self):
        self.switched_to_students_delete_page.emit()
