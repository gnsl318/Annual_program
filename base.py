from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from db.session import engine

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True)
    # images = relationship("Image", back_populates="users")
    is_manager = Column(Boolean)
    is_worker = Column(Boolean)
    is_inspector = Column(Boolean)
    field_id = Column(Integer, ForeignKey("field.id"))
    field_of_work = relationship("Field", foreign_keys=[field_id])

    created_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
    )
    updated_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
        onupdate=func.now() + datetime.timedelta(hours=9),
    )


class Image(Base):
    __tablename__ = "image"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image_name = Column(String, unique=True)
    manager_id = Column(Integer, ForeignKey("user.id"))
    worker_id = Column(Integer, ForeignKey("user.id"))
    field_id = Column(Integer, ForeignKey("field.id"))
    is_finish_work = Column(Boolean, default=False)
    managers = relationship("User", foreign_keys=[manager_id])
    workers = relationship("User", foreign_keys=[worker_id])
    fields = relationship("Field", foreign_keys=[field_id])
    labels = relationship("Label", back_populates="images")

    created_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
    )
    updated_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
        onupdate=func.now() + datetime.timedelta(hours=9),
    )


class Label(Base):
    __tablename__ = "label"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    image_id = Column(Integer, ForeignKey("image.id"))
    images = relationship("Image", back_populates="labels")

    before_cnt = Column(Integer, default=0)
    after_cnt = Column(Integer, default=0)

    created_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
    )
    updated_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
        onupdate=func.now() + datetime.timedelta(hours=9),
    )


class Field(Base):
    __tablename__ = "field"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    main_field = Column(String)
    sub_field = Column(String, nullable=True)
    created_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
    )
    updated_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
        onupdate=func.now() + datetime.timedelta(hours=9),
    )


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image_id = Column(Integer, ForeignKey("image.id"), index=True)
    images = relationship("Image", foreign_keys=[image_id])
    inspector_id = Column(Integer, ForeignKey("user.id"), index=True)
    inspectors = relationship("User", foreign_keys=[inspector_id])

    comment = Column(String, nullable=True)

    created_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
    )
    updated_at = Column(
        DateTime,
        default=func.now() + datetime.timedelta(hours=9),
        onupdate=func.now() + datetime.timedelta(hours=9),
    )


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
