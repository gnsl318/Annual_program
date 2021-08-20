from sqlalchemy.orm import Session
from models.base import Kind


def get_all_kind(
    *,
    db:Session,
):
    positions = db.query(Kind).all()
    return positions