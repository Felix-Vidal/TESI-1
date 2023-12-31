from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from infra.entities.ERequester import ERequester

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import aliased

class Requesters(Base):
    __tablename__ = "requesters" 

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email= Column(String(50))
    telephone = Column(String(50))
    typeRequester = Column(Enum(ERequester))

with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())

