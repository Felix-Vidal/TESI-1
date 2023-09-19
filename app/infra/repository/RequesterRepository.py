from infra.config.connection import DBConnectionHandler
from infra.entities.Requesters import Requesters

class RequesterRepository:

    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(Requesters).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Requesters).filter(Requesters.id == id).first()
            return data

    def insert(name, email, telephone, typeRequester):
        with DBConnectionHandler() as db:
            if RequesterRepository.get(id) == None:
                data = Requesters(name=name, email=email, telephone=telephone, typeRequester=typeRequester)
                db.session.add(data)
                db.session.commit()
                return True
            else:
                return False

    def update(id, name, email, telephone, typeRequester):
        with DBConnectionHandler() as db:
            if RequesterRepository.get(id):
                db.session.query(Requesters).filter(Requesters.id == id).update({

                    "name":name, 
                    "email":email, 
                    "telephone":telephone, 
                    "typeRequester":typeRequester
                    
                })
                db.session.commit()
                return True
            else:
                return False

    def delete(id):
        with DBConnectionHandler() as db:
            if RequesterRepository.get(id):
                db.session.query(Requesters).filter(Requesters.id == id).delete()
                db.session.commit()
                return True
            else:
                return False