from PyQt6 import QtWidgets, QtCore, QtGui

from Function.UserManager import UserManager


class Ui_AddUser(QtWidgets.QWidget):
    switched_to_UserManager = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(520, 180, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(520, 270, 61, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(660, 360, 131, 31))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(520, 360, 71, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(660, 180, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(660, 240, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 540, 230, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 540, 230, 70))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.switch_to_UserManager)
        self.pushButton.clicked.connect(self.add_user)
        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">用户名</span></p></body></html>"))
        self.label_2.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">密码</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "园长"))
        self.comboBox.setItemText(1, _translate("Form", "教师"))
        self.comboBox.setItemText(2, _translate("Form", "保健老师"))
        self.label_3.setText(
            _translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">权限</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_2.setText(_translate("Form", "返回"))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.pushButton.setFont(font)
        self.pushButton_2.setFont(font)

    def add_user(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        role = self.comboBox.currentIndex()
        if UserManager().add_User(username, password, role):
            QtWidgets.QMessageBox.information(self, "提示", "添加成功")
        else:
            QtWidgets.QMessageBox.information(self, "提示", "添加失败")

    def switch_to_UserManager(self):
        self.switched_to_UserManager.emit()
