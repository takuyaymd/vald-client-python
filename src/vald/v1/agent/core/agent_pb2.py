# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vald/v1/agent/core/agent.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'vald/v1/agent/core/agent.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1evald/v1/agent/core/agent.proto\x12\x07\x63ore.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dvald/v1/payload/payload.proto2\xde\x03\n\x05\x41gent\x12_\n\x0b\x43reateIndex\x12&.payload.v1.Control.CreateIndexRequest\x1a\x11.payload.v1.Empty\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/index/create\x12\x46\n\tSaveIndex\x12\x11.payload.v1.Empty\x1a\x11.payload.v1.Empty\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/index/save\x12m\n\x12\x43reateAndSaveIndex\x12&.payload.v1.Control.CreateIndexRequest\x1a\x11.payload.v1.Empty\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/index/createandsave\x12Q\n\tIndexInfo\x12\x11.payload.v1.Empty\x1a\x1c.payload.v1.Info.Index.Count\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/index/info\x12j\n\x0cGetTimestamp\x12&.payload.v1.Object.GetTimestampRequest\x1a\x1c.payload.v1.Object.Timestamp\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/object/metaBc\n org.vdaas.vald.api.v1.agent.coreB\tValdAgentP\x01Z2github.com/vdaas/vald/apis/grpc/v1/agent/core;coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.agent.core.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n org.vdaas.vald.api.v1.agent.coreB\tValdAgentP\001Z2github.com/vdaas/vald/apis/grpc/v1/agent/core;core'
  _globals['_AGENT'].methods_by_name['CreateIndex']._loaded_options = None
  _globals['_AGENT'].methods_by_name['CreateIndex']._serialized_options = b'\202\323\344\223\002\017\022\r/index/create'
  _globals['_AGENT'].methods_by_name['SaveIndex']._loaded_options = None
  _globals['_AGENT'].methods_by_name['SaveIndex']._serialized_options = b'\202\323\344\223\002\r\022\013/index/save'
  _globals['_AGENT'].methods_by_name['CreateAndSaveIndex']._loaded_options = None
  _globals['_AGENT'].methods_by_name['CreateAndSaveIndex']._serialized_options = b'\202\323\344\223\002\026\022\024/index/createandsave'
  _globals['_AGENT'].methods_by_name['IndexInfo']._loaded_options = None
  _globals['_AGENT'].methods_by_name['IndexInfo']._serialized_options = b'\202\323\344\223\002\r\022\013/index/info'
  _globals['_AGENT'].methods_by_name['GetTimestamp']._loaded_options = None
  _globals['_AGENT'].methods_by_name['GetTimestamp']._serialized_options = b'\202\323\344\223\002\016\022\014/object/meta'
  _globals['_AGENT']._serialized_start=105
  _globals['_AGENT']._serialized_end=583
# @@protoc_insertion_point(module_scope)
