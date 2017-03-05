from __future__ import print_function
from __future__ import absolute_import

from .exceptions import StreamableApiException


class Authentication:
    """
    Internal authentication info class.
    """
    _username = None
    _password = None

    def __init__(self, username=None, password=None):
        """
        Constructor, either both username and password are provided or neither
        is. If only one is present an exception is thrown
        :param username: streamable.com username
        :param password: streamable.com password
        """
        if not username and password or username and not password:
            raise StreamableApiException(
                "API with authentication can only be used with both username"
                "and password.")
        self._username = username
        self._password = password

    def get_auth(self):
        """
        Return authentication tuple.
        """
        return self._username, self._password

    def has_auth(self):
        """
        Returns true if authentication info is available.
        """
        return self._username and self._password
