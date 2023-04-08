# main.py
from UI.Window import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from UI.LoginWidget import LoginUI
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())