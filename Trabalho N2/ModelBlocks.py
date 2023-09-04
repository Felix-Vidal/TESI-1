
import sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///sgad.db")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum

Base = declarative_base()

class Blocks(Base):
    __tablename__ = "blocks" 

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

Base.metadata.create_all(engine)