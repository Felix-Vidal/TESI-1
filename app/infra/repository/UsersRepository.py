from infra.config.connection import DBConnectionHandler
from infra.entities.Users import Users



class UsersRepository():

    def gets():
        with DBConnectionHandler() as db:
            data = db.session.query(Users).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Users).filter(Users.id == id).first()
            return data
        
    def getUserName(userName):
        with DBConnectionHandler() as db:
            data = db.session.query(Users).filter(Users.userName == userName).first()
            return data

    def insert(userName, fullName, password, role):
        with DBConnectionHandler() as db:
            data_isert = Users(userName=userName, fullName=fullName, password=password, role=role)
            db.session.add(data_isert)
            db.session.commit()

    def update(id, userName, fullName, password, role):
        with DBConnectionHandler() as db:
            db.session.query(Users).filter(Users.id == id).update({

                "userName": userName,
                "fullName": fullName,
                "password": password,
                "role": role
                
            })
            db.session.commit()

    def delete(id):
        with DBConnectionHandler() as db:
            db.session.query(Users).filter(Users.id == id).delete()
            db.session.commit()
        