from __future__ import print_function
from __future__ import absolute_import

import requests

from .exceptions import (StreamableApiClientException,
                         StreamableApiServerException)
from .utils import Authentication

STREAMABLE_URL = 'https://streamable.com'
API_ROOT = 'https://api.streamable.com'
UPLOAD_URL = API_ROOT + '/upload'
RETRIEVE_URL = API_ROOT + '/videos/%s'
IMPORT_URL = API_ROOT + '/import'


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
        Args:
            username: streamable.com username
            password: streamable.com password
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
        Args:
            filename: Path to video to be uploaded
            title: Optional title for the video, if not present streamable uses
                   filename as title

        Returns:
            JSON with uploaded video data.
        """
        data = None
        files = {'file': open(filename, 'rb')}
        if title:
            data = {'title': title}
        resp = self._api_request(UPLOAD_URL, requests.post, data, files)
        return resp.json()

    def _api_request(self, url, method, data=None, files=None):
        auth = self.authentication.get_auth() \
            if self.authentication.has_auth() else None
        resp = method(url=url,
                      data=data if data else None,
                      files=files if files else None,
                      auth=auth)
        if 200 >= resp.status_code < 300:
            return resp
        if 400 >= resp.status_code < 500:
            raise StreamableApiClientException(resp.text)
        if 500 >= resp.status_code < 600:
            raise StreamableApiServerException(resp.text)

        raise RuntimeError(resp.text)
