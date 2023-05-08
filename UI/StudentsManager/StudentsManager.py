# Form implementation generated from reading ui file 'StudentsManager.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal


class Ui_StudentsManager(QtWidgets.QWidget):
    switched_to_main_function_page = pyqtSignal()
    switched_to_students_basic_info_page = pyqtSignal()
    switched_to_students_daily_attend_page = pyqtSignal()

    # switched_to_students_examination_info_page = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 270, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 270, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        # self.pushButton_3.setGeometry(QtCore.QRect(400, 360, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        # self.pushButton_3.setFont(font)
        # self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 360, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton.clicked.connect(self.switch_to_students_basic_info_page)
        self.pushButton_2.clicked.connect(self.switch_to_students_daily_attend_page)
        # self.pushButton_3.clicked.connect(self.switch_to_students_examination_info_page)
        self.pushButton_4.clicked.connect(self.switch_to_main_function_page)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "幼儿基础信息管理"))
        self.pushButton_2.setText(_translate("Form", "每日出勤信息管理"))
        # self.pushButton_3.setText(_translate("Form", "幼儿体检信息管理"))
        self.pushButton_4.setText(_translate("Form", "返回"))

    def switch_to_main_function_page(self):
        self.switched_to_main_function_page.emit()

    def switch_to_students_basic_info_page(self):
        self.switched_to_students_basic_info_page.emit()

    def switch_to_students_daily_attend_page(self):
        self.switched_to_students_daily_attend_page.emit()

# def switch_to_students_examination_info_page(self):
# self.switched_to_students_examination_info_page.emit()
