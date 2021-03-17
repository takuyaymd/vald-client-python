# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class UpsertStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upsert = channel.unary_unary(
                '/vald.v1.Upsert/Upsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamUpsert = channel.stream_stream(
                '/vald.v1.Upsert/StreamUpsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
                )
        self.MultiUpsert = channel.unary_unary(
                '/vald.v1.Upsert/MultiUpsert',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.MultiRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )


class UpsertServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Upsert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUpsert(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiUpsert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpsertServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upsert': grpc.unary_unary_rpc_method_handler(
                    servicer.Upsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamUpsert': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamUpsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.SerializeToString,
            ),
            'MultiUpsert': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiUpsert,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.MultiRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vald.v1.Upsert', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Upsert(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Upsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Upsert/Upsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamUpsert(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Upsert/StreamUpsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiUpsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Upsert/MultiUpsert',
            vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.MultiRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)