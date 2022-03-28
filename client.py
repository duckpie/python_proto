import grpc

from pkg.proto.user import user_microservice_pb2_grpc
from pkg.proto.user import user_microservice_pb2


def get_user_by_id(stub, id):
    user_id = user_microservice_pb2.UserReqID(id=id)

    try:
        user = stub.GetUserById(user_id)
        print(user)
    except:
        print('ops')


def get_user_by_login(stub, login):
    user_login = user_microservice_pb2.UserReqLogin(login=login)
    try:
        user = stub.GetUserByLogin(user_login)
        print(user)
    except:
        print('ops')


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_microservice_pb2_grpc.UserServiceStub(channel)
        print("-------------- GetUserById --------------")
        get_user_by_id(stub, id=1)
        print("-------------- GetUserByLogin --------------")
        get_user_by_login(stub, login='lizon')


if __name__ == '__main__':
    run()
