from infra.config.base import Base
from infra.config.connection import DBConnectionHandler
from sqlalchemy import Column, Integer, String, Enum
from infra.entities.ERole import ERole


class Users(Base):
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True)
    userName = Column(String(50), unique=True)
    fullName = Column(String(50))
    password = Column(String(50))
    role = Column(Enum(ERole))

def create_admin_user(session):
    admin_user = session.query(Users).filter_by(userName='admin').first()
    if not admin_user:
        admin_data = Users(userName='admin', fullName='Admin User', password='admin', role=ERole.ROLE_ADMIN)
        session.add(admin_data)
        session.commit()

with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())
    create_admin_user(db.session)


