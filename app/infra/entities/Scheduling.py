from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from sqlalchemy import Column, ForeignKey, Integer, DateTime

class Scheduling(Base):
    __tablename__ = "scheduling" 

    id = Column(Integer, primary_key=True)
    requester = Column(Integer, ForeignKey("requester.name"))
    classRoom = Column(Integer, ForeignKey("classRoom.name"))
    dateTime = Column(DateTime(timezone=False))

with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())