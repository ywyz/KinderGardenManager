# Form implementation generated from reading ui file 'StudentAddSingle2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal


class Ui_StudentAddSingle2(QtWidgets.QWidget):
    switched_to_students_basic_info_page = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 600, 230, 70))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 600, 230, 70))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(185, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(330, 100, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(160, 235, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 230, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(162, 170, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(330, 170, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(190, 300, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(parent=Form)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 290, 211, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(160, 360, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 350, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(163, 415, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 410, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(600, 270, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 250, 211, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_3 = QtWidgets.QComboBox(parent=Form)
        self.comboBox_3.setGeometry(QtCore.QRect(720, 110, 211, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(590, 110, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(560, 170, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(600, 220, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(parent=Form)
        self.label_13.setGeometry(QtCore.QRect(160, 470, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(720, 210, 211, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.comboBox_4 = QtWidgets.QComboBox(parent=Form)
        self.comboBox_4.setGeometry(QtCore.QRect(370, 470, 171, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(730, 160, 201, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(720, 310, 211, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(570, 320, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(parent=Form)
        self.label_12.setGeometry(QtCore.QRect(600, 380, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(720, 370, 211, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.switch_to_students_basic_info_page)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_2.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "第一监护人姓名"))
        self.label_2.setText(_translate("Form", "第一监护人证件号码"))
        self.label_3.setText(_translate("Form", "第一监护人证件类型"))
        self.comboBox.setItemText(0, _translate("Form", "居民身份证"))
        self.comboBox.setItemText(1, _translate("Form", "香港特区护照/身份证明"))
        self.comboBox.setItemText(2, _translate("Form", "澳门特区护照/身份证明"))
        self.comboBox.setItemText(3, _translate("Form", "台湾居民来往大陆通行证"))
        self.comboBox.setItemText(4, _translate("Form", "境外永久居住证"))
        self.comboBox.setItemText(5, _translate("Form", "其他"))
        self.label_4.setText(_translate("Form", "第一监护人关系"))
        self.comboBox_2.setItemText(0, _translate("Form", "父亲"))
        self.comboBox_2.setItemText(1, _translate("Form", "母亲"))
        self.comboBox_2.setItemText(2, _translate("Form", "继父或养父"))
        self.comboBox_2.setItemText(3, _translate("Form", "继母或养母"))
        self.comboBox_2.setItemText(4, _translate("Form", "祖父"))
        self.comboBox_2.setItemText(5, _translate("Form", "祖母"))
        self.comboBox_2.setItemText(6, _translate("Form", "外祖父"))
        self.comboBox_2.setItemText(7, _translate("Form", "外祖母"))
        self.comboBox_2.setItemText(8, _translate("Form", "哥哥"))
        self.comboBox_2.setItemText(9, _translate("Form", "姐姐"))
        self.comboBox_2.setItemText(10, _translate("Form", "其他亲属"))
        self.comboBox_2.setItemText(11, _translate("Form", "非亲属"))
        self.label_5.setText(_translate("Form", "第一监护人联系地址"))
        self.label_6.setText(_translate("Form", "第一监护人联系电话"))
        self.label_8.setText(_translate("Form", "第一监护人国籍"))
        self.lineEdit_6.setText(_translate("Form", "中国"))
        self.comboBox_3.setItemText(0, _translate("Form", "男"))
        self.comboBox_3.setItemText(1, _translate("Form", "女"))
        self.label_10.setText(_translate("Form", "第一监护人性别"))
        self.label_11.setText(_translate("Form", "第一监护人出生日期"))
        self.label_9.setText(_translate("Form", "第一监护人民族"))
        self.label_13.setText(_translate("Form", "第一监护人是否法定监护人"))
        self.lineEdit_10.setText(_translate("Form", "汉族"))
        self.comboBox_4.setItemText(0, _translate("Form", "是"))
        self.comboBox_4.setItemText(1, _translate("Form", "否"))
        self.label_7.setText(_translate("Form", "第一监护人工作单位"))
        self.label_12.setText(_translate("Form", "第一监护人职务"))

    def switch_to_students_basic_info_page(self):
        self.switched_to_students_basic_info_page.emit()

