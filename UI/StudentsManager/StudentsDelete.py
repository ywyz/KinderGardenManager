# Form implementation generated from reading ui file 'StudentsDelete.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal

from Function.StudentsManager import StudentsManager


class Ui_StudentsDelete(QtWidgets.QWidget):
    switched_to_students_basic_info_page = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(350, 210, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(620, 230, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 450, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 450, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.switch_to_students_basic_info_page)
        self.pushButton.clicked.connect(self.deleteStudents)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "需删除幼儿的姓名："))
        self.pushButton.setText(_translate("Form", "确认删除"))
        self.pushButton_2.setText(_translate("Form", "返回"))

    def switch_to_students_basic_info_page(self):
        self.switched_to_students_basic_info_page.emit()

    def deleteStudents(self):
        name = self.lineEdit.text()
        stu = StudentsManager()
        if stu.del_stu_info(name):
            QtWidgets.QMessageBox.information(self, '提示', '删除成功！')
        else:
            QtWidgets.QMessageBox.information(self, '提示', '删除失败！')
