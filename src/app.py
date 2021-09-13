import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate,QTime
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from db import session
from add_user import Add_user
from edit_user import Edit_user
from login import Login
from crud.crud_user import *
from crud.crud_annual import *
import pandas as pd



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
            self.edit_user_btn.clicked.connect(self.edit_user)
            self.download_btn.clicked.connect(self.download)
        else:
            self.annual_table.setDisabled(True)
            self.add_user_btn.setDisabled(True)
            self.download_btn.setDisabled(True)
        self.user_info(self.name)
        self.save_btn.clicked.connect(self.save)
        
    def save(self):
        button_list=[self.radioButton_1,self.radioButton_2,self.radioButton_3,self.radioButton_4,self.radioButton_5]
        for button in button_list:
            if button.isChecked():
                create_annual(db=self._db,in_name=self.name,start_day=self.start_date.text(),end_day=self.end_date.text(),
                start_time=self.start_time.text(),end_time=self.end_time.text(),in_kind=button.text(),annual_txt=self.reason_text.toPlainText())
                update_annual_day(db=self._db,name=self.name,kind=button.text())
                if self.admin:
                    self.set_table()
    
    
    def login_page(self):
        Login_app = Login()
        Login_app.exec_()
        return Login_app.name,Login_app.admin
        

    def set_table(self):
        self.user_list = get_all_user(db=self._db)
        self.annual_table.setColumnCount(5)
        self.annual_table.setRowCount(self.user_list.count())
        row = 0
        
        
        for user in self.user_list:
            if user.status:
                self.annual_table.setItem(row, 0, QTableWidgetItem(user.name))
                self.annual_table.setItem(row, 1, QTableWidgetItem(user.part.part))
                self.annual_table.setItem(row, 2, QTableWidgetItem(user.position.position))
                self.annual_table.setItem(row, 3, QTableWidgetItem(str(user.start_date)))
                self.annual_table.setItem(row, 4, QTableWidgetItem(str(user.annual_day)))
                row +=1
                
    def edit_user(self):
        edit_user_app = Edit_user()
        edit_user_app.exec_()

            

    def add_user(self):
        add_user_app = Add_user()
        add_user_app.exec_()
    
    def user_info(self,name):
        self.part,self.position = get_pp(db=self._db,name=name)
        self.name_edit.setText(name)
        self.Position_edit.setText(self.position)
        self.Part_edit.setText(self.part)

    def download(self):
        df = pd.DataFrame(columns =['이름', '부서', '직위','입사일','연차 수'])
        for num,user in enumerate(self.user_list):
            if user.status:
                df.loc[num] = user.name , user.part.part , user.position.position , str(user.start_date) , str(user.annual_day)
        df.to_excel("연차정보.xlsx")
    
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