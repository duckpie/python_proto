# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from user import user_microservice_pb2 as user_dot_user__microservice__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/user.UserService/CreateUser',
                request_serializer=user_dot_user__microservice__pb2.NewUserReq.SerializeToString,
                response_deserializer=user_dot_user__microservice__pb2.User.FromString,
                )
        self.GetUserById = channel.unary_unary(
                '/user.UserService/GetUserById',
                request_serializer=user_dot_user__microservice__pb2.UserReqID.SerializeToString,
                response_deserializer=user_dot_user__microservice__pb2.User.FromString,
                )
        self.GetUserByUuid = channel.unary_unary(
                '/user.UserService/GetUserByUuid',
                request_serializer=user_dot_user__microservice__pb2.UserReqUuid.SerializeToString,
                response_deserializer=user_dot_user__microservice__pb2.User.FromString,
                )
        self.GetUserByLogin = channel.unary_unary(
                '/user.UserService/GetUserByLogin',
                request_serializer=user_dot_user__microservice__pb2.UserReqLogin.SerializeToString,
                response_deserializer=user_dot_user__microservice__pb2.User.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/user.UserService/DeleteUser',
                request_serializer=user_dot_user__microservice__pb2.UserReqUuid.SerializeToString,
                response_deserializer=user_dot_user__microservice__pb2.User.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/user.UserService/UpdateUser',
                request_serializer=user_dot_user__microservice__pb2.UpdateUserReq.SerializeToString,
                response_deserializer=user_dot_user__microservice__pb2.User.FromString,
                )
        self.GetAll = channel.unary_unary(
                '/user.UserService/GetAll',
                request_serializer=user_dot_user__microservice__pb2.SelectionReq.SerializeToString,
                response_deserializer=user_dot_user__microservice__pb2.Selection.FromString,
                )
        self.HeartbeatCheck = channel.unary_unary(
                '/user.UserService/HeartbeatCheck',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByUuid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByLogin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HeartbeatCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=user_dot_user__microservice__pb2.NewUserReq.FromString,
                    response_serializer=user_dot_user__microservice__pb2.User.SerializeToString,
            ),
            'GetUserById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserById,
                    request_deserializer=user_dot_user__microservice__pb2.UserReqID.FromString,
                    response_serializer=user_dot_user__microservice__pb2.User.SerializeToString,
            ),
            'GetUserByUuid': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByUuid,
                    request_deserializer=user_dot_user__microservice__pb2.UserReqUuid.FromString,
                    response_serializer=user_dot_user__microservice__pb2.User.SerializeToString,
            ),
            'GetUserByLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByLogin,
                    request_deserializer=user_dot_user__microservice__pb2.UserReqLogin.FromString,
                    response_serializer=user_dot_user__microservice__pb2.User.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=user_dot_user__microservice__pb2.UserReqUuid.FromString,
                    response_serializer=user_dot_user__microservice__pb2.User.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=user_dot_user__microservice__pb2.UpdateUserReq.FromString,
                    response_serializer=user_dot_user__microservice__pb2.User.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=user_dot_user__microservice__pb2.SelectionReq.FromString,
                    response_serializer=user_dot_user__microservice__pb2.Selection.SerializeToString,
            ),
            'HeartbeatCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartbeatCheck,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/CreateUser',
            user_dot_user__microservice__pb2.NewUserReq.SerializeToString,
            user_dot_user__microservice__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/GetUserById',
            user_dot_user__microservice__pb2.UserReqID.SerializeToString,
            user_dot_user__microservice__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByUuid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/GetUserByUuid',
            user_dot_user__microservice__pb2.UserReqUuid.SerializeToString,
            user_dot_user__microservice__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/GetUserByLogin',
            user_dot_user__microservice__pb2.UserReqLogin.SerializeToString,
            user_dot_user__microservice__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/DeleteUser',
            user_dot_user__microservice__pb2.UserReqUuid.SerializeToString,
            user_dot_user__microservice__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/UpdateUser',
            user_dot_user__microservice__pb2.UpdateUserReq.SerializeToString,
            user_dot_user__microservice__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/GetAll',
            user_dot_user__microservice__pb2.SelectionReq.SerializeToString,
            user_dot_user__microservice__pb2.Selection.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HeartbeatCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.UserService/HeartbeatCheck',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
