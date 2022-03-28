from pkg.proto.user import user_microservice_pb2_grpc
from pkg.proto.user import user_microservice_pb2
from pkg.proto.core import error_pb2
import grpc
from concurrent import futures


class TestUser():
    def __init__(self, id, uuid, login, email, role, created_at, updated_at):
        self.id = id
        self.uuid = uuid
        self.login = login
        self.email = email
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at


test_user = TestUser(id=1,
                     uuid='3213213',
                     login='lizon',
                     email='12345@gmail.com',
                     role=1,
                     created_at='13:22:32',
                     updated_at='13:22:32')


def get_user(test_user):
    return user_microservice_pb2.User(id=test_user.id,
                                      uuid=test_user.uuid,
                                      login=test_user.login,
                                      email=test_user.email,
                                      role=test_user.role,
                                      created_at=test_user.created_at,
                                      updated_at=test_user.updated_at)


class UserServicer(user_microservice_pb2_grpc.UserServiceServicer):

    def GetUserById(self, request, context):
        if request.id == test_user.id:
            return get_user(test_user)
        else:
            print('ops')

    def GetUserByLogin(self, request, context):
        if request.login == test_user.login:
            return get_user(test_user)
        else:
            print('ops')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_microservice_pb2_grpc.add_UserServiceServicer_to_server(
        UserServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
