# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eregister.proto\x12\x08register\"O\n\x0fRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\"\'\n\x10RegisterResponse\x12\x13\n\x0bmaterial_id\x18\x01 \x01(\x04\x32U\n\x08Register\x12I\n\x10RegisterMaterial\x12\x19.register.RegisterRequest\x1a\x1a.register.RegisterResponseB\x11Z\x0fgen/go/registerb\x06proto3')



_REGISTERREQUEST = DESCRIPTOR.message_types_by_name['RegisterRequest']
_REGISTERRESPONSE = DESCRIPTOR.message_types_by_name['RegisterResponse']
RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:register.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:register.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)

_REGISTER = DESCRIPTOR.services_by_name['Register']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\017gen/go/register'
  _REGISTERREQUEST._serialized_start=28
  _REGISTERREQUEST._serialized_end=107
  _REGISTERRESPONSE._serialized_start=109
  _REGISTERRESPONSE._serialized_end=148
  _REGISTER._serialized_start=150
  _REGISTER._serialized_end=235
# @@protoc_insertion_point(module_scope)