from sqlalchemy.orm import Session
from models.base import Part


def get_all_part(
    *,
    db:Session,
):
    parts = db.query(Part).all()
    return parts
