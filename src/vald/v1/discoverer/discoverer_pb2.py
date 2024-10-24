# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/discoverer/discoverer.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'vald/v1/discoverer/discoverer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#vald/v1/discoverer/discoverer.proto\x12\rdiscoverer.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dvald/v1/payload/payload.proto2\xa9\x02\n\nDiscoverer\x12X\n\x04Pods\x12\x1e.payload.v1.Discoverer.Request\x1a\x15.payload.v1.Info.Pods\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/discover/pods:\x01*\x12[\n\x05Nodes\x12\x1e.payload.v1.Discoverer.Request\x1a\x16.payload.v1.Info.Nodes\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/discover/nodes:\x01*\x12\x64\n\x08Services\x12\x1e.payload.v1.Discoverer.Request\x1a\x19.payload.v1.Info.Services\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/discover/services:\x01*Bc\n org.vdaas.vald.api.v1.discovererB\x0eValdDiscovererP\x01Z-github.com/vdaas/vald/apis/grpc/v1/discovererb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.discoverer.discoverer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n org.vdaas.vald.api.v1.discovererB\016ValdDiscovererP\001Z-github.com/vdaas/vald/apis/grpc/v1/discoverer'
  _globals['_DISCOVERER'].methods_by_name['Pods']._loaded_options = None
  _globals['_DISCOVERER'].methods_by_name['Pods']._serialized_options = b'\202\323\344\223\002\023\"\016/discover/pods:\001*'
  _globals['_DISCOVERER'].methods_by_name['Nodes']._loaded_options = None
  _globals['_DISCOVERER'].methods_by_name['Nodes']._serialized_options = b'\202\323\344\223\002\024\"\017/discover/nodes:\001*'
  _globals['_DISCOVERER'].methods_by_name['Services']._loaded_options = None
  _globals['_DISCOVERER'].methods_by_name['Services']._serialized_options = b'\202\323\344\223\002\027\"\022/discover/services:\001*'
  _globals['_DISCOVERER']._serialized_start=116
  _globals['_DISCOVERER']._serialized_end=413
# @@protoc_insertion_point(module_scope)