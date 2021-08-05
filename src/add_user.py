import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate,Qt
from db import session





class Add_user(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self._db = next(session.get_db())
        self.user_name = None

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("사원추가")
        self.setWindowIcon(QIcon("icon.png"))

        name_label = QLabel("이름: ")
        part_label = QLabel("파트: ")
        position_label = QLabel("직위: ")
        start_date_label = QLabel("입사일: ")

        self.name_edit = QLineEdit()
        self.part_edit = QLineEdit()
        self.position_edit = QLineEdit()

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

    def pushButtonClicked(self):
        self.user_name = self.name_edit.text()
        self.user_part = self.part_edit.text()
        self.user_position = self.position_edit.text()
        self.start_date = self.start_date.date().toString(Qt.ISODate)
        print(self.user_name,self.user_part,self.user_position,self.start_date)
        # try:
        #     create_user(
        #         db=self_db,
        #         user_name = self.user_name,
        #         user_part = self.user_part,
        #         user_position = self.user_position,
        #         start_date = self.start_date
        #     )
        # except:
        #     self.show_message("재시도")            
        self.close()
