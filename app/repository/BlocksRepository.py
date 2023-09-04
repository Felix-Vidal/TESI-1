# conect BD
from model.Blocks import Blocks
import sqlalchemy
from sqlalchemy.orm import sessionmaker


class BlocksRepository():

    def gets():
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session.query(Blocks)


    def get(id):
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session.query(Blocks).filter_by(id=id).filter()

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
        session.query(Blocks).filter_by(id=object.id).filter().update({

                "name": object.name
            
        })
        session.commit()

    def delete(id):
        engine = sqlalchemy.create_engine("sqlite:///sgad.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        registro = session.query(Blocks).filter_by(id=id).filter()
        session.delete(registro)
        session.commit()
        