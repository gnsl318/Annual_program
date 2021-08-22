from sqlalchemy.orm import Session
from models.base import *


def get_all_annual(
    *,
    db:Session,
):
    positions = db.query(Annual).all()
    return positions

def create_annual(
    *,
    db : Session,
    in_name:str,
    start_day,
    end_day,
    start_time,
    end_time,
    in_kind:str,
    annual_txt:str):

    name_id = db.query(User).filter(User.name == in_name).first().id
    kind_id = db.query(Kind).filter(Kind.kind==in_kind).first().id

    new_annual = Annual(
        name_id=name_id,
        start_day = start_day,
        end_day = end_day,
        start_time = start_time,
        end_time = end_time,
        kind_id = kind_id,
        annual_txt = annual_txt
    )
    db.add(new_annual)
    db.commit()
    return new_annual