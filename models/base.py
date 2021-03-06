from sqlalchemy import Column, Integer, String, ForeignKey, Time, func, Boolean, Date,Float
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
  annual_day = Column(Float)

class Annual(Base):
  __tablename__ = "annuals"
  id = Column(Integer, primary_key = True, autoincrement=True,index=True)
  name_id = Column(Integer, ForeignKey("users.id"))
  start_day = Column(Date)
  end_day = Column(Date)
  start_time = Column(Time)
  end_time = Column(Time)
  kind_id = Column(Integer,ForeignKey("kinds.id"))
  annual_txt = Column(String(100))
  
class Kind(Base):
  __tablename__ = "kinds"
  id = Column(Integer, primary_key = True, autoincrement=True,index=True)
  kind = Column(String(20), unique=True)
  

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