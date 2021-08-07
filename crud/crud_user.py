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

