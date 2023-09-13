from infra.config.connection import DBConnectionHandler
from infra.entities.ClassRooms import ClassRooms
from infra.entities.Blocks import Blocks

class ClassRoomsRepository:
    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(ClassRooms,  Blocks).join(Blocks, Blocks.id == ClassRooms.block).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(ClassRooms,  Blocks).join(Blocks, Blocks.id == ClassRooms.block).filter(ClassRooms.id == id).first()
            return data

    def insert(name, capacity, block, typeRoom):
        with DBConnectionHandler() as db:
            data_isert = ClassRooms(name=name, capacity=capacity, block=block, typeRoom=typeRoom)
            db.session.add(data_isert)
            db.session.commit()

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
            db.session.query(ClassRooms).filter(ClassRooms.id == id).delete()
            db.session.commit()