# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

"""
主界面，系统所有窗口框架，
"""
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget, QMainWindow
from UI.MainWidget import Ui_MainFunction
from UI.UserManager.UserManagerUI import Ui_UserManager
from UI.UserManager.UserAddUI import Ui_AddUser
from UI.UserManager.UserFindUI import Ui_FindUser
from UI.UserManager.UserChangeUI import Ui_ChangeUser
from UI.Login.LoginWidget import Ui_Login
from UI.StudentsManager.StudentsManager import Ui_StudentsManager
from UI.StudentsManager.StudentsBasicSystem import Ui_StudentsBasicManager
from UI.StudentsManager.StudentAddSingle1 import Ui_StudentAddSingle1
from UI.StudentsManager.StudentAddSingle2 import Ui_StudentAddSingle2

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 使用QStackedWidget实现窗口切换
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_page = Ui_Login()                    # 登录界面
        self.main_function_page = Ui_MainFunction()     # 主功能界面
        self.userManager_page = Ui_UserManager()        # 用户管理界面
        self.addUser_page = Ui_AddUser()                # 添加用户界面
        self.findUser_page = Ui_FindUser()              # 查找用户界面
        self.changeUser_page = Ui_ChangeUser()          # 修改用户界面
        self.studentsManager_page = Ui_StudentsManager()# 学生管理界面
        self.studentsBasicManager_page = Ui_StudentsBasicManager()      # 学生基本信息管理界面
        self.studentAddSingle1_page = Ui_StudentAddSingle1()            # 学生基本信息添加界面1
        self.studentAddSingle2_page = Ui_StudentAddSingle2()            # 学生基本信息添加界面2

        # 将所有界面添加到QStackedWidget中
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.main_function_page)
        self.stacked_widget.addWidget(self.userManager_page)
        self.stacked_widget.addWidget(self.addUser_page)
        self.stacked_widget.addWidget(self.findUser_page)
        self.stacked_widget.addWidget(self.changeUser_page)
        self.stacked_widget.addWidget(self.studentsManager_page)
        self.stacked_widget.addWidget(self.studentsBasicManager_page)
        self.stacked_widget.addWidget(self.studentAddSingle1_page)
        self.stacked_widget.addWidget(self.studentAddSingle2_page)

        # 信号与槽
        self.login_page.login_success.connect(self.show_main_function)          # 登录成功，切换到主功能界面

        # 切换到用户管理界面
        self.main_function_page.switched_to_userManager.connect(self.show_user_manager)     # 主界面切换到用户管理界面
        self.userManager_page.switched_to_addUser.connect(self.show_addUser)                # 用户管理界面切换到添加用户界面
        self.userManager_page.switched_to_findUser.connect(self.show_findUser)              # 用户管理界面切换到查找用户界面
        self.userManager_page.switched_to_changeUser.connect(self.show_changeUser)              # 用户管理界面切换到修改用户界面
        self.userManager_page.switched_to_menu.connect(self.show_main_function)             # 用户管理界面切换到主功能界面
        self.addUser_page.switched_to_UserManager.connect(self.show_user_manager)           # 添加用户界面切换到用户管理界面
        self.findUser_page.switched_to_UserManager.connect(self.show_user_manager)          # 查找用户界面切换到用户管理界面
        self.changeUser_page.switched_to_UserManager.connect(self.show_user_manager)        # 修改用户界面切换到用户管理界面

        # 切换到学生管理界面
        self.main_function_page.switched_to_studentsmanager.connect(self.show_studentsManager)     # 主界面切换到学生管理界面
        self.studentsManager_page.switched_to_main_function_page.connect(self.show_main_function)  # 学生管理界面切换到主功能界面
        self.studentsManager_page.switched_to_students_basic_info_page.connect(self.show_studentsBasicManager_page)  # 学生管理界面切换到学生基本信息管理界面
        self.studentsBasicManager_page.switched_to_student_manager_page.connect(self.show_studentsManager)  # 学生基本信息管理界面切换到学生管理界面
        self.studentsBasicManager_page.switched_to_student_add_page.connect(self.show_studentAddSingle1_page)  # 学生基本信息管理界面切换到学生基本信息添加界面
        self.studentAddSingle1_page.switched_to_student_add_single2_page.connect(self.show_studentAddSingle2_page)
        self.studentAddSingle1_page.switched_to_students_basic_info_page.connect(self.show_studentsBasicManager_page)
        self.studentAddSingle2_page.switched_to_students_basic_info_page.connect(self.show_studentsBasicManager_page)

        # 设置初始界面
        self.stacked_widget.setCurrentWidget(self.login_page)


    def show_main_function(self):
        self.stacked_widget.setCurrentWidget(self.main_function_page)

    def show_user_manager(self):
        self.stacked_widget.setCurrentWidget(self.userManager_page)

    def show_addUser(self):
        self.stacked_widget.setCurrentWidget(self.addUser_page)

    def show_findUser(self):
        self.stacked_widget.setCurrentWidget(self.findUser_page)

    def show_changeUser(self):
        self.stacked_widget.setCurrentWidget(self.changeUser_page)

    def show_studentsManager(self):
        self.stacked_widget.setCurrentWidget(self.studentsManager_page)

    def show_studentsBasicManager_page(self):
        self.stacked_widget.setCurrentWidget(self.studentsBasicManager_page)

    def show_studentAddSingle1_page(self):
        self.stacked_widget.setCurrentWidget(self.studentAddSingle1_page)

    def show_studentAddSingle2_page(self):
        self.stacked_widget.setCurrentWidget(self.studentAddSingle2_page)

