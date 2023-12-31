# conect BD
from sqlalchemy import or_
from infra.config.connection import DBConnectionHandler
from infra.entities.Blocks import Blocks

class BlocksRepository():

    def gets(searchTerm=None):
        with DBConnectionHandler() as db:
            if searchTerm == None:
                data = db.session.query(Blocks).all()
            else:
                data = db.session.query(Blocks).filter(or_(
                    Blocks.id.like(f'%{searchTerm}%'),
                    Blocks.name.like(f'%{searchTerm}%'),
                )).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Blocks).filter(Blocks.id == id).first()
            return data
        
    @staticmethod
    def get_by_id(block_id):
        with DBConnectionHandler() as db:
            session = db.get_session()
            block = session.query(Blocks).filter(Blocks.id == block_id).first()
            return block
    
    def getName(name):
        with DBConnectionHandler() as db:
            data = db.session.query(Blocks).filter(Blocks.name == name).first()
            return data

    def insert(name):
        with DBConnectionHandler() as db:
            if BlocksRepository.getName(name) ==  None:
                data = Blocks(name=name)
                db.session.add(data)
                db.session.commit()
                return True
            else: 
                return False

    def update(id, name):
        with DBConnectionHandler() as db:
            if BlocksRepository.get(id):
                db.session.query(Blocks).filter(Blocks.id == id).update({
                    
                    "name":name
                    
                })
                db.session.commit()
                return True
            else:
                return False

    def delete(id):
        with DBConnectionHandler() as db:
            if BlocksRepository.get(id):
                db.session.query(Blocks).filter(Blocks.id == id).delete()
                db.session.commit()
                return True
            else:
                return False

        