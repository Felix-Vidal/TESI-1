from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from sqlalchemy import Column, Integer, String, Enum
from infra.entities.ERole import ERole


class Users(Base):
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True)
    userName = Column(String(50))
    fullName = Column(String(50))
    password = Column(String(50))
    role = Column(Enum(ERole))

with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())


