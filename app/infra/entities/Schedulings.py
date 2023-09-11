from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from sqlalchemy import Column, ForeignKey, Integer, DateTime

class Schedulings(Base):
    __tablename__ = "schedulings" 

    id = Column(Integer, primary_key=True)
    requester = Column(Integer, ForeignKey("requesters.id"))
    classRoom = Column(Integer, ForeignKey("classRooms.id"))
    dateTime = Column(DateTime)

with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())