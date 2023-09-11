from infra.repository.UsersRepository import UsersRepository
from infra.repository.BlocksRepository import BlocksRepository
from infra.repository.ClassRoomsRepository import ClassRoomsRepository
from infra.repository.RequesterRepository import RequesterRepository
from infra.repository.SchedulingRepository import SchedulingRepository
from datetime import datetime
UsersRepository.inserir("admin", "admin", "admin", "ROLE_ADMIN")
UsersRepository.inserir("felix", "Joao Felix", "felix", "ROLE_USER")
UsersRepository.inserir("mario", "Mario Dantas", "mario", "ROLE_USER")

print("\t\tUser")

print("==========================================")
for i in UsersRepository.gets():
    print(f"{i.id} {i.userName} {i.role}")
print("==========================================", end="\n\n")

BlocksRepository.inserir("Dantas")
BlocksRepository.inserir("valdermir")
BlocksRepository.inserir("walter felix")


ClassRoomsRepository.inserir("sala 1", 40, 1, "LAB")
ClassRoomsRepository.inserir("sala 2", 35, 1, "LAB")

ClassRoomsRepository.inserir("sala 1", 50, 2, "CLASS_ROOM")
ClassRoomsRepository.inserir("sala 2", 45, 2, "CLASS_ROOM")
ClassRoomsRepository.inserir("sala 3", 30, 2, "CLASS_ROOM")

print("\t\tClassRooms")

print("==========================================")
for classRoom, Block in ClassRoomsRepository.gets():
    print(f"ClassRoom: ID:{classRoom.id} Name: {classRoom.name} Capacity: {classRoom.capacity} TypeRoom: {classRoom.typeRoom} \nBloco: ID: {Block.id} Name: {Block.name} ", end="\n\n")
print("==========================================", end="\n\n")



RequesterRepository.inserir("joao felix", "joao@gmail.com", 6899999999, "ROLE_ALUNO")
RequesterRepository.inserir("mateus", "mateus@gmail.com", 6899999999, "ROLE_ALUNO")
RequesterRepository.inserir("limeira", "limeira@gmail.com", 6899999999, "ROLE_PROFESSOR")

print("\t\tRequester")

print("==========================================")
for requester in RequesterRepository.gets():
    print(f"ID: {requester.id} Name: {requester.name} Email: {requester.email} Telephone: {requester.telephone} Requester:{requester.typeRequester}")
print("==========================================", end="\n\n")
datatime = datetime(2023, 9, 11, 12, 0, 0)
print(datatime)
SchedulingRepository.inserir(1,1, datetime(2023, 9, 11, 12, 0, 0))

SchedulingRepository.inserir(1,1, datetime(2023, 9, 11, 13, 0, 0))

print("\t\tScheduling")

print("==========================================")
for i in SchedulingRepository.gets():
    print(f"ID {i.id} ClassRoom: {i.classRoom} Requester: {i.requester} Data: {i.dateTime}")
print("==========================================", end="\n\n")