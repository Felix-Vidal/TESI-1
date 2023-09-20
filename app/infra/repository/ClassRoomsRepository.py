from sqlalchemy import or_
from infra.config.connection import DBConnectionHandler
from infra.entities.ClassRooms import ClassRooms
from infra.entities.Blocks import Blocks

class ClassRoomsRepository:
    def gets(searchTerm=None):
        with DBConnectionHandler() as db:
            if searchTerm == None:
                data = db.session.query(ClassRooms,  Blocks).join(Blocks, Blocks.id == ClassRooms.block).all()
                
            else:
                data = db.session.query(ClassRooms,  Blocks).join(Blocks, Blocks.id == ClassRooms.block).filter(or_(
                    ClassRooms.id.like(f'%{searchTerm}%'),
                    ClassRooms.name.like(f'%{searchTerm}%'),
                    ClassRooms.capacity.like(f'%{searchTerm}%'),
                    ClassRooms.typeRoom.like(f'%{searchTerm}%'),
                    Blocks.name.like(f'%{searchTerm}%'),
                )).all()
            return data    

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(ClassRooms,  Blocks).join(Blocks, Blocks.id == ClassRooms.block).filter(ClassRooms.id == id).first()
            return data
        
    def getName(name):
        with DBConnectionHandler() as db:
            data = db.session.query(ClassRooms).filter(ClassRooms.name == name).first()
            return data

    def insert(name, capacity, block, typeRoom):
        with DBConnectionHandler() as db:
            if ClassRoomsRepository.getName(name) ==  None:
                data = ClassRooms(name=name, capacity=capacity, block=block, typeRoom=typeRoom)
                db.session.add(data)
                db.session.commit()
                return True
            else:
                return False

    def update(id, name, capacity, block, typeRoom):
        with DBConnectionHandler() as db:
            db.session.query(ClassRooms).filter(ClassRooms.id == id).update({

                "name":name, 
                "capacity":capacity, 
                "block":block, 
                "typeRoom":typeRoom
                
            })
            db.session.commit()

    def delete(id):
        with DBConnectionHandler() as db:
            sucess = db.session.query(ClassRooms).filter(ClassRooms.id == id).delete()
            if sucess:
                db.session.commit()
                return True