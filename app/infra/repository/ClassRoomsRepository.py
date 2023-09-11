from infra.config.connection import DBConnectionHandler
from infra.entities.ClassRooms import ClassRooms

class ClassRoomsRepository:
    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(ClassRooms).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(ClassRooms).filter(ClassRooms.id == id).first()
            return data

    def inserir(name, email, telephone, typeRequester):
        with DBConnectionHandler() as db:
            data_isert = ClassRooms(name=name, email=email, telephone=telephone, typeRequester=typeRequester)
            db.session.add(data_isert)
            db.session.commit()

    def update(id, name, email, telephone, typeRequester):
        with DBConnectionHandler() as db:
            db.session.query(ClassRooms).filter(ClassRooms.id == id).update({

                "name":name, 
                "email":email, 
                "telephone":telephone, 
                "typeRequester":typeRequester
                
            })
            db.session.commit()

    def delete(id):
        with DBConnectionHandler() as db:
            db.session.query(ClassRooms).filter(ClassRooms.id == id).delete()
            db.session.commit()