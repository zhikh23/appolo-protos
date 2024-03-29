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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eregister.proto\x12\x06\x61ppolo\"T\n\x08Material\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\"O\n\x0fRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\"\'\n\x10RegisterResponse\x12\x13\n\x0bmaterial_id\x18\x01 \x01(\x04\"-\n\x16GetMaterialByIdRequest\x12\x13\n\x0bmaterial_id\x18\x01 \x01(\x04\"=\n\x17GetMaterialByIdResponse\x12\"\n\x08material\x18\x01 \x01(\x0b\x32\x10.appolo.Material\")\n\x19GetMaterialsByTagsRequest\x12\x0c\n\x04tags\x18\x01 \x03(\t\"A\n\x1aGetMaterialsByTagsResponse\x12#\n\tmaterials\x18\x01 \x03(\x0b\x32\x10.appolo.Material2\x89\x02\n\x0fRegisterService\x12\x45\n\x10RegisterMaterial\x12\x17.appolo.RegisterRequest\x1a\x18.appolo.RegisterResponse\x12R\n\x0fGetMaterialById\x12\x1e.appolo.GetMaterialByIdRequest\x1a\x1f.appolo.GetMaterialByIdResponse\x12[\n\x12GetMaterialsByTags\x12!.appolo.GetMaterialsByTagsRequest\x1a\".appolo.GetMaterialsByTagsResponseB\x11Z\x0fgen/go/registerb\x06proto3')



_MATERIAL = DESCRIPTOR.message_types_by_name['Material']
_REGISTERREQUEST = DESCRIPTOR.message_types_by_name['RegisterRequest']
_REGISTERRESPONSE = DESCRIPTOR.message_types_by_name['RegisterResponse']
_GETMATERIALBYIDREQUEST = DESCRIPTOR.message_types_by_name['GetMaterialByIdRequest']
_GETMATERIALBYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetMaterialByIdResponse']
_GETMATERIALSBYTAGSREQUEST = DESCRIPTOR.message_types_by_name['GetMaterialsByTagsRequest']
_GETMATERIALSBYTAGSRESPONSE = DESCRIPTOR.message_types_by_name['GetMaterialsByTagsResponse']
Material = _reflection.GeneratedProtocolMessageType('Material', (_message.Message,), {
  'DESCRIPTOR' : _MATERIAL,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:appolo.Material)
  })
_sym_db.RegisterMessage(Material)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:appolo.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:appolo.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)

GetMaterialByIdRequest = _reflection.GeneratedProtocolMessageType('GetMaterialByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMATERIALBYIDREQUEST,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:appolo.GetMaterialByIdRequest)
  })
_sym_db.RegisterMessage(GetMaterialByIdRequest)

GetMaterialByIdResponse = _reflection.GeneratedProtocolMessageType('GetMaterialByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMATERIALBYIDRESPONSE,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:appolo.GetMaterialByIdResponse)
  })
_sym_db.RegisterMessage(GetMaterialByIdResponse)

GetMaterialsByTagsRequest = _reflection.GeneratedProtocolMessageType('GetMaterialsByTagsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMATERIALSBYTAGSREQUEST,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:appolo.GetMaterialsByTagsRequest)
  })
_sym_db.RegisterMessage(GetMaterialsByTagsRequest)

GetMaterialsByTagsResponse = _reflection.GeneratedProtocolMessageType('GetMaterialsByTagsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMATERIALSBYTAGSRESPONSE,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:appolo.GetMaterialsByTagsResponse)
  })
_sym_db.RegisterMessage(GetMaterialsByTagsResponse)

_REGISTERSERVICE = DESCRIPTOR.services_by_name['RegisterService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\017gen/go/register'
  _MATERIAL._serialized_start=26
  _MATERIAL._serialized_end=110
  _REGISTERREQUEST._serialized_start=112
  _REGISTERREQUEST._serialized_end=191
  _REGISTERRESPONSE._serialized_start=193
  _REGISTERRESPONSE._serialized_end=232
  _GETMATERIALBYIDREQUEST._serialized_start=234
  _GETMATERIALBYIDREQUEST._serialized_end=279
  _GETMATERIALBYIDRESPONSE._serialized_start=281
  _GETMATERIALBYIDRESPONSE._serialized_end=342
  _GETMATERIALSBYTAGSREQUEST._serialized_start=344
  _GETMATERIALSBYTAGSREQUEST._serialized_end=385
  _GETMATERIALSBYTAGSRESPONSE._serialized_start=387
  _GETMATERIALSBYTAGSRESPONSE._serialized_end=452
  _REGISTERSERVICE._serialized_start=455
  _REGISTERSERVICE._serialized_end=720
# @@protoc_insertion_point(module_scope)
