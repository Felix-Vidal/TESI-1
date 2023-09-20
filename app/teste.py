from infra.repository.UsersRepository import UsersRepository
from infra.repository.BlocksRepository import BlocksRepository
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from infra.repository.RequesterRepository import RequesterRepository
from infra.repository.SchedulingRepository import SchedulingRepository
from datetime import datetime

# admin da sendo colocado automaticamente no banco
UsersRepository.insert("felix", "Joao Felix", "felix", "ROLE_USER")
print(UsersRepository.insert("mario", "Mario Dantas", "mario", "ROLE_USER"))
print(UsersRepository.insert("mario", "Mario Dantas", "mario", "ROLE_USER"))


print("\t\tUsers")

print("==========================================")
for i in UsersRepository.gets():
    print(f"{i.id} {i.userName} {i.role}")
print("==========================================", end="\n\n")

BlocksRepository.insert("Dantas")
BlocksRepository.insert("valdermir")
BlocksRepository.insert("walter felix")

print("\t\tBlocks")

print("==========================================")

for i in BlocksRepository.gets('val'):
    print(f"{i.id} {i.name}")


ClassRoomsRepository.insert("sala 1", 40, 1, "LAB")
ClassRoomsRepository.insert("sala 2", 35, 1, "LAB")

ClassRoomsRepository.insert("sala 1", 50, 2, "CLASS_ROOM")
ClassRoomsRepository.insert("sala 2", 45, 2, "CLASS_ROOM")
ClassRoomsRepository.insert("sala 3", 30, 2, "CLASS_ROOM")

print("\t\tClassRooms")

print("==========================================")
for classRoom, Block in ClassRoomsRepository.gets("room"):
    print(f"ClassRoom: ID:{classRoom.id} Name: {classRoom.name} Capacity: {classRoom.capacity} TypeRoom: {classRoom.typeRoom} \nBloco: ID: {Block.id} Name: {Block.name} ", end="\n\n")
print("==========================================", end="\n\n")



RequesterRepository.insert("joao felix", "joao@gmail.com", 6899999999, "ROLE_ALUNO")
RequesterRepository.insert("mateus", "mateus@gmail.com", 6899999999, "ROLE_ALUNO")
RequesterRepository.insert("limeira", "limeira@gmail.com", 6899999999, "ROLE_PROFESSOR")

print("\t\tRequester")

print("==========================================")
for requester in RequesterRepository.gets("professor"):
    print(f"ID: {requester.id} Name: {requester.name} Email: {requester.email} Telephone: {requester.telephone} Requester: {requester.typeRequester}")
print("==========================================", end="\n\n")

SchedulingRepository.insert(1,1, datetime(2023, 9, 11, 12, 0, 0))
SchedulingRepository.insert(1,1, datetime(2023, 9, 11, 13, 0, 0))
SchedulingRepository.insert(1,1, datetime(2023, 9, 11, 13, 0, 0))

print("\t\tScheduling")

print("==========================================")
for scheduling, requester, classRoom, block in SchedulingRepository.gets("12"):
    print(f"Scheduling: ID {scheduling.id} Data: {scheduling.dateTime} \nRequester: ID:{requester.id} Name: {requester.name} \nClassRoom: ID: {classRoom.id} name:{classRoom.name} capacity:{classRoom.capacity} name the block: {block.name} TypeRoom: {classRoom.typeRoom} \n")
print("==========================================", end="\n\n")





