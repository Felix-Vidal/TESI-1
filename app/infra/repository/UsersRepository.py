from infra.config.connection import DBConnectionHandler
from infra.entities.Users import Users



class UsersRepository():

    def gets(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Users).all()
            return data

    def get(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Users).filter(Users.id == id).first()
            return data

    def inserir(self, userName, fullName, password, role):
        with DBConnectionHandler() as db:
            data_isert = Users(userName=userName, fullName=fullName, password=password, role=role)
            db.session.add(data_isert)
            db.session.commit()

    def update(self,id, userName, fullName, password, role):
        with DBConnectionHandler() as db:
            db.session.query(Users).filter(Users.id == id).update({

                "userName": userName,
                "fullName": fullName,
                "password": password,
                "role": role
                
            })
            db.session.commit()

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Users).filter(Users.id == id).delete()
            db.session.commit()
        