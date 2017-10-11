from __future__ import print_function
from __future__ import absolute_import

import requests

from .exceptions import (StreamableApiClientException,
                         StreamableApiServerException)
from .utils import Authentication

__author__ = 'Matej Repinc'
__email__ = 'mrepinc@gmail.com'
__version__ = '1.0.1'
__license__ = 'MIT'


STREAMABLE_URL = 'https://streamable.com'
API_ROOT = 'https://api.streamable.com'
UPLOAD_URL = API_ROOT + '/upload'
RETRIEVE_URL = API_ROOT + '/videos/%s'
IMPORT_URL = API_ROOT + '/import'
RETRIEVE_USER_URL = API_ROOT + '/users/%s'
AUTH_USER_URL = API_ROOT + '/me'
USER_AGENT = {'user-agent': 'pystreamable/%s (api.streamable.com python wrapper)' % __version__ }


class StreamableApi:
    """
    streamable.com API wrapper.
    """
    authentication = Authentication()

    def __init__(self, username=None, password=None):
        """
        Create a new instance of the API.
        If you provide username and password the uploads will be stored in your
        account.
        :param username: streamable.com username
        :param password: streamable.com password
        """
        self.authentication = Authentication(username, password)

    def get_info(self, video_id):
        """
        Get video info for video with given video ID.
        Args:
            video_id: Streamable short video id

        Returns:
            JSON with video data.
        """
        url = RETRIEVE_URL % video_id
        resp = self._api_request(url, requests.get)
        return resp.json()

    def upload_video(self, filename, title=None):
        """
        Upload a video to streamable.com. Works with absolute and relative
        paths.
        :param filename: Path to video to be uploaded
        :param title: Optional title for the video, if not present streamable
                      uses filename as title
        :return: JSON with uploaded video data.
        """
        data = None
        with open(filename, 'rb') as infile:
            files = {'file': infile}
            if title:
                data = {'title': title}
            resp = self._api_request(UPLOAD_URL,
                                     requests.post,
                                     data=data,
                                     files=files)
            return resp.json()

    def retrieve_user(self, username):
        """
        Retrieves user info.
        :param username: username for which to get user info
        :return: JSON with user info
        """
        url = RETRIEVE_USER_URL % username
        resp = self._api_request(url, requests.get)
        return resp.json()

    def auth_user_info(self):
        """
        Get authenticated user info.
        :return: JSON with info of authenticated user.
        """
        resp = self._api_request(AUTH_USER_URL, requests.get)
        return resp.json()

    def import_video(self, url, title=None):
        """
        Imports a video from video hosted on external site.
        :param url: URL to video file or webpage containing a video
        :param title: Optional title of uploaded video
        :return: JSON with uploaded video data
        """
        payload = {'url': url}
        if title:
            payload['title'] = title
        resp = self._api_request(IMPORT_URL, requests.get, payload=payload)
        return resp.json()

    def _api_request(self, url, method, payload=None, data=None, files=None):
        auth = self.authentication.get_auth() \
            if self.authentication.has_auth() else None
        resp = method(url=url,
                      params=payload,
                      data=data if data else None,
                      files=files if files else None,
                      auth=auth,
                      headers=USER_AGENT)
        if 200 >= resp.status_code < 300:
            return resp
        if 400 >= resp.status_code < 500:
            raise StreamableApiClientException(resp.text)
        if 500 >= resp.status_code < 600:
            raise StreamableApiServerException(resp.text)

        raise RuntimeError(resp.text)
