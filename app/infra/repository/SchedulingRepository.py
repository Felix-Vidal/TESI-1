from infra.config.connection import DBConnectionHandler
from infra.entities.Schedulings import Schedulings
from infra.entities.Requesters import Requesters
from infra.entities.ClassRooms import ClassRooms
from infra.entities.Blocks import Blocks
from infra.entities.ESituation import ESituation
from sqlalchemy import and_, or_
class SchedulingRepository:
    
    def checkTime(classRoom, dateTime, schedulings=None):
        data = None
        with DBConnectionHandler() as db:
            if schedulings:
                data = db.session.query(Schedulings).filter(and_(Schedulings.classRoom == classRoom, Schedulings.dateTime == dateTime, Schedulings.id != schedulings, Schedulings.situation == ESituation.MARKED)).all()
            else:
                data = db.session.query(Schedulings).filter(and_(Schedulings.classRoom == classRoom, Schedulings.dateTime == dateTime, Schedulings.situation == ESituation.MARKED)).all()

        if len(data) == 0:
            return True
        
        return False

    def gets(searchTerm=None):
        with DBConnectionHandler() as db:
            if searchTerm == None:
                data = db.session.query(Schedulings, Requesters, ClassRooms, Blocks).join(Schedulings, Requesters.id == Schedulings.requester).join(ClassRooms, ClassRooms.id == Schedulings.classRoom).join(Blocks, Blocks.id == ClassRooms.block).all()
                
            else:
                data = db.session.query(Schedulings, Requesters, ClassRooms, Blocks).join(Schedulings, Requesters.id == Schedulings.requester).join(ClassRooms, ClassRooms.id == Schedulings.classRoom).join(Blocks, Blocks.id == ClassRooms.block).filter(or_(
                    Schedulings.id.like(f'%{searchTerm}%'),
                    Schedulings.dateTime.like(f'%{searchTerm}%'),
                    Schedulings.situation.like(f'%{searchTerm}%'),
                    Requesters.name.like(f'%{searchTerm}%'),
                    ClassRooms.name.like(f'%{searchTerm}%'),
                    Blocks.name.like(f'%{searchTerm}%') 
                )).all()
            return data   

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Schedulings, Requesters, ClassRooms, Blocks).join(Schedulings, Requesters.id == Schedulings.requester).join(ClassRooms, ClassRooms.id == Schedulings.classRoom).join(Blocks, Blocks.id == ClassRooms.block).filter(Schedulings.id == id).first()
            return data

    def insert(requester, classRoom, dateTime):
        with DBConnectionHandler() as db:
            if SchedulingRepository.checkTime(classRoom, dateTime):
                data = Schedulings(requester=requester, classRoom=classRoom, dateTime=dateTime)
                db.session.add(data)
                db.session.commit()
                return True
            else:
                return False
    
    
    def update(id, requester, classRoom, dateTime):
        with DBConnectionHandler() as db:
            if SchedulingRepository.checkTime(classRoom, dateTime, id):
                db.session.query(Schedulings).filter(Schedulings.id == id).update({

                    "requester":requester, 
                    "classRoom":classRoom, 
                    "dateTime":dateTime
                    
                })
                db.session.commit()
            else:
                return False

    def canceled(id):
        with DBConnectionHandler() as db:
            success = db.session.query(Schedulings).filter(Schedulings.id == id).update({
                "situation": ESituation.CANCELED
            })
            if success:
                db.session.commit()
                return True