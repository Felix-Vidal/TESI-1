import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
engine = sqlalchemy.create_engine('sqlite:///sgad.db')
Base = declarative_base()


def create():
    Base.metadata.creatre_all()
    


