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





class Edit_user(QDialog):
    def __init__(self):
        super().__init__()
        self._db = next(session.get_db())
        self.setupUI()


    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("사원관리")

        name_label = QLabel("이름: ")
        part_label = QLabel("파트: ")
        position_label = QLabel("직위: ")
        start_date_label = QLabel("입사일: ")
        annual_day_label = QLabel("연차 수")
        state_label = QLabel("상태:")

        self.name_edit = QComboBox()
        self.part_edit = QLineEdit()
        self.position_edit = QLineEdit()
        self.setuser()
        self.start_date = QDateEdit()
        self.annual_day_edit = QLineEdit()
        self.state_edit = QLineEdit()

        self.edit_save_btn = QPushButton("저장")
        self.edit_save_btn.clicked.connect(self.saveButtonClicked)
        self.search_btn = QPushButton("검색")
        self.search_btn.clicked.connect(self.searchButtonClicked)
        self.state_btn = QPushButton("퇴사")
        self.state_btn.clicked.connect(self.updatestate)
        self.up_annual_btn = QPushButton("연차 추가")
        self.up_annual_btn.clicked.connect(self.up_annual)
        self.down_annual_btn = QPushButton("연차 삭감")
        self.down_annual_btn.clicked.connect(self.down_annual)


        layout = QGridLayout()
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(self.name_edit, 0, 1)
        layout.addWidget(part_label, 1, 0)
        layout.addWidget(self.search_btn, 0, 2)
        layout.addWidget(self.part_edit, 1, 1)
        layout.addWidget(position_label, 2, 0)
        layout.addWidget(self.position_edit, 2, 1)
        layout.addWidget(start_date_label, 3, 0)
        layout.addWidget(self.start_date,3, 1)
        layout.addWidget(annual_day_label, 4, 0)
        layout.addWidget(self.annual_day_edit, 4, 1)
        layout.addWidget(state_label, 5, 0)
        layout.addWidget(self.state_edit, 5, 1)
        layout.addWidget(self.state_btn, 5 ,2)
        layout.addWidget(self.up_annual_btn,6, 0)
        layout.addWidget(self.down_annual_btn,6, 1)
        layout.addWidget(self.edit_save_btn, 6, 2)
        self.setLayout(layout)

    def setuser(self):
        self.user_info = get_all_user(db=self._db)
        for name in self.user_info:
            if name.status:
                self.name_edit.addItem(name.name)

    @staticmethod
    def show_message(message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec_()

    def saveButtonClicked(self):
        self.user_name = self.name_edit.currentText()
        self.user_part = self.part_edit.text()
        self.user_position = self.position_edit.text()
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
        
    def searchButtonClicked(self):
        self.name = self.name_edit.currentText()
        user = get_user(db=self._db,name=self.name)
        self.position_edit.setText(user.position.position)
        self.part_edit.setText(user.part.part)
        self.start_date.setDate(user.start_date)
        self.annual_day_edit.setText(str(user.annual_day))
        if user.status:
            self.state_edit.setText("재직중")
        else:
            self.state_edit.setText("퇴사")
    
    def up_annual(self):
        update_total_annual(db=self._db,edit="up")
    def down_annual(self):
        update_total_annual(db=self._db,edit="down")

    def updatestate(self):
        update_state(db=self._db,name=self.name)
        self.state_edit.setText("퇴사")
