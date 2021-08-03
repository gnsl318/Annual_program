import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate,QTime
import os


BASE_DIR = os.getcwd()
login_ui_path = os.path.join(BASE_DIR,"templates/main.ui").replace("\\","/")
form_class = uic.loadUiType(login_ui_path)[0]


class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.func()


    def func(self):
        self.start_date.setDate(QDate.currentDate())
        self.end_date.setDate(QDate.currentDate())
        self.start_time.setTime(QTime.currentTime())
        self.end_time.setTime(QTime.currentTime())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())