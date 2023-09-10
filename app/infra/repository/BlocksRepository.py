# conect BD
from infra.config.connection import DBConnectionHandler
from infra.entities.Blocks import Blocks

class BlocksRepository():

    def gets(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Blocks).all()
            return data

    def get(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Blocks).filter(Blocks.id == id).first()
            return data

    def inserir(self, name):
        with DBConnectionHandler() as db:
            data_isert = Blocks(name=name)
            db.session.add(data_isert)
            db.session.commit()

    def update(self, id, name):
        with DBConnectionHandler() as db:
            db.session.query(Blocks).filter(Blocks.id == id).update({
                
                "name":name
                
            })
            db.session.commit()

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Blocks).filter(Blocks.id == id).delete()
            db.session.commit()

        