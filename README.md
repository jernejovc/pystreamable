# pystreamable
streamable.com API wrapper for Python 2.7+.

**NOTE:** Work in progress, feature requests and bug reports welcome.

## Installation
Currently only available on github. When cloned, run 

`pip install -r requirements.pip`

to install dependecies (currently just `requests`).

## Usage
### Creating an instance of StreamableApi
```
from pystreamable import StreamableApi
api = StreamableApi()
```
This will create an instance of `StreamableApi` without authentication.

If you wish to upload videos to your account, use
`api = StreamableApi('username', 'password)`

### Retrieving video info
`api.get_info('shortcode')`

This will return a `dict` with values as described on ['Retrieve a video' part of Streamable API Docs](https://streamable.com/documentation)

### Uploading a video
`api.upload_video('/path/to/video.mp4', 'Video title')`

This will return a `dict` with values as described on ['Upload a video file' part of Streamable API Docs](https://streamable.com/documentation).

The video title parameter is not mandatory, if not provided streamable will create the video title from video filename (`video.mp4` in the case above) 

