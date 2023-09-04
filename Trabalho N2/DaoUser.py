# conect BD
from ModelUser import User
import sqlalchemy
from sqlalchemy.orm import sessionmaker


class DaoUser():

    def registros():
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session.query(User)


    def registro(id):
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session.query(User).filter_by(id=id).filter()

    def inserir(object):
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(object)
        session.commit()

    def update(object):
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(User).filter_by(id=object.id).filter().update({

                "userName": object.userName,
                "fullName": object.fullName,
                "password": object.password,
                "role": object.role
            
        })
        session.commit()

    def delete(id):
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        registro = session.query(User).filter_by(id=id).filter()
        session.delete(registro)
        session.commit()
        