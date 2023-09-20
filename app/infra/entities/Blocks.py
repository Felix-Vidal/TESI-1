
from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from sqlalchemy import Column, Integer, String


class Blocks(Base):
    __tablename__ = "blocks" 

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())
