# Form implementation generated from reading ui file 'StudentAddMany.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QFileDialog
from Function.StudentsManager import StudentsManager

class Ui_StudentAddMany(QtWidgets.QWidget):
    switched_to_students_basic_info_page = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stu = StudentsManager()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 380, 230, 70))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 390, 230, 70))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(460, 200, 371, 51))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.load_data)
        self.pushButton_2.clicked.connect(self.switch_to_student_basic_page)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "导入文件"))
        self.pushButton_2.setText(_translate("Form", "返回"))

    def switch_to_student_basic_page(self):
        self.switched_to_students_basic_info_page.emit()

    def load_data(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "Excel Files (*.xlsx)")
        self.label.setText(filename)
        if self.stu.load_data(filename):
            QtWidgets.QMessageBox.information(self, '提示', '导入成功！')
        else:
            QtWidgets.QMessageBox.information(self, '提示', '导入失败！')

