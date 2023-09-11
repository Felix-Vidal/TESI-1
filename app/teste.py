from infra.repository.UsersRepository import UsersRepository

UsersRepository.inserir("admin", "admin", "admin", "ROLE_ADMIN")
UsersRepository.inserir("felix", "admin", "admin", "ROLE_USER")
UsersRepository.update( 2, "top", "top", "toptop", "ROLE_USER")
for i in UsersRepository.gets():
    print(f"{i.id} {i.userName} {i.role}")