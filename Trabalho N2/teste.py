from DaoUser import DaoUser
from ModelUser import User


user = User(userName="admin", fullName="admin", password="admin" , role="ROLE_ADMIN")

DaoUser.inserir(user)
DaoUser.update(User(userName="admin teste 2", fullName="admin", password="admin" , role="ROLE_ADMIN", id="1"))
registros = DaoUser.registros()
for i in registros:
    print(i.userName)

