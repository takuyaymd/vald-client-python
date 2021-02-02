# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class FilterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchObject = channel.unary_unary(
                '/vald.v1.Filter/SearchObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
                )
        self.MultiSearchObject = channel.unary_unary(
                '/vald.v1.Filter/MultiSearchObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.FromString,
                )
        self.StreamSearchObject = channel.stream_stream(
                '/vald.v1.Filter/StreamSearchObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.FromString,
                )
        self.InsertObject = channel.unary_unary(
                '/vald.v1.Filter/InsertObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamInsertObject = channel.stream_stream(
                '/vald.v1.Filter/StreamInsertObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
                )
        self.MultiInsertObject = channel.unary_unary(
                '/vald.v1.Filter/MultiInsertObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.MultiObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )
        self.UpdateObject = channel.unary_unary(
                '/vald.v1.Filter/UpdateObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Update.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamUpdateObject = channel.stream_stream(
                '/vald.v1.Filter/StreamUpdateObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Update.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
                )
        self.MultiUpdateObject = channel.unary_unary(
                '/vald.v1.Filter/MultiUpdateObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Update.MultiObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )
        self.UpsertObject = channel.unary_unary(
                '/vald.v1.Filter/UpsertObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
                )
        self.StreamUpsertObject = channel.stream_stream(
                '/vald.v1.Filter/StreamUpsertObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.ObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
                )
        self.MultiUpsertObject = channel.unary_unary(
                '/vald.v1.Filter/MultiUpsertObject',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.MultiObjectRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
                )


class FilterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiSearchObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamSearchObject(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamInsertObject(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiInsertObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUpdateObject(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiUpdateObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpsertObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUpsertObject(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiUpsertObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FilterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchObject': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.SerializeToString,
            ),
            'MultiSearchObject': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiSearchObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.SerializeToString,
            ),
            'StreamSearchObject': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamSearchObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.SerializeToString,
            ),
            'InsertObject': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamInsertObject': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamInsertObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.SerializeToString,
            ),
            'MultiInsertObject': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiInsertObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Insert.MultiObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
            'UpdateObject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Update.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamUpdateObject': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamUpdateObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Update.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.SerializeToString,
            ),
            'MultiUpdateObject': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiUpdateObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Update.MultiObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
            'UpsertObject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpsertObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.SerializeToString,
            ),
            'StreamUpsertObject': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamUpsertObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.ObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.SerializeToString,
            ),
            'MultiUpsertObject': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiUpsertObject,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.MultiObjectRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vald.v1.Filter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Filter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/SearchObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiSearchObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/MultiSearchObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamSearchObject(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Filter/StreamSearchObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/InsertObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Insert.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamInsertObject(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Filter/StreamInsertObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Insert.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiInsertObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/MultiInsertObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Insert.MultiObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/UpdateObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Update.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamUpdateObject(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Filter/StreamUpdateObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Update.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiUpdateObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/MultiUpdateObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Update.MultiObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpsertObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/UpsertObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamUpsertObject(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Filter/StreamUpsertObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.ObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.StreamLocation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiUpsertObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Filter/MultiUpsertObject',
            vald_dot_v1_dot_payload_dot_payload__pb2.Upsert.MultiObjectRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Object.Locations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
