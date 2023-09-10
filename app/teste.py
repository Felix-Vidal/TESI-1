from infra.repository.UsersRepository import UsersRepository

repo = UsersRepository

UsersRepository.inserir(UsersRepository, "admin", "admin", "admin", "ROLE_ADMIN")
UsersRepository.inserir(UsersRepository, "felix", "admin", "admin", "ROLE_USER")
UsersRepository.update(UsersRepository, 2, "top", "top", "toptop", "ROLE_USER")
for i in repo.gets(repo):
    print(f"{i.userName} {i.role}")