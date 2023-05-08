# Form implementation generated from reading ui file 'StudentsFind.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QTableWidgetItem

from Function.StudentsManager import StudentsManager


class Ui_StudentsFind(QtWidgets.QWidget):
    switched_to_students_basic_info_page = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1261, 641))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(980, 650, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.switch_to_students_basic_info_page)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.load_students()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "返回"))

    def switch_to_students_basic_info_page(self):
        self.switched_to_students_basic_info_page.emit()

    def load_students(self):
        self.stu = StudentsManager()
        data = self.stu.get_students_info()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(33)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("学生号"))  # 设置表头
        self.tableWidget.setItem(0, 1, QTableWidgetItem("学生姓名"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("身份证件号码"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("户口所在地"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("现住址"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("出生地"))
        self.tableWidget.setItem(0, 6, QTableWidgetItem("国籍"))
        self.tableWidget.setItem(0, 7, QTableWidgetItem("民族"))
        self.tableWidget.setItem(0, 8, QTableWidgetItem("性别"))
        self.tableWidget.setItem(0, 9, QTableWidgetItem("是否港澳台侨外"))
        self.tableWidget.setItem(0, 10, QTableWidgetItem("是否独生子女"))
        self.tableWidget.setItem(0, 11, QTableWidgetItem("健康状况"))
        self.tableWidget.setItem(0, 12, QTableWidgetItem("就读方式"))
        self.tableWidget.setItem(0, 13, QTableWidgetItem("血型"))
        self.tableWidget.setItem(0, 14, QTableWidgetItem("是否孤儿"))
        self.tableWidget.setItem(0, 15, QTableWidgetItem("是否来自低保家庭"))
        self.tableWidget.setItem(0, 16, QTableWidgetItem("身份证件类型"))
        self.tableWidget.setItem(0, 16, QTableWidgetItem("是否留守儿童"))
        self.tableWidget.setItem(0, 17, QTableWidgetItem("是否残疾儿童"))
        self.tableWidget.setItem(0, 18, QTableWidgetItem("出生日期"))
        self.tableWidget.setItem(0, 19, QTableWidgetItem("入学日期"))
        self.tableWidget.setItem(0, 20, QTableWidgetItem("第一监护人姓名"))
        self.tableWidget.setItem(0, 21, QTableWidgetItem("第一监护人关系"))
        self.tableWidget.setItem(0, 22, QTableWidgetItem("第一监护人身份证件类型"))
        self.tableWidget.setItem(0, 23, QTableWidgetItem("第一监护人身份证件号码"))
        self.tableWidget.setItem(0, 24, QTableWidgetItem("第一监护人出生年月"))
        self.tableWidget.setItem(0, 25, QTableWidgetItem("第一监护人性别"))
        self.tableWidget.setItem(0, 26, QTableWidgetItem("第一监护人是否法定监护人"))
        self.tableWidget.setItem(0, 27, QTableWidgetItem("第一监护人工作单位"))
        self.tableWidget.setItem(0, 28, QTableWidgetItem("第一监护人职务"))
        self.tableWidget.setItem(0, 29, QTableWidgetItem("第一监护人国籍"))
        self.tableWidget.setItem(0, 30, QTableWidgetItem("第一监护人联系电话"))
        self.tableWidget.setItem(0, 31, QTableWidgetItem("第一监护人民族"))
        self.tableWidget.setItem(0, 32, QTableWidgetItem("第一监护人学历"))
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(value)))