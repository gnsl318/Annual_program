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





class Add_user(QDialog):
    def __init__(self):
        super().__init__()
        self._db = next(session.get_db())
        self.setupUI()


    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("사원추가")
        self.setWindowIcon(QIcon("icon.png"))

        name_label = QLabel("이름: ")
        part_label = QLabel("파트: ")
        position_label = QLabel("직위: ")
        start_date_label = QLabel("입사일: ")

        self.name_edit = QLineEdit()
        self.part_edit = QComboBox()
        self.position_edit = QComboBox()
        self.additem()
        self.start_date = QDateEdit()
        self.start_date.setDate(QDate.currentDate())

        self.pushButton1 = QPushButton("추가")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(self.name_edit, 0, 1)
        layout.addWidget(part_label, 1, 0)
        layout.addWidget(self.part_edit, 1, 1)
        layout.addWidget(position_label, 2, 0)
        layout.addWidget(self.position_edit, 2, 1)

        layout.addWidget(start_date_label, 3, 0)
        layout.addWidget(self.start_date,3, 1)
        layout.addWidget(self.pushButton1, 3, 2)
        

        self.setLayout(layout)
    def additem(self):
        parts = get_all_part(db=self._db)
        for part in parts:
            self.part_edit.addItem(part.part)
        positions = get_all_position(db=self._db)
        for position in positions:
            self.position_edit.addItem(position.position)

    
    @staticmethod
    def show_message(message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec_()

    def pushButtonClicked(self):
        self.user_name = self.name_edit.text()
        self.user_part = self.part_edit.currentText()
        self.user_position = self.position_edit.currentText()
        self.start_date = self.start_date.date().toPyDate()
        try:
            create_user(
                db=self._db,
                name = self.user_name,
                part = self.user_part,
                position = self.user_position,
                start_date = self.start_date
            )
            self.close()
        except:
            self.show_message("재시도")            
        
