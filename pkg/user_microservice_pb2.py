# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user-microservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17user-microservice.proto\x12\x04user\x1a\x1bgoogle/protobuf/empty.proto\"<\n\nNewUserReq\x12\r\n\x05login\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\";\n\rUpdateUserReq\x12\r\n\x05login\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\x05\"\x17\n\tUserReqID\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1b\n\x0bUserReqUuid\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x1d\n\x0cUserReqLogin\x12\r\n\x05login\x18\x01 \x01(\t\"-\n\x0cSelectionReq\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\"t\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\r\n\x05login\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\x05\x12\x12\n\ncreated_at\x18\x06 \x01(\t\x12\x12\n\nupdated_at\x18\x07 \x01(\t\"f\n\tSelection\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x18\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\n.user.User\x12\r\n\x05total\x18\x04 \x01(\x05\x12\x11\n\tlast_page\x18\x05 \x01(\x05\x32\x94\x03\n\x0bUserService\x12*\n\nCreateUser\x12\x10.user.NewUserReq\x1a\n.user.User\x12*\n\x0bGetUserById\x12\x0f.user.UserReqID\x1a\n.user.User\x12.\n\rGetUserByUuid\x12\x11.user.UserReqUuid\x1a\n.user.User\x12\x30\n\x0eGetUserByLogin\x12\x12.user.UserReqLogin\x1a\n.user.User\x12+\n\nDeleteUser\x12\x11.user.UserReqUuid\x1a\n.user.User\x12-\n\nUpdateUser\x12\x13.user.UpdateUserReq\x1a\n.user.User\x12-\n\x06GetAll\x12\x12.user.SelectionReq\x1a\x0f.user.Selection\x12@\n\x0eHeartbeatCheck\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.EmptyB(Z&github.com/wrs-news/node-protocol/userb\x06proto3')



_NEWUSERREQ = DESCRIPTOR.message_types_by_name['NewUserReq']
_UPDATEUSERREQ = DESCRIPTOR.message_types_by_name['UpdateUserReq']
_USERREQID = DESCRIPTOR.message_types_by_name['UserReqID']
_USERREQUUID = DESCRIPTOR.message_types_by_name['UserReqUuid']
_USERREQLOGIN = DESCRIPTOR.message_types_by_name['UserReqLogin']
_SELECTIONREQ = DESCRIPTOR.message_types_by_name['SelectionReq']
_USER = DESCRIPTOR.message_types_by_name['User']
_SELECTION = DESCRIPTOR.message_types_by_name['Selection']
NewUserReq = _reflection.GeneratedProtocolMessageType('NewUserReq', (_message.Message,), {
  'DESCRIPTOR' : _NEWUSERREQ,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.NewUserReq)
  })
_sym_db.RegisterMessage(NewUserReq)

UpdateUserReq = _reflection.GeneratedProtocolMessageType('UpdateUserReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQ,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.UpdateUserReq)
  })
_sym_db.RegisterMessage(UpdateUserReq)

UserReqID = _reflection.GeneratedProtocolMessageType('UserReqID', (_message.Message,), {
  'DESCRIPTOR' : _USERREQID,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.UserReqID)
  })
_sym_db.RegisterMessage(UserReqID)

UserReqUuid = _reflection.GeneratedProtocolMessageType('UserReqUuid', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUUID,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.UserReqUuid)
  })
_sym_db.RegisterMessage(UserReqUuid)

UserReqLogin = _reflection.GeneratedProtocolMessageType('UserReqLogin', (_message.Message,), {
  'DESCRIPTOR' : _USERREQLOGIN,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.UserReqLogin)
  })
_sym_db.RegisterMessage(UserReqLogin)

SelectionReq = _reflection.GeneratedProtocolMessageType('SelectionReq', (_message.Message,), {
  'DESCRIPTOR' : _SELECTIONREQ,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.SelectionReq)
  })
_sym_db.RegisterMessage(SelectionReq)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  })
_sym_db.RegisterMessage(User)

Selection = _reflection.GeneratedProtocolMessageType('Selection', (_message.Message,), {
  'DESCRIPTOR' : _SELECTION,
  '__module__' : 'user_microservice_pb2'
  # @@protoc_insertion_point(class_scope:user.Selection)
  })
_sym_db.RegisterMessage(Selection)

_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/wrs-news/node-protocol/user'
  _NEWUSERREQ._serialized_start=62
  _NEWUSERREQ._serialized_end=122
  _UPDATEUSERREQ._serialized_start=124
  _UPDATEUSERREQ._serialized_end=183
  _USERREQID._serialized_start=185
  _USERREQID._serialized_end=208
  _USERREQUUID._serialized_start=210
  _USERREQUUID._serialized_end=237
  _USERREQLOGIN._serialized_start=239
  _USERREQLOGIN._serialized_end=268
  _SELECTIONREQ._serialized_start=270
  _SELECTIONREQ._serialized_end=315
  _USER._serialized_start=317
  _USER._serialized_end=433
  _SELECTION._serialized_start=435
  _SELECTION._serialized_end=537
  _USERSERVICE._serialized_start=540
  _USERSERVICE._serialized_end=944
# @@protoc_insertion_point(module_scope)
