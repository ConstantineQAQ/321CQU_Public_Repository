# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_services_protobuf/notification_center/wechat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8micro_services_protobuf/notification_center/wechat.proto\x12\x13notification_center\"1\n\x14SetUserOpenIdRequest\x12\x0b\n\x03uid\x18\x01 \x01(\x0c\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"X\n\x1eHandleWechatServerEventRequest\x12\x0e\n\x06openid\x18\x01 \x01(\t\x12\x13\n\x0btemplate_id\x18\x02 \x01(\t\x12\x11\n\tis_accept\x18\x03 \x01(\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'micro_services_protobuf.notification_center.wechat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SETUSEROPENIDREQUEST']._serialized_start=81
  _globals['_SETUSEROPENIDREQUEST']._serialized_end=130
  _globals['_HANDLEWECHATSERVEREVENTREQUEST']._serialized_start=132
  _globals['_HANDLEWECHATSERVEREVENTREQUEST']._serialized_end=220
# @@protoc_insertion_point(module_scope)
