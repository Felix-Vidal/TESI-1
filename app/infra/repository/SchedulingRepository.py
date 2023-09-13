from infra.config.connection import DBConnectionHandler
from infra.entities.Schedulings import Schedulings
from infra.entities.Requesters import Requesters
from infra.entities.ClassRooms import ClassRooms
from infra.entities.Blocks import Blocks
class SchedulingRepository:

    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(Schedulings, Requesters, ClassRooms, Blocks).join(Schedulings, Requesters.id == Schedulings.requester).join(ClassRooms, ClassRooms.id == Schedulings.classRoom).join(Blocks, Blocks.id == ClassRooms.block).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Schedulings, Requesters, ClassRooms, Blocks).join(Schedulings, Requesters.id == Schedulings.requester).join(ClassRooms, ClassRooms.id == Schedulings.classRoom).join(Blocks, Blocks.id == ClassRooms.block).filter(Schedulings.id == id).first()
            return data

    def insert(requester, classRoom, dataTime):
        with DBConnectionHandler() as db:
            data= Schedulings(requester=requester, classRoom=classRoom, dateTime=dataTime)
            db.session.add(data)
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