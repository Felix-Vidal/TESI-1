from DaoUsers import DaoUsers
from ModelUsers import Users


user = Users(userName="admin", fullName="admin", password="admin" , role="ROLE_ADMIN")

DaoUsers.inserir(user)
DaoUsers.update(Users(userName="admin teste 2", fullName="admin", password="admin" , role="ROLE_ADMIN", id="1"))
registros = DaoUsers.registros()
for i in registros:
    print(i.userName)

