import sqlalchemy

from ERoom import ERoom
engine = sqlalchemy.create_engine("sqlite:///sgad.db", echo=True)

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey

Base = declarative_base()

class ClassRooms(Base):
    __tablename__ = "classRooms" 

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    capacity = Column(Integer)
    block = Column(Integer, ForeignKey("blocks.name"))
    typeRoom = Column(Enum(ERoom))

Base.metadata.create_all(engine)
