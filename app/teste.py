from infra.repository.UsersRepository import UsersRepository
from infra.repository.BlocksRepository import BlocksRepository
from infra.repository.ClassRoomsRepository import ClassRoomsRepository

UsersRepository.inserir("admin", "admin", "admin", "ROLE_ADMIN")

for i in UsersRepository.gets():
    print(f"{i.id} {i.userName} {i.role}")

BlocksRepository.inserir("Dantas")
BlocksRepository.inserir("valdermir")
BlocksRepository.inserir("walter felix")


ClassRoomsRepository.inserir("sala 1", 40, 1, "LAB")
ClassRoomsRepository.inserir("sala 2", 35, 1, "LAB")

ClassRoomsRepository.inserir("sala 1", 50, 2, "CLASS_ROOM")
ClassRoomsRepository.inserir("sala 2", 45, 2, "CLASS_ROOM")
ClassRoomsRepository.inserir("sala 3", 30, 2, "CLASS_ROOM")

for classRoom, Block in ClassRoomsRepository.gets():
    print(f"ClassRoom: ID:{classRoom.id} Name: {classRoom.name} Capacity: {classRoom.capacity} TypeRoom: {classRoom.typeRoom} \nBloco: ID: {Block.id} Name: {Block.name} ", end="\n\n")
