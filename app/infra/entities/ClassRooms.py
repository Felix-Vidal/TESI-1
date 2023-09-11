from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from infra.entities.ERoom import ERoom


class ClassRooms(Base):
    __tablename__ = "classRooms" 

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    capacity = Column(Integer)
    block = Column(Integer, ForeignKey("blocks.id"))
    typeRoom = Column(Enum(ERoom))


with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())
