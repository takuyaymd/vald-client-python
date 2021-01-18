# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/vald/object.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vald/v1/vald/object.proto',
  package='vald.v1',
  syntax='proto3',
  serialized_options=b'\n\032org.vdaas.vald.api.v1.valdB\nValdObjectP\001Z\'github.com/vdaas/vald/apis/grpc/v1/vald',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19vald/v1/vald/object.proto\x12\x07vald.v1\x1a\x1dvald/v1/payload/payload.proto\x1a\x1cgoogle/api/annotations.proto2\xfc\x01\n\x06Object\x12L\n\x06\x45xists\x12\x15.payload.v1.Object.ID\x1a\x15.payload.v1.Object.ID\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/exists/{id}\x12S\n\tGetObject\x12\x15.payload.v1.Object.ID\x1a\x19.payload.v1.Object.Vector\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/object/{id}\x12O\n\x0fStreamGetObject\x12\x15.payload.v1.Object.ID\x1a\x1f.payload.v1.Object.StreamVector\"\x00(\x01\x30\x01\x42S\n\x1aorg.vdaas.vald.api.v1.valdB\nValdObjectP\x01Z\'github.com/vdaas/vald/apis/grpc/v1/valdb\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_OBJECT = _descriptor.ServiceDescriptor(
  name='Object',
  full_name='vald.v1.Object',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=100,
  serialized_end=352,
  methods=[
  _descriptor.MethodDescriptor(
    name='Exists',
    full_name='vald.v1.Object.Exists',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_ID,
    serialized_options=b'\202\323\344\223\002\016\022\014/exists/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetObject',
    full_name='vald.v1.Object.GetObject',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_VECTOR,
    serialized_options=b'\202\323\344\223\002\016\022\014/object/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamGetObject',
    full_name='vald.v1.Object.StreamGetObject',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_ID,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._OBJECT_STREAMVECTOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBJECT)

DESCRIPTOR.services_by_name['Object'] = _OBJECT

# @@protoc_insertion_point(module_scope)
