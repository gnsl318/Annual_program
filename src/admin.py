import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate,Qt
from db import session
from crud.crud_user import *
from crud.crud_part import *
from crud.crud_position import *


class Admin(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("관리자")
        self.setWindowIcon(QIcon("icon.png"))
        
        
        id_label = QLabel("ID: ")
        self.id_edit = QLineEdit()
        
        password_label = QLabel("PASSWORD: ")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("로그인")
        self.login_btn.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(id_label, 0, 0)
        layout.addWidget(self.id_edit, 0, 1)
        layout.addWidget(password_label,1,0)
        layout.addWidget(self.password_edit,1,1)
        layout.addWidget(self.login_btn,2,1)
        self.setLayout(layout)
        
    @staticmethod
    def show_message(message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec_()

    def pushButtonClicked(self):
        self.id = self.id_edit.text()
        self.password = self.password_edit.text()
        admin_id,admin_password,password =session.get_admin()
        if self.password == admin_password and self.id == admin_id:
            self.id = "admin"
            self.close()
            return self.id
        elif self.password == password:
            self.close()
            return self.id
        else:
            self.show_message("로그인 실패")
