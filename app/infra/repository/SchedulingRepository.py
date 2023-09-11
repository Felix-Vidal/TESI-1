from infra.config.connection import DBConnectionHandler
from infra.entities.Scheduling import Scheduling
class SchedulingRepository:

    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(Scheduling).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Scheduling).filter(Scheduling.id == id).first()
            return data

    def inserir(name, capacity, block, typeRoom):
        with DBConnectionHandler() as db:
            data_isert = Scheduling(name=name, capacity=capacity, block=block, typeRoom=typeRoom)
            db.session.add(data_isert)
            db.session.commit()

    def update(id, name, capacity, block, typeRoom):
        with DBConnectionHandler() as db:
            db.session.query(Scheduling).filter(Scheduling.id == id).update({

                "number":name, 
                "capacity":capacity, 
                "block":block, 
                "typeRoom":typeRoom
                
            })
            db.session.commit()

    def delete(id):
        with DBConnectionHandler() as db:
            db.session.query(Scheduling).filter(Scheduling.id == id).delete()
            db.session.commit()