import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate,QTime
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from db import session
from add_user import Add_user



BASE_DIR = os.getcwd().replace("src","templates")
main_ui_path = os.path.join(BASE_DIR,"main.ui").replace("\\","/")
form_class = uic.loadUiType(main_ui_path)[0]


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
        self.add_user_btn.clicked.connect(self.add_user)

    def add_user(self):
        add_user_app = Add_user()
        add_user_app.exec_()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())