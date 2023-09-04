from repository.UsersRepository import UsersRepository
from model.Users import Users


user = Users(userName="admin", fullName="admin", password="admin" , role="ROLE_ADMIN")

UsersRepository.inserir(user)
UsersRepository.update(Users(userName="admin teste 2", fullName="admin", password="admin" , role="ROLE_ADMIN", id="1"))
registros = UsersRepository.gets()
for i in registros:
    print(i.userName)
