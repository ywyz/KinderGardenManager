# Form implementation generated from reading ui file 'StudentsDailyAttend.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal

from Function.StudentsManager import StudentsManager


class Ui_StudentsDailyAttend(QtWidgets.QWidget):
    switched_to_student_manager_page = pyqtSignal()
    switched_to_student_find_daily_page = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(410, 170, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(410, 240, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(410, 310, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(410, 380, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(410, 460, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(410, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(620, 170, 231, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 240, 231, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(620, 380, 231, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(620, 470, 231, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(620, 310, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(620, 90, 231, 31))
        self.dateEdit.setCurrentSectionIndex(1)
        self.dateEdit.setDate(QtCore.QDate(2023, 5, 7))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 550, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 550, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(840, 550, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.comboBox.addItem("是")
        self.comboBox.addItem("否")
        self.pushButton.clicked.connect(self.submit_data)
        self.pushButton_2.clicked.connect(self.switched_to_student_find_daily_page)
        self.pushButton_3.clicked.connect(self.switched_to_student_manager_page)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "缺勤幼儿姓名"))
        self.label_2.setText(_translate("Form", "班级"))
        self.label_3.setText(_translate("Form", "是否病假"))
        self.label_4.setText(_translate("Form", "缺勤原因"))
        self.label_5.setText(_translate("Form", "联系人"))
        self.label_6.setText(_translate("Form", "日期"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_2.setText(_translate("Form", "查看缺勤幼儿"))
        self.pushButton_3.setText(_translate("Form", "返回"))

    def switch_to_student_manager_page(self):
        self.switched_to_student_manager_page.emit()

    def add_list(self):
        self.list = []
        self.list.append(self.dateEdit.text())
        self.list.append(self.lineEdit.text())
        self.list.append(self.lineEdit_2.text())
        self.list.append(self.comboBox.currentText())
        self.list.append(self.lineEdit_3.text())
        self.list.append(self.lineEdit_4.text())
        return self.list

    def submit_data(self):
        if self.add_list()[0] == "" or self.add_list()[1] == "" or self.add_list()[2] == "" or self.add_list()[
            3] == "" or self.add_list()[4] == "" or self.add_list()[5] == "":
            QtWidgets.QMessageBox.warning(self, '警告', '请填写完整信息！')
        else:
            self.stu = StudentsManager()
            if self.stu.stu_daily_attend(self.add_list()):
                QtWidgets.QMessageBox.information(self, '提示', '提交成功！')
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
            else:
                QtWidgets.QMessageBox.warning(self, '警告', '提交失败！')

    def switch_to_student_find_daily_page(self):
        self.switched_to_student_find_daily_page.emit()
