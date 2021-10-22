# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class SearchStub(object):
    """Search service provides ways to search indexed vectors.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/vald.v1.Search/Search',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
                )
        self.SearchByID = channel.unary_unary(
                '/vald.v1.Search/SearchByID',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
                )
        self.StreamSearch = channel.stream_stream(
                '/vald.v1.Search/StreamSearch',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.FromString,
                )
        self.StreamSearchByID = channel.stream_stream(
                '/vald.v1.Search/StreamSearchByID',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.FromString,
                )
        self.MultiSearch = channel.unary_unary(
                '/vald.v1.Search/MultiSearch',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.FromString,
                )
        self.MultiSearchByID = channel.unary_unary(
                '/vald.v1.Search/MultiSearchByID',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiIDRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.FromString,
                )


class SearchServicer(object):
    """Search service provides ways to search indexed vectors.
    """

    def Search(self, request, context):
        """A method to search indexed vectors by a raw vector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByID(self, request, context):
        """A method to search indexed vectors by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamSearch(self, request_iterator, context):
        """A method to search indexed vectors by multiple vectors.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamSearchByID(self, request_iterator, context):
        """A method to search indexed vectors by multiple IDs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiSearch(self, request, context):
        """A method to search indexed vectors by multiple vectors in a single request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiSearchByID(self, request, context):
        """A method to search indexed vectors by multiple IDs in a single request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.SerializeToString,
            ),
            'SearchByID': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByID,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.SerializeToString,
            ),
            'StreamSearch': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamSearch,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.SerializeToString,
            ),
            'StreamSearchByID': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamSearchByID,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.SerializeToString,
            ),
            'MultiSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiSearch,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.SerializeToString,
            ),
            'MultiSearchByID': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiSearchByID,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiIDRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vald.v1.Search', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Search(object):
    """Search service provides ways to search indexed vectors.
    """

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Search/Search',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Search/SearchByID',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamSearch(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Search/StreamSearch',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Request.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamSearchByID(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/vald.v1.Search/StreamSearchByID',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.IDRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.StreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Search/MultiSearch',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiSearchByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vald.v1.Search/MultiSearchByID',
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.MultiIDRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Search.Responses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
