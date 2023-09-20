from sqlalchemy import or_
from infra.config.connection import DBConnectionHandler
from infra.entities.Requesters import Requesters

class RequesterRepository:

    def gets(searchTerm=None):
        with DBConnectionHandler() as db:
            if searchTerm == None:
                data = db.session.query(Requesters).all()
            else:
                data = db.session.query(Requesters).filter(or_(
                    Requesters.id.like(f'%{searchTerm}%'),
                    Requesters.name.like(f'%{searchTerm}%'),
                    Requesters.email.like(f'%{searchTerm}%'),
                    Requesters.telephone.like(f'%{searchTerm}%'),
                    Requesters.typeRequester.like(f'%{searchTerm}%'),
                )).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Requesters).filter(Requesters.id == id).first()
            return data
        
    def getName(name):
        with DBConnectionHandler() as db:
            data = db.session.query(Requesters).filter(Requesters.name == name).first()
            return data

    def insert(name, email, telephone, typeRequester):
        with DBConnectionHandler() as db:
                data = Requesters(name=name, email=email, telephone=telephone, typeRequester=typeRequester)
                db.session.add(data)
                db.session.commit()
                return True
                
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