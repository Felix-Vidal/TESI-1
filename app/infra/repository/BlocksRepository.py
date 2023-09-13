# conect BD
from infra.config.connection import DBConnectionHandler
from infra.entities.Blocks import Blocks

class BlocksRepository():

    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(Blocks).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Blocks).filter(Blocks.id == id).first()
            return data

    def insert(name):
        with DBConnectionHandler() as db:
            data = Blocks(name=name)
            db.session.add(data)
            db.session.commit()

    def update(id, name):
        with DBConnectionHandler() as db:
            db.session.query(Blocks).filter(Blocks.id == id).update({
                
                "name":name
                
            })
            db.session.commit()

    def delete(id):
        with DBConnectionHandler() as db:
            db.session.query(Blocks).filter(Blocks.id == id).delete()
            db.session.commit()

        