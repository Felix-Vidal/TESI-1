from sqlalchemy import or_
from infra.config.connection import DBConnectionHandler
from infra.entities.Users import Users



class UsersRepository():

    def gets(searchTerm=None):

        with DBConnectionHandler() as db:
            if searchTerm == None:
                data = db.session.query(Users).all()
            else:
                data = db.session.query(Users).filter(or_(

                    Users.userName.like(f'%{searchTerm}%'),
                    Users.fullName.like(f'%{searchTerm}%'),
                    Users.password.like(f'%{searchTerm}%'),
                    Users.role.like(f'%{searchTerm}%'))

                ).all()
            return data

    def get(id):
        with DBConnectionHandler() as db:
            data = db.session.query(Users).filter(Users.id == id).first()
            return data
        
    def getUserName(userName):
        with DBConnectionHandler() as db:
            data = db.session.query(Users).filter(Users.userName == userName).first()
            return data
    
    def getUserRole(role):
        with DBConnectionHandler() as db:
            data = db.session.query(Users).filter(Users.role == role).first()
            return data
    

    def insert(userName, fullName, password, role):
        with DBConnectionHandler() as db:
            if UsersRepository.getUserName(userName) ==  None:
                data= Users(userName=userName, fullName=fullName, password=password, role=role)
                db.session.add(data)
                db.session.commit()
                return True
            else:
                return False

    def update(id, userName, fullName, password, role):
        with DBConnectionHandler() as db:
            if UsersRepository.get(id) !=  None:
                db.session.query(Users).filter(Users.id == id).update({

                    "userName": userName,
                    "fullName": fullName,
                    "password": password,
                    "role": role
                    
                })
                db.session.commit()
                return True
            else:
                return False

    def delete(id):
        with DBConnectionHandler() as db:
            success = db.session.query(Users).filter(Users.id == id).delete()
            if success:
                db.session.commit()
                return True
        