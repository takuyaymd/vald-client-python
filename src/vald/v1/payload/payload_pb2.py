# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/payload/payload.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dvald/v1/payload/payload.proto\x12\npayload.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x17google/rpc/status.proto\"\xed\n\n\x06Search\x1a^\n\x07Request\x12 \n\x06vector\x18\x01 \x03(\x02\x42\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Search.RequestR\x08requests\x1aN\n\tIDRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.ConfigR\x06\x63onfig\x1aJ\n\x0eMultiIDRequest\x12\x38\n\x08requests\x18\x01 \x03(\x0b\x32\x1c.payload.v1.Search.IDRequestR\x08requests\x1a\x95\x01\n\rObjectRequest\x12\x16\n\x06object\x18\x01 \x01(\x0cR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Search.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Search.ObjectRequestR\x08requests\x1a\x94\x03\n\x06\x43onfig\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12\x19\n\x03num\x18\x02 \x01(\rB\x07\xbaH\x04*\x02(\x01R\x03num\x12\x16\n\x06radius\x18\x03 \x01(\x02R\x06radius\x12\x18\n\x07\x65psilon\x18\x04 \x01(\x02R\x07\x65psilon\x12\x18\n\x07timeout\x18\x05 \x01(\x03R\x07timeout\x12\x42\n\x0fingress_filters\x18\x06 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x0eingressFilters\x12@\n\x0e\x65gress_filters\x18\x07 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\regressFilters\x12 \n\x07min_num\x18\x08 \x01(\rB\x07\xbaH\x04*\x02(\x00R\x06minNum\x12\\\n\x15\x61ggregation_algorithm\x18\t \x01(\x0e\x32\'.payload.v1.Search.AggregationAlgorithmR\x14\x61ggregationAlgorithm\x1a`\n\x08Response\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12\x35\n\x07results\x18\x02 \x03(\x0b\x32\x1b.payload.v1.Object.DistanceR\x07results\x1a\x46\n\tResponses\x12\x39\n\tresponses\x18\x01 \x03(\x0b\x32\x1b.payload.v1.Search.ResponseR\tresponses\x1a\x84\x01\n\x0eStreamResponse\x12\x39\n\x08response\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Search.ResponseH\x00R\x08response\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\"k\n\x14\x41ggregationAlgorithm\x12\x0b\n\x07Unknown\x10\x00\x12\x13\n\x0f\x43oncurrentQueue\x10\x01\x12\r\n\tSortSlice\x10\x02\x12\x11\n\rSortPoolSlice\x10\x03\x12\x0f\n\x0bPairingHeap\x10\x04\"y\n\x06\x46ilter\x1a\x30\n\x06Target\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04port\x18\x02 \x01(\rR\x04port\x1a=\n\x06\x43onfig\x12\x33\n\x07targets\x18\x01 \x03(\x0b\x32\x19.payload.v1.Filter.TargetR\x07targets\"\xe5\x04\n\x06Insert\x1ay\n\x07Request\x12;\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Insert.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Insert.RequestR\x08requests\x1a\xae\x01\n\rObjectRequest\x12/\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Insert.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Insert.ObjectRequestR\x08requests\x1a\x92\x01\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\"\x9d\x05\n\x06Update\x1ay\n\x07Request\x12;\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Update.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Update.RequestR\x08requests\x1a\xae\x01\n\rObjectRequest\x12/\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Update.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Update.ObjectRequestR\x08requests\x1a\xca\x01\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12\x36\n\x17\x64isable_balanced_update\x18\x04 \x01(\x08R\x15\x64isableBalancedUpdate\"\x9d\x05\n\x06Upsert\x1ay\n\x07Request\x12;\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Upsert.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Upsert.RequestR\x08requests\x1a\xae\x01\n\rObjectRequest\x12/\n\x06object\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobR\x06object\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Upsert.ConfigR\x06\x63onfig\x12\x39\n\nvectorizer\x18\x03 \x01(\x0b\x32\x19.payload.v1.Filter.TargetR\nvectorizer\x1aR\n\x12MultiObjectRequest\x12<\n\x08requests\x18\x01 \x03(\x0b\x32 .payload.v1.Upsert.ObjectRequestR\x08requests\x1a\xca\x01\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12\x36\n\x17\x64isable_balanced_update\x18\x04 \x01(\x08R\x15\x64isableBalancedUpdate\"\x91\x04\n\x06Remove\x1a\x63\n\x07Request\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.IDR\x02id\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.payload.v1.Remove.ConfigR\x06\x63onfig\x1a\x46\n\x0cMultiRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32\x1a.payload.v1.Remove.RequestR\x08requests\x1aP\n\x10TimestampRequest\x12<\n\ntimestamps\x18\x01 \x03(\x0b\x32\x1c.payload.v1.Remove.TimestampR\ntimestamps\x1a\xa8\x01\n\tTimestamp\x12\x1c\n\ttimestamp\x18\x01 \x01(\x03R\ttimestamp\x12\x41\n\x08operator\x18\x02 \x01(\x0e\x32%.payload.v1.Remove.Timestamp.OperatorR\x08operator\":\n\x08Operator\x12\x06\n\x02\x45q\x10\x00\x12\x06\n\x02Ne\x10\x01\x12\x06\n\x02Ge\x10\x02\x12\x06\n\x02Gt\x10\x03\x12\x06\n\x02Le\x10\x04\x12\x06\n\x02Lt\x10\x05\x1a]\n\x06\x43onfig\x12\x35\n\x17skip_strict_exist_check\x18\x01 \x01(\x08R\x14skipStrictExistCheck\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\"\xb4\x0b\n\x06Object\x1au\n\rVectorRequest\x12/\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.IDB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x02id\x12\x33\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x19.payload.v1.Filter.ConfigR\x07\x66ilters\x1a\x36\n\x08\x44istance\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1a\n\x08\x64istance\x18\x02 \x01(\x02R\x08\x64istance\x1a\x84\x01\n\x0eStreamDistance\x12\x39\n\x08\x64istance\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Object.DistanceH\x00R\x08\x64istance\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a\x1d\n\x02ID\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x1a\x17\n\x03IDs\x12\x10\n\x03ids\x18\x01 \x03(\tR\x03ids\x1a\x61\n\x06Vector\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x12 \n\x06vector\x18\x02 \x03(\x02\x42\x08\xbaH\x05\x92\x01\x02\x08\x02R\x06vector\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x1a\x46\n\x13GetTimestampRequest\x12/\n\x02id\x18\x01 \x01(\x0b\x32\x15.payload.v1.Object.IDB\x08\xbaH\x05\x92\x01\x02\x08\x02R\x02id\x1a\x42\n\tTimestamp\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x1a>\n\x07Vectors\x12\x33\n\x07vectors\x18\x01 \x03(\x0b\x32\x19.payload.v1.Object.VectorR\x07vectors\x1a|\n\x0cStreamVector\x12\x33\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorH\x00R\x06vector\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a=\n\rReshapeVector\x12\x16\n\x06object\x18\x01 \x01(\x0cR\x06object\x12\x14\n\x05shape\x18\x02 \x03(\x05R\x05shape\x1a\x37\n\x04\x42lob\x12\x17\n\x02id\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x02id\x12\x16\n\x06object\x18\x02 \x01(\x0cR\x06object\x1at\n\nStreamBlob\x12-\n\x04\x62lob\x18\x01 \x01(\x0b\x32\x17.payload.v1.Object.BlobH\x00R\x04\x62lob\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a\x44\n\x08Location\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04uuid\x18\x02 \x01(\tR\x04uuid\x12\x10\n\x03ips\x18\x03 \x03(\tR\x03ips\x1a\x84\x01\n\x0eStreamLocation\x12\x39\n\x08location\x18\x01 \x01(\x0b\x32\x1b.payload.v1.Object.LocationH\x00R\x08location\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\x1a\x46\n\tLocations\x12\x39\n\tlocations\x18\x01 \x03(\x0b\x32\x1b.payload.v1.Object.LocationR\tlocations\x1a\x8b\x01\n\x04List\x1a\t\n\x07Request\x1ax\n\x08Response\x12\x33\n\x06vector\x18\x01 \x01(\x0b\x32\x19.payload.v1.Object.VectorH\x00R\x06vector\x12,\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x06statusB\t\n\x07payload\"E\n\x07\x43ontrol\x1a:\n\x12\x43reateIndexRequest\x12$\n\tpool_size\x18\x01 \x01(\rB\x07\xbaH\x04*\x02(\x00R\x08poolSize\"f\n\nDiscoverer\x1aX\n\x07Request\x12\x1b\n\x04name\x18\x01 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x04name\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x12\n\x04node\x18\x03 \x01(\tR\x04node\"\x8c\r\n\x04Info\x1a\xca\x01\n\x05Index\x1au\n\x05\x43ount\x12\x16\n\x06stored\x18\x01 \x01(\rR\x06stored\x12 \n\x0buncommitted\x18\x02 \x01(\rR\x0buncommitted\x12\x1a\n\x08indexing\x18\x03 \x01(\x08R\x08indexing\x12\x16\n\x06saving\x18\x04 \x01(\x08R\x06saving\x1aJ\n\x04UUID\x1a\x1f\n\tCommitted\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x1a!\n\x0bUncommitted\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x1a\xef\x01\n\x03Pod\x12\x19\n\x08\x61pp_name\x18\x01 \x01(\tR\x07\x61ppName\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1c\n\tnamespace\x18\x03 \x01(\tR\tnamespace\x12\x17\n\x02ip\x18\x04 \x01(\tB\x07\xbaH\x04r\x02x\x01R\x02ip\x12&\n\x03\x63pu\x18\x05 \x01(\x0b\x32\x14.payload.v1.Info.CPUR\x03\x63pu\x12/\n\x06memory\x18\x06 \x01(\x0b\x32\x17.payload.v1.Info.MemoryR\x06memory\x12)\n\x04node\x18\x07 \x01(\x0b\x32\x15.payload.v1.Info.NodeR\x04node\x1a\xe8\x01\n\x04Node\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rinternal_addr\x18\x02 \x01(\tR\x0cinternalAddr\x12#\n\rexternal_addr\x18\x03 \x01(\tR\x0c\x65xternalAddr\x12&\n\x03\x63pu\x18\x04 \x01(\x0b\x32\x14.payload.v1.Info.CPUR\x03\x63pu\x12/\n\x06memory\x18\x05 \x01(\x0b\x32\x17.payload.v1.Info.MemoryR\x06memory\x12)\n\x04Pods\x18\x06 \x01(\x0b\x32\x15.payload.v1.Info.PodsR\x04Pods\x1a\x82\x02\n\x07Service\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\ncluster_ip\x18\x02 \x01(\tR\tclusterIp\x12\x1f\n\x0b\x63luster_ips\x18\x03 \x03(\tR\nclusterIps\x12\x32\n\x05ports\x18\x04 \x03(\x0b\x32\x1c.payload.v1.Info.ServicePortR\x05ports\x12/\n\x06labels\x18\x05 \x01(\x0b\x32\x17.payload.v1.Info.LabelsR\x06labels\x12>\n\x0b\x61nnotations\x18\x06 \x01(\x0b\x32\x1c.payload.v1.Info.AnnotationsR\x0b\x61nnotations\x1a\x35\n\x0bServicePort\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04port\x18\x02 \x01(\x05R\x04port\x1a\x80\x01\n\x06Labels\x12;\n\x06labels\x18\x01 \x03(\x0b\x32#.payload.v1.Info.Labels.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x9e\x01\n\x0b\x41nnotations\x12O\n\x0b\x61nnotations\x18\x01 \x03(\x0b\x32-.payload.v1.Info.Annotations.AnnotationsEntryR\x0b\x61nnotations\x1a>\n\x10\x41nnotationsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1aK\n\x03\x43PU\x12\x14\n\x05limit\x18\x01 \x01(\x01R\x05limit\x12\x18\n\x07request\x18\x02 \x01(\x01R\x07request\x12\x14\n\x05usage\x18\x03 \x01(\x01R\x05usage\x1aN\n\x06Memory\x12\x14\n\x05limit\x18\x01 \x01(\x01R\x05limit\x12\x18\n\x07request\x18\x02 \x01(\x01R\x07request\x12\x14\n\x05usage\x18\x03 \x01(\x01R\x05usage\x1a:\n\x04Pods\x12\x32\n\x04pods\x18\x01 \x03(\x0b\x32\x14.payload.v1.Info.PodB\x08\xbaH\x05\x92\x01\x02\x08\x01R\x04pods\x1a>\n\x05Nodes\x12\x35\n\x05nodes\x18\x01 \x03(\x0b\x32\x15.payload.v1.Info.NodeB\x08\xbaH\x05\x92\x01\x02\x08\x01R\x05nodes\x1aJ\n\x08Services\x12>\n\x08services\x18\x01 \x03(\x0b\x32\x18.payload.v1.Info.ServiceB\x08\xbaH\x05\x92\x01\x02\x08\x01R\x08services\x1a\x15\n\x03IPs\x12\x0e\n\x02ip\x18\x01 \x03(\tR\x02ip\"\x07\n\x05\x45mptyBd\n\x1dorg.vdaas.vald.api.v1.payloadB\x0bValdPayloadP\x01Z*github.com/vdaas/vald/apis/grpc/v1/payload\xa2\x02\x07Payloadb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vald.v1.payload.payload_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035org.vdaas.vald.api.v1.payloadB\013ValdPayloadP\001Z*github.com/vdaas/vald/apis/grpc/v1/payload\242\002\007Payload'
  _globals['_SEARCH_REQUEST'].fields_by_name['vector']._options = None
  _globals['_SEARCH_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_SEARCH_CONFIG'].fields_by_name['num']._options = None
  _globals['_SEARCH_CONFIG'].fields_by_name['num']._serialized_options = b'\272H\004*\002(\001'
  _globals['_SEARCH_CONFIG'].fields_by_name['min_num']._options = None
  _globals['_SEARCH_CONFIG'].fields_by_name['min_num']._serialized_options = b'\272H\004*\002(\000'
  _globals['_INSERT_REQUEST'].fields_by_name['vector']._options = None
  _globals['_INSERT_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_UPDATE_REQUEST'].fields_by_name['vector']._options = None
  _globals['_UPDATE_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_UPSERT_REQUEST'].fields_by_name['vector']._options = None
  _globals['_UPSERT_REQUEST'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_VECTORREQUEST'].fields_by_name['id']._options = None
  _globals['_OBJECT_VECTORREQUEST'].fields_by_name['id']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_ID'].fields_by_name['id']._options = None
  _globals['_OBJECT_ID'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_OBJECT_VECTOR'].fields_by_name['id']._options = None
  _globals['_OBJECT_VECTOR'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_OBJECT_VECTOR'].fields_by_name['vector']._options = None
  _globals['_OBJECT_VECTOR'].fields_by_name['vector']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_GETTIMESTAMPREQUEST'].fields_by_name['id']._options = None
  _globals['_OBJECT_GETTIMESTAMPREQUEST'].fields_by_name['id']._serialized_options = b'\272H\005\222\001\002\010\002'
  _globals['_OBJECT_TIMESTAMP'].fields_by_name['id']._options = None
  _globals['_OBJECT_TIMESTAMP'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_OBJECT_BLOB'].fields_by_name['id']._options = None
  _globals['_OBJECT_BLOB'].fields_by_name['id']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_CONTROL_CREATEINDEXREQUEST'].fields_by_name['pool_size']._options = None
  _globals['_CONTROL_CREATEINDEXREQUEST'].fields_by_name['pool_size']._serialized_options = b'\272H\004*\002(\000'
  _globals['_DISCOVERER_REQUEST'].fields_by_name['name']._options = None
  _globals['_DISCOVERER_REQUEST'].fields_by_name['name']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_INFO_POD'].fields_by_name['ip']._options = None
  _globals['_INFO_POD'].fields_by_name['ip']._serialized_options = b'\272H\004r\002x\001'
  _globals['_INFO_LABELS_LABELSENTRY']._options = None
  _globals['_INFO_LABELS_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._options = None
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_INFO_PODS'].fields_by_name['pods']._options = None
  _globals['_INFO_PODS'].fields_by_name['pods']._serialized_options = b'\272H\005\222\001\002\010\001'
  _globals['_INFO_NODES'].fields_by_name['nodes']._options = None
  _globals['_INFO_NODES'].fields_by_name['nodes']._serialized_options = b'\272H\005\222\001\002\010\001'
  _globals['_INFO_SERVICES'].fields_by_name['services']._options = None
  _globals['_INFO_SERVICES'].fields_by_name['services']._serialized_options = b'\272H\005\222\001\002\010\001'
  _globals['_SEARCH']._serialized_start=100
  _globals['_SEARCH']._serialized_end=1489
  _globals['_SEARCH_REQUEST']._serialized_start=110
  _globals['_SEARCH_REQUEST']._serialized_end=204
  _globals['_SEARCH_MULTIREQUEST']._serialized_start=206
  _globals['_SEARCH_MULTIREQUEST']._serialized_end=276
  _globals['_SEARCH_IDREQUEST']._serialized_start=278
  _globals['_SEARCH_IDREQUEST']._serialized_end=356
  _globals['_SEARCH_MULTIIDREQUEST']._serialized_start=358
  _globals['_SEARCH_MULTIIDREQUEST']._serialized_end=432
  _globals['_SEARCH_OBJECTREQUEST']._serialized_start=435
  _globals['_SEARCH_OBJECTREQUEST']._serialized_end=584
  _globals['_SEARCH_MULTIOBJECTREQUEST']._serialized_start=586
  _globals['_SEARCH_MULTIOBJECTREQUEST']._serialized_end=668
  _globals['_SEARCH_CONFIG']._serialized_start=671
  _globals['_SEARCH_CONFIG']._serialized_end=1075
  _globals['_SEARCH_RESPONSE']._serialized_start=1077
  _globals['_SEARCH_RESPONSE']._serialized_end=1173
  _globals['_SEARCH_RESPONSES']._serialized_start=1175
  _globals['_SEARCH_RESPONSES']._serialized_end=1245
  _globals['_SEARCH_STREAMRESPONSE']._serialized_start=1248
  _globals['_SEARCH_STREAMRESPONSE']._serialized_end=1380
  _globals['_SEARCH_AGGREGATIONALGORITHM']._serialized_start=1382
  _globals['_SEARCH_AGGREGATIONALGORITHM']._serialized_end=1489
  _globals['_FILTER']._serialized_start=1491
  _globals['_FILTER']._serialized_end=1612
  _globals['_FILTER_TARGET']._serialized_start=1501
  _globals['_FILTER_TARGET']._serialized_end=1549
  _globals['_FILTER_CONFIG']._serialized_start=1551
  _globals['_FILTER_CONFIG']._serialized_end=1612
  _globals['_INSERT']._serialized_start=1615
  _globals['_INSERT']._serialized_end=2228
  _globals['_INSERT_REQUEST']._serialized_start=1625
  _globals['_INSERT_REQUEST']._serialized_end=1746
  _globals['_INSERT_MULTIREQUEST']._serialized_start=1748
  _globals['_INSERT_MULTIREQUEST']._serialized_end=1818
  _globals['_INSERT_OBJECTREQUEST']._serialized_start=1821
  _globals['_INSERT_OBJECTREQUEST']._serialized_end=1995
  _globals['_INSERT_MULTIOBJECTREQUEST']._serialized_start=1997
  _globals['_INSERT_MULTIOBJECTREQUEST']._serialized_end=2079
  _globals['_INSERT_CONFIG']._serialized_start=2082
  _globals['_INSERT_CONFIG']._serialized_end=2228
  _globals['_UPDATE']._serialized_start=2231
  _globals['_UPDATE']._serialized_end=2900
  _globals['_UPDATE_REQUEST']._serialized_start=2241
  _globals['_UPDATE_REQUEST']._serialized_end=2362
  _globals['_UPDATE_MULTIREQUEST']._serialized_start=2364
  _globals['_UPDATE_MULTIREQUEST']._serialized_end=2434
  _globals['_UPDATE_OBJECTREQUEST']._serialized_start=2437
  _globals['_UPDATE_OBJECTREQUEST']._serialized_end=2611
  _globals['_UPDATE_MULTIOBJECTREQUEST']._serialized_start=2613
  _globals['_UPDATE_MULTIOBJECTREQUEST']._serialized_end=2695
  _globals['_UPDATE_CONFIG']._serialized_start=2698
  _globals['_UPDATE_CONFIG']._serialized_end=2900
  _globals['_UPSERT']._serialized_start=2903
  _globals['_UPSERT']._serialized_end=3572
  _globals['_UPSERT_REQUEST']._serialized_start=2913
  _globals['_UPSERT_REQUEST']._serialized_end=3034
  _globals['_UPSERT_MULTIREQUEST']._serialized_start=3036
  _globals['_UPSERT_MULTIREQUEST']._serialized_end=3106
  _globals['_UPSERT_OBJECTREQUEST']._serialized_start=3109
  _globals['_UPSERT_OBJECTREQUEST']._serialized_end=3283
  _globals['_UPSERT_MULTIOBJECTREQUEST']._serialized_start=3285
  _globals['_UPSERT_MULTIOBJECTREQUEST']._serialized_end=3367
  _globals['_UPSERT_CONFIG']._serialized_start=2698
  _globals['_UPSERT_CONFIG']._serialized_end=2900
  _globals['_REMOVE']._serialized_start=3575
  _globals['_REMOVE']._serialized_end=4104
  _globals['_REMOVE_REQUEST']._serialized_start=3585
  _globals['_REMOVE_REQUEST']._serialized_end=3684
  _globals['_REMOVE_MULTIREQUEST']._serialized_start=3686
  _globals['_REMOVE_MULTIREQUEST']._serialized_end=3756
  _globals['_REMOVE_TIMESTAMPREQUEST']._serialized_start=3758
  _globals['_REMOVE_TIMESTAMPREQUEST']._serialized_end=3838
  _globals['_REMOVE_TIMESTAMP']._serialized_start=3841
  _globals['_REMOVE_TIMESTAMP']._serialized_end=4009
  _globals['_REMOVE_TIMESTAMP_OPERATOR']._serialized_start=3951
  _globals['_REMOVE_TIMESTAMP_OPERATOR']._serialized_end=4009
  _globals['_REMOVE_CONFIG']._serialized_start=4011
  _globals['_REMOVE_CONFIG']._serialized_end=4104
  _globals['_OBJECT']._serialized_start=4107
  _globals['_OBJECT']._serialized_end=5567
  _globals['_OBJECT_VECTORREQUEST']._serialized_start=4117
  _globals['_OBJECT_VECTORREQUEST']._serialized_end=4234
  _globals['_OBJECT_DISTANCE']._serialized_start=4236
  _globals['_OBJECT_DISTANCE']._serialized_end=4290
  _globals['_OBJECT_STREAMDISTANCE']._serialized_start=4293
  _globals['_OBJECT_STREAMDISTANCE']._serialized_end=4425
  _globals['_OBJECT_ID']._serialized_start=4427
  _globals['_OBJECT_ID']._serialized_end=4456
  _globals['_OBJECT_IDS']._serialized_start=4458
  _globals['_OBJECT_IDS']._serialized_end=4481
  _globals['_OBJECT_VECTOR']._serialized_start=4483
  _globals['_OBJECT_VECTOR']._serialized_end=4580
  _globals['_OBJECT_GETTIMESTAMPREQUEST']._serialized_start=4582
  _globals['_OBJECT_GETTIMESTAMPREQUEST']._serialized_end=4652
  _globals['_OBJECT_TIMESTAMP']._serialized_start=4654
  _globals['_OBJECT_TIMESTAMP']._serialized_end=4720
  _globals['_OBJECT_VECTORS']._serialized_start=4722
  _globals['_OBJECT_VECTORS']._serialized_end=4784
  _globals['_OBJECT_STREAMVECTOR']._serialized_start=4786
  _globals['_OBJECT_STREAMVECTOR']._serialized_end=4910
  _globals['_OBJECT_RESHAPEVECTOR']._serialized_start=4912
  _globals['_OBJECT_RESHAPEVECTOR']._serialized_end=4973
  _globals['_OBJECT_BLOB']._serialized_start=4975
  _globals['_OBJECT_BLOB']._serialized_end=5030
  _globals['_OBJECT_STREAMBLOB']._serialized_start=5032
  _globals['_OBJECT_STREAMBLOB']._serialized_end=5148
  _globals['_OBJECT_LOCATION']._serialized_start=5150
  _globals['_OBJECT_LOCATION']._serialized_end=5218
  _globals['_OBJECT_STREAMLOCATION']._serialized_start=5221
  _globals['_OBJECT_STREAMLOCATION']._serialized_end=5353
  _globals['_OBJECT_LOCATIONS']._serialized_start=5355
  _globals['_OBJECT_LOCATIONS']._serialized_end=5425
  _globals['_OBJECT_LIST']._serialized_start=5428
  _globals['_OBJECT_LIST']._serialized_end=5567
  _globals['_OBJECT_LIST_REQUEST']._serialized_start=110
  _globals['_OBJECT_LIST_REQUEST']._serialized_end=119
  _globals['_OBJECT_LIST_RESPONSE']._serialized_start=5447
  _globals['_OBJECT_LIST_RESPONSE']._serialized_end=5567
  _globals['_CONTROL']._serialized_start=5569
  _globals['_CONTROL']._serialized_end=5638
  _globals['_CONTROL_CREATEINDEXREQUEST']._serialized_start=5580
  _globals['_CONTROL_CREATEINDEXREQUEST']._serialized_end=5638
  _globals['_DISCOVERER']._serialized_start=5640
  _globals['_DISCOVERER']._serialized_end=5742
  _globals['_DISCOVERER_REQUEST']._serialized_start=5654
  _globals['_DISCOVERER_REQUEST']._serialized_end=5742
  _globals['_INFO']._serialized_start=5745
  _globals['_INFO']._serialized_end=7421
  _globals['_INFO_INDEX']._serialized_start=5754
  _globals['_INFO_INDEX']._serialized_end=5956
  _globals['_INFO_INDEX_COUNT']._serialized_start=5763
  _globals['_INFO_INDEX_COUNT']._serialized_end=5880
  _globals['_INFO_INDEX_UUID']._serialized_start=5882
  _globals['_INFO_INDEX_UUID']._serialized_end=5956
  _globals['_INFO_INDEX_UUID_COMMITTED']._serialized_start=5890
  _globals['_INFO_INDEX_UUID_COMMITTED']._serialized_end=5921
  _globals['_INFO_INDEX_UUID_UNCOMMITTED']._serialized_start=5923
  _globals['_INFO_INDEX_UUID_UNCOMMITTED']._serialized_end=5956
  _globals['_INFO_POD']._serialized_start=5959
  _globals['_INFO_POD']._serialized_end=6198
  _globals['_INFO_NODE']._serialized_start=6201
  _globals['_INFO_NODE']._serialized_end=6433
  _globals['_INFO_SERVICE']._serialized_start=6436
  _globals['_INFO_SERVICE']._serialized_end=6694
  _globals['_INFO_SERVICEPORT']._serialized_start=6696
  _globals['_INFO_SERVICEPORT']._serialized_end=6749
  _globals['_INFO_LABELS']._serialized_start=6752
  _globals['_INFO_LABELS']._serialized_end=6880
  _globals['_INFO_LABELS_LABELSENTRY']._serialized_start=6823
  _globals['_INFO_LABELS_LABELSENTRY']._serialized_end=6880
  _globals['_INFO_ANNOTATIONS']._serialized_start=6883
  _globals['_INFO_ANNOTATIONS']._serialized_end=7041
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._serialized_start=6979
  _globals['_INFO_ANNOTATIONS_ANNOTATIONSENTRY']._serialized_end=7041
  _globals['_INFO_CPU']._serialized_start=7043
  _globals['_INFO_CPU']._serialized_end=7118
  _globals['_INFO_MEMORY']._serialized_start=7120
  _globals['_INFO_MEMORY']._serialized_end=7198
  _globals['_INFO_PODS']._serialized_start=7200
  _globals['_INFO_PODS']._serialized_end=7258
  _globals['_INFO_NODES']._serialized_start=7260
  _globals['_INFO_NODES']._serialized_end=7322
  _globals['_INFO_SERVICES']._serialized_start=7324
  _globals['_INFO_SERVICES']._serialized_end=7398
  _globals['_INFO_IPS']._serialized_start=7400
  _globals['_INFO_IPS']._serialized_end=7421
  _globals['_EMPTY']._serialized_start=7423
  _globals['_EMPTY']._serialized_end=7430
# @@protoc_insertion_point(module_scope)
