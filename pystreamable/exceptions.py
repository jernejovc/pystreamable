from __future__ import print_function


class StreamableApiException(Exception):
    """
    Base class for all Streamable API wrapper exceptions.
    """
    pass


class StreamableApiServerException(StreamableApiException):
    """
    Streamable API server exception.
    """
    pass


class StreamableApiClientException(StreamableApiException):
    """
    Streamable API client exception.
    """
    pass
