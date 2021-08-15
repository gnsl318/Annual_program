import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate,QTime
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from db import session
from add_user import Add_user
from login import Login
from crud import *



BASE_DIR = os.getcwd().replace("src","templates")
main_ui_path = os.path.join(BASE_DIR,"main.ui").replace("\\","/")
form_class = uic.loadUiType(main_ui_path)[0]


class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.name,self.admin= self.login_page()
        self.setupUi(self)
        self._db = next(session.get_db())
        self.func()
        if self.admin:
            self.set_table()
        


    def func(self):
        self.start_date.setDate(QDate.currentDate())
        self.end_date.setDate(QDate.currentDate())
        self.start_time.setTime(QTime.currentTime())
        self.end_time.setTime(QTime.currentTime())
        if self.admin: 
            self.add_user_btn.clicked.connect(self.add_user)
        else:
            self.annual_table.setDisabled(True)
            self.add_user_btn.setDisabled(True)
        self.user_info(self.name)
        

    def login_page(self):
        Login_app = Login()
        Login_app.exec_()
        return Login_app.name,Login_app.admin
        

    def set_table(self):
        user_list = crud_user.get_all_user(db=self._db)
        self.annual_table.setColumnCount(5)
        self.annual_table.setRowCount(user_list.count())
        row = 0
        for user in user_list:
            if user.status:
                self.annual_table.setItem(row, 0, QTableWidgetItem(user.name))
                self.annual_table.setItem(row, 1, QTableWidgetItem(user.part.part))
                self.annual_table.setItem(row, 2, QTableWidgetItem(user.position.position))
                self.annual_table.setItem(row, 3, QTableWidgetItem(str(user.start_date)))
                self.annual_table.setItem(row, 4, QTableWidgetItem(str(user.annual_day)))
                row +=1

            

    def add_user(self):
        add_user_app = Add_user()
        add_user_app.exec_()
    
    def user_info(self,name):
        part,position = crud_user.get_pp(db=self._db,name=name)
        self.name_edit.setText(name)
        self.Position_edit.setText(position)
        self.Part_edit.setText(part)



    @staticmethod
    def show_message(message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec_()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())