from sqlalchemy.orm import Session
from models.base import Position


def get_all_position(
    *,
    db:Session,
):
    positions = db.query(Position).all()
    return positions