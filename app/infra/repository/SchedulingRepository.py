from infra.config.connection import DBConnectionHandler
from infra.entities.Schedulings import Schedulings
class SchedulingRepository:

    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(Schedulings).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Schedulings).filter(Schedulings.id == id).first()
            return data

    def inserir(requester, classRoom, dataTime):
        with DBConnectionHandler() as db:
            data_isert = Schedulings(requester=requester, classRoom=classRoom, dateTime=dataTime)
            db.session.add(data_isert)
            db.session.commit()

    def update(id, requester, classRoom, dateTime):
        with DBConnectionHandler() as db:
            db.session.query(Schedulings).filter(Schedulings.id == id).update({

                "requester":requester, 
                "classRoom":classRoom, 
                "dateTime":dateTime
                
            })
            db.session.commit()

    def delete(id):
        with DBConnectionHandler() as db:
            db.session.query(Schedulings).filter(Schedulings.id == id).delete()
            db.session.commit()