"""
Pixabay image and video download API.

See more: https://pixabay.com/api/docs/
"""
from yta_stock_pixabay.settings import PixabaySettings, PixabayEndpoints
from yta_stock_pixabay.dataclasses import PixabayVideo, PixabayImage
from yta_programming.output import Output
from yta_constants.file import FileType
from random import choice
from typing import Union

import requests


class _PixabayRawImagesApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the images in the raw Pixabay API.
    """

    @staticmethod
    def get(
        query: str,
        # TODO: What values are available (?)
        orientation: str = 'horizontal',
        # TODO: Should we accept 'image_type' (?)
        timeout: int = 10
    ) -> dict:
        """
        Send a search request throw the pixabay
        images with the provided 'query' and get
        the ones matching that query.

        TODO: This is not handling pages.
        """
        return requests.get(
            PixabayEndpoints.API_ENDPOINT_URL,
            {
                'key': PixabaySettings.API_KEY,
                'q': query,
                'orientation': orientation,
                'image_type': 'photo'
            },
            timeout = timeout
        ).json()

class _PixabayRawVideosApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the videos in the raw Pixabay API.
    """

    @staticmethod
    def get(
        query: str,
        # TODO: Should we accept 'video_type' (?)
        timeout: int = 10
    ) -> dict:
        """
        Send a search request throw the pixabay
        videos with the provided 'query' and get
        the ones matching that query.

        TODO: This is not handling pages.
        """
        return requests.get(
            url = PixabayEndpoints.VIDEOS_API_ENDPOINT_URL,
            params = {
                'key': PixabaySettings.API_KEY,
                'q': query,
                'video_type': 'film',
                'pretty': 'true'
            },
            timeout = timeout
        ).json()

class PixabayRawAPI:
    """
    Class to wrap the functionality related
    to the raw Pixabay API with no data
    conversion, handling the information as
    it is returned by the official endpoints.

    You need a valid API KEY activated and
    set in the .env file to be able to obtain
    a valid response.
    """

    video: _PixabayRawVideosApi = _PixabayRawVideosApi
    """
    Shortcut to the endpoints related to videos.
    """
    image: _PixabayRawImagesApi = _PixabayRawImagesApi
    """
    Shortcut to the endpoints related to images.
    """

class _PixabayImagesApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the images of our own Pixabay API 
    that formats and wraps the raw API.
    """

    @staticmethod
    def get(
        query: str,
        ids_to_ignore: list[str] = []
    ) -> list[PixabayImage]:
        """
        Search videos for the given 'query' ignoring
        the ones with an id that is contained in the
        'ids_to_ignore' parameter provided. They will
        be returned in the order they were given but
        as PixabayImage instances.

        TODO: This is not handling pages.
        """
        response = PixabayRawAPI.image.get(
            query = query,
            timeout = 10
        )

        return (
            []
            if response['total'] == 0 else
            [
                PixabayImage(image)
                for image in response['hits']
                if image['id'] not in ids_to_ignore
            ]
        )
    
    def get_one(
        query: str,
        ids_to_ignore: list[str] = []
    ) -> Union[PixabayImage, None]:
        """
        Search for the images with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        the first one (if results available).
        """
        images = _PixabayImagesApi.get(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            images[0]
            if len(images) > 0 else
            None
        )
    
    def get_random(
        query: str,
        ids_to_ignore: list[str] = []
    ) -> Union[PixabayImage, None]:
        """
        Search for the images with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        a random one (if results available).
        """
        images = _PixabayImagesApi.get(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            choice(images)
            if len(images) > 0 else
            None
        )
    
    def download_one(
        query: str,
        ids_to_ignore: list[str] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Search for teh images with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and download
        the first one (if results available).

        This method returns a 'FileReturned' instance.
        """
        image = _PixabayImagesApi.get_one(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            image.download(Output.get_filename(output_filename, FileType.IMAGE))
            if image is not None else
            None
        )
    
    def download_random(
        query: str,
        ids_to_ignore: list[str] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Search for the images with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and download
        a random one (if results available).

        This method returns a 'FileReturned' instance.
        """
        image = _PixabayImagesApi.get_random(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            image.download(Output.get_filename(output_filename, FileType.IMAGE))
            if image is not None else
            None
        )

class _PixabayVideosApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the videos of our own Pixabay API 
    that formats and wraps the raw API.
    """

    @staticmethod
    def get(
        query: str,
        ids_to_ignore: list[str] = []
    ) -> list[PixabayVideo]:
        """
        Search videos for the given 'query' ignoring
        the ones with an id that is contained in the
        'ids_to_ignore' parameter provided. They will
        be returned in the order they were given but
        as PixabayVideo instances.

        TODO: This is not handling pages.
        """
        response = PixabayRawAPI.video.get(
            query = query,
            timeout = 10
        )

        return (
            []
            if response['total'] == 0 else
            [
                PixabayVideo(video)
                for video in response['hits']
                if video['id'] not in ids_to_ignore
            ]
        )
    
    def get_one(
        query: str,
        ids_to_ignore: list[str] = []
    ) -> Union[PixabayVideo, None]:
        """
        Search for the videos with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        the first one (if results available).
        """
        videos = _PixabayVideosApi.get(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            videos[0]
            if len(videos) > 0 else
            None
        )
    
    def get_random(
        query: str,
        ids_to_ignore: list[str] = []
    ) -> Union[PixabayVideo, None]:
        """
        Search for the videos with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        a random one (if results available).
        """
        videos = _PixabayVideosApi.get(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            choice(videos)
            if len(videos) > 0 else
            None
        )
    
    def download_one(
        query: str,
        ids_to_ignore: list[str] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Search for teh videos with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and download
        the first one (if results available).

        This method returns a 'FileReturned' instance.
        """
        video = _PixabayVideosApi.get_one(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            video.download(Output.get_filename(output_filename, FileType.VIDEO))
            if video is not None else
            None
        )
    
    def download_random(
        query: str,
        ids_to_ignore: list[str] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Search for the videos with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and download
        a random one (if results available).

        This method returns a 'FileReturned' instance.
        """
        video = _PixabayVideosApi.get_random(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            video.download(Output.get_filename(output_filename, FileType.VIDEO))
            if video is not None else
            None
        )

class PixabayApi:
    """
    Class to wrap the functionality related
    to our own Pixabay API, which uses the
    raw Pixabay API and formats and wraps
    the information to make easier reading
    and manipulating the data.
    """

    video: _PixabayVideosApi = _PixabayVideosApi
    """
    Shortcut to the endpoints related to videos.
    """
    image: _PixabayImagesApi = _PixabayImagesApi
    """
    Shortcut to the endpoints related to images.
    """