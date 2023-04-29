# main.py
from UI.Window import Ui_MainWindow
import sys
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())

