import grpc

from pkg import user_microservice_pb2_grpc
from pkg import user_microservice_pb2


channel = grpc.insecure_channel('localhost:50051')
stub = user_microservice_pb2_grpc.UserServiceStub(channel)


id = 1

feature = stub.GetUserById(id)