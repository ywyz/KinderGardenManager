# Form implementation generated from reading ui file 'UserChangeUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
"""
    修改用户信息界面，包含修改用户信息和删除用户两个功能
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from Function.UserManager import UserManager

switched_to_UserManager = QtCore.pyqtSignal()


class Ui_ChangeUser(QtWidgets.QWidget):
    """
    修改用户信息界面
    """
    switched_to_UserManager = QtCore.pyqtSignal()                   # 切换到用户管理界面

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280,720)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(660, 180, 211, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(420, 180, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(420, 270, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(660, 270, 211, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 650, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.delete_User)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 650, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.switch_to_UserManager)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(420, 360, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(660, 360, 211, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 650, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.change_User)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(420, 450, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(660, 450, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setCurrentText("教师")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请输入想要修改或删除的用户名"))
        self.label_2.setText(_translate("Form", "请输入该用户的密码"))
        self.pushButton.setText(_translate("Form", "确认删除"))
        self.pushButton_2.setText(_translate("Form", "返回"))
        self.label_3.setText(_translate("Form", "请输入新密码"))
        self.pushButton_3.setText(_translate("Form", "确认修改"))
        self.label_4.setText(_translate("Form", "新的权限"))
        self.comboBox.setItemText(0, _translate("Form", "园长"))
        self.comboBox.setItemText(1, _translate("Form", "教师"))
        self.comboBox.setItemText(2, _translate("Form", "保健老师"))

    def switch_to_UserManager(self):
        """切换到用户管理界面"""
        self.switched_to_UserManager.emit()

    def delete_User(self):
        """删除用户"""
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        user = UserManager()
        if user.delete_User(self.username, self.password):
            QtWidgets.QMessageBox.information(self, '提示', '删除成功')
        else:
            QtWidgets.QMessageBox.information(self, '提示', '删除失败')

    def change_User(self):
        """修改用户"""
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.new_password = self.lineEdit_3.text()
        self.role = self.comboBox.currentIndex()
        user = UserManager()
        if user.change_User(self.username, self.password, self.new_password, self.role):
            QtWidgets.QMessageBox.information(self, '提示', '修改成功')
        else:
            QtWidgets.QMessageBox.information(self, '提示', '修改失败')




