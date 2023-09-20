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
                    Users.role.like(f'%{searchTerm}%')),
                    Users.active.like(f'%{searchTerm}%')

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
                Users()
                data = Users(userName=userName, fullName=fullName, password=password, role=role, active=True)
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

    def habilitar(id):
        with DBConnectionHandler() as db:
            success = db.session.query(Users).filter(Users.id == id).update({
                "active": True
            })
            if success:
                db.session.commit()
                return True
    
    def desabilita(id):
        with DBConnectionHandler() as db:
            success = db.session.query(Users).filter(Users.id == id).update({
                "active": False
            })
            if success:
                db.session.commit()
                return True
        