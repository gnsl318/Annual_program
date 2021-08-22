from datetime import date
from typing import List
from sqlalchemy.orm import Session
from models.base import *



def create_user(
    *,
    db : Session,
    name:str,
    position:str,
    part:str,
    start_date):

    if db.query(User).filter(User.name == name).first()==None:
        part_id=db.query(Part).filter(Part.part ==part).first().id
        position_id = db.query(Position).filter(Position.position==position).first().id
        new_user = User(
            name=name,
            position_id = position_id,
            part_id = part_id,
            start_date = start_date,
            status = True,
            annual_day = 0
        )
        db.add(new_user)
        db.commit()
        return new_user

def get_all_user(
    *,
    db:Session,
):
    user_info=db.query(User).join(Part,Position) 
    return user_info

def get_pp(
    *,
    db:Session,
    name:str
):
    user_info = db.query(User).filter(User.name==name).first()
    part = db.query(Part).filter(Part.id==user_info.part_id).first().part
    position = db.query(Position).filter(Position.id == user_info.position_id).first().position
    return part,position

def update_annual_day(
    *,
    db:Session,
    name:str,
    kind:str
):
    user = db.query(User).filter(User.name == name).first()
    if kind == "연차":
        user.annual_day -=  1
    elif kind == "반차":
        user.annual_day -= 0.5
    db.commit()
