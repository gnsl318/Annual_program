from datetime import date
from typing import List
from sqlalchemy.orm import Session
from models.base import user,part,position

def get_multi(*,db:Session) -> List[User]:
    return db.query(user,part,position).join(part,position)

def create_user(*,db:Session):
    if db.query(user).fileter(user.name == user_name).first():
        return False
    else:
        db.obj = user(
            name=user_name,
            position = user_position,
            part = user_part,
            start_date = start_date,
            status = True
        )
        db.add(db.obj)
        db.commit()
        return db_obj

