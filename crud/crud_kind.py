from sqlalchemy.orm import Session
from models.base import Kind


def get_all_kind(
    *,
    db:Session,
):
    kind = db.query(Kind).all()
    return kind