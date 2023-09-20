from infra.entities.ESituation import ESituation
from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from sqlalchemy import Column, Enum, ForeignKey, Integer, DateTime
from infra.entities.Requesters import Requesters
from infra.entities.ClassRooms import ClassRooms

class Schedulings(Base):
    __tablename__ = "schedulings" 

    id = Column(Integer, primary_key=True)
    requester = Column(Integer, ForeignKey("requesters.id"))
    classRoom = Column(Integer, ForeignKey("classRooms.id"))
    dateTime = Column(DateTime)
    situation = Column(Enum(ESituation), default=ESituation.MARKED)

with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())