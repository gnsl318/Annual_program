from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from db.session import engine

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True, index=True)
  name = Column(String(20), unique=True)
  position_id = Column(Integer, ForeignKey("positions.id"))
  position = relationship('Position', foreign_keys=[position_id])
  part_id = Column(Integer, ForeignKey("parts.id"))
  part = relationship('Part', foreign_keys=[part_id])
  start_date = Column(Date)
  status = Column(Boolean)
  annual_day = Column(Integer)

class Position(Base):
  __tablename__ = 'positions'
  id = Column(Integer, primary_key=True, autoincrement=True, index=True)
  position = Column(String(20), unique=True)


class Part(Base):
  __tablename__ = 'parts'
  id = Column(Integer, primary_key=True, autoincrement=True, index=True)
  part = Column(String(20), unique=True)


if __name__ == "__main__":
  Base.metadata.create_all(bind=engine)