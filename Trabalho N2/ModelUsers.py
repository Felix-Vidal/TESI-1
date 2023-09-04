import sqlalchemy

from ERole import ERole
engine = sqlalchemy.create_engine("sqlite:///sgad.db")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum

Base = declarative_base()

class Users(Base):
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True)
    userName = Column(String(50))
    fullName = Column(String(50))
    password = Column(String(50))
    role = Column(Enum(ERole))

Base.metadata.create_all(engine)
