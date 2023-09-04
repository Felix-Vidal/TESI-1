import sqlalchemy

from ERequester import ERequester
engine = sqlalchemy.create_engine("sqlite:///sgad.db")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey

Base = declarative_base()

class ClassRooms(Base):
    __tablename__ = "classRooms" 

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email= Column(String(50))
    telephone = Column(String(50))
    typeRequester = Column(Enum(ERequester))

Base.metadata.create_all(engine)
