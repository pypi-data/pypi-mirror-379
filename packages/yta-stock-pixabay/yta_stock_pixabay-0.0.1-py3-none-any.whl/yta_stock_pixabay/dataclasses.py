from yta_stock_pixabay.enum import PixabayVideoQuality
from yta_file_downloader import Downloader
from yta_programming.output import Output
from yta_constants.file import FileType
from dataclasses import dataclass
from typing import Union


@dataclass
class PixabayImage:
    """
    Class to represent a Pixabay image and to
    simplify the way we work with its data.
    """

    @property
    def id(
        self
    ) -> int:
        """
        The unique identifier of the image.
        """
        return self._data['id']
    
    @property
    def size(
        self
    ) -> tuple[int, int]:
        """
        The size of the image.
        """
        return (self._data['imageWidth'], self._data['imageHeight'])
    
    @property
    def file_size(
        self
    ) -> int:
        """
        The size of the image file (in bytes?).
        """
        return self._data['imageSize']
    
    @property
    def display_url(
        self
    ) -> str:
        """
        The url in which the image will be displayed.
        """
        return self._data['pageURL']
    
    @property
    def tags(
        self
    ) -> list[str]:
        """
        The tags of the image.
        """
        # It comes like this: "puppy, dog, nature"
        return [
            tag.strip()
            for tag in self._data['tags'].split(',')
        ]
    
    @property
    def number_of_views(
        self
    ) -> int:
        """
        The amount of views the display url has
        received.
        """
        return self._data['views']
    
    @property
    def number_of_downloads(
        self
    ) -> int:
        """
        The amount of times the video has been
        downloaded.
        """
        return self._data['downloads']
    
    @property
    def number_of_likes(
        self
    ) -> int:
        """
        The amount of times the people liked the
        video.
        """
        return self._data['likes']
    
    @property
    def author(
        self
    ) -> dict:
        """
        The author of the image, including the
        'id', 'name' and 'avatar_url' fields.
        """
        return {
            'id': self._data['user_id'],
            'name': self._data['user'],
            'avatar_url': self._data['userImageURL']
        }
    
    @property
    def is_ai(
        self
    ) -> bool:
        """
        Flag to indicate if the image has been generated
        with artificial intelligence (ai) or not.
        """
        return self._data['isAiGenerated']
    
    @property
    def download_url_180w(
        self
    ) -> str:
        """
        The download url for the image with a width
        of 180 pixels.

        Use `.download_url` for the best resolution.
        """
        return self.download_url_640w.replace('_640.', '_180.')
    
    @property
    def download_url_340w(
        self
    ) -> str:
        """
        The download url for the image with a width
        of 340 pixels.

        Use `.download_url` for the best resolution.
        """
        return self.download_url_640w.replace('_640.', '_340.')
    
    @property
    def download_url_640w(
        self
    ) -> str:
        """
        The download url for the image with a width
        of 640 pixels, valid only during 24 hours.

        Use `.download_url` for the best resolution.
        """
        
        return self._data['webformatURL']

    @property
    def download_url_960w(
        self
    ) -> str:
        """
        The download url for the image with a width
        of 960 pixels.

        Use `.download_url` for the best resolution.
        """
        return self.download_url_640w.replace('_640.', '_960.')
    
    @property
    def download_url_1280w(
        self
    ) -> str:
        """
        The download url for the image with a width
        of 1280 pixels.

        Use `.download_url` for the best resolution.
        """
        return self._data['largeImageURL']
    
    @property
    def download_url_fullhd(
        self
    ) -> Union[str, None]:
        """
        *Only accessible when fully registered in API*

        The download url of the image scaled to 1920px.

        This can be None if the request is made with
        not enough privileges.
        """
        return getattr(self._data, 'fullHDURL', None)
    
    @property
    def download_url_original(
        self
    ) -> Union[str, None]:
        """
        *Only accessible when fully registered in API*

        The download url of the original image (as it
        was uploaded) that fits the 'self.size'
        property.

        This can be None if the request is made with
        not enough privileges.
        """
        return getattr(self._data, 'imageURL', None)
    
    @property
    def download_url_vector(
        self
    ) -> Union[str, None]:
        """
        *Only accessible when fully registered in API*

        The download url of the original but as a vector
        (only if available).

        This can be None if the request is made with
        not enough privileges or the image doesn't have
        a vector version.
        """
        return getattr(self._data, 'vectorURL', None)

    @property
    def download_url(
        self
    ):
        """
        The download url of the option with the highest
        quality available.
        """
        return (
            self.download_url_original
            if self.download_url_original is not None else
            # TODO: Maybe check if 'size' > 1920 to send
            # the 'fullhd' instead (?)
            self.download_url_fullhd
            if self.download_url_fullhd is not None else
            self.download_url_1280w
            # This '1280' above is always available
        )
    
    @property
    def as_json(self):
        """
        Return the object instance as a json to be
        displayed and debugged.
        """
        return {
            'id': self.id,
            'size': self.size,
            'file_size': self.file_size,
            'display_url': self.display_url,
            'tags': self.tags,
            'number_of_views': self.number_of_views,
            'number_of_downloads': self.number_of_downloads,
            'number_of_likes': self.number_of_likes,
            'author': self.author,
            'is_ai': self.is_ai,
            'download_urls': {
                '180': self.download_url_180w,
                '340': self.download_url_340w,
                '640': self.download_url_640w,
                '960': self.download_url_960w,
                '1280': self.download_url_1280w,
                'vector': self.download_url_vector,
                'original': self.download_url_original,
                'fullHD': self.download_url_fullhd,
            }
        }

    def __init__(
        self,
        data: any
    ):
        self._data: dict = data
        """
        The original data as it was received in the
        response.
        """

    def download(
        self,
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download the current Pixabay image to the provided
        'output_filename' (or, if not provided, to a 
        temporary file).

        This method returns the final 'output_filename' 
        of the downloaded image.
        """
        return Downloader.download_image(
            self.download_url,
            Output.get_filename(output_filename, FileType.IMAGE)
        )

@dataclass
class PixabayVideoSource:
    """
    Class to represent one source of a video from
    the Pixabay platform, that has a specific
    quality.

    A video is uploaded to the platform and has
    different resolutions and file sizes. This
    class represent each of those resolutions.
    """

    @property
    def thumbnail_url(
        self
    ) -> str:
        """
        The url of the thumbnail of the video.
        """
        return self._data['thumbnail']
    
    @property
    def download_url(
        self
    ) -> str:
        """
        The url to download the video file.
        """
        return self._data['url']
    
    @property
    def file_extension(
        self
    ) -> str:
        """
        The extension of the video file.
        """
        return self.download_url.split('.')[-1]
    
    @property
    def size(
        self
    ) -> tuple[int, int]:
        """
        The size of the video in the format
        (width, height).
        """
        return (self._data['width'], self._data['height'])

    @property
    def file_size(
        self
    ) -> int:
        """
        The size of the video file (in bytes (?)).
        """
        return self._data['size']
    
    @property
    def as_json(
        self
    ) -> dict:
        """
        The instance but as a json (dict in python).
        """
        return {
            'quality': self.quality,
            'thumbnail_url': self.thumbnail_url,
            'download_url': self.download_url,
            'file_extension': self.file_extension,
            'size': self.size,
            'file_size': self.file_size
        }

    def __init__(
        self,
        quality: str,
        data: dict
    ):
        # TODO: If we don't receive the 'quality'
        # in the 'data', we need to pass it when
        # instantiating this class
        self.quality: str = quality
        """
        The quality of the video according to the
        Pixabay platform. It can be 'large',
        'medium', 'small', 'tiny'.
        """
        self._data: dict = data
        """
        The raw data of the video, obtained from
        the response.
        """
    
    def download(
        self,
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download this video source to the provided
        local 'output_filename'. If no
        'output_filename' is provided, it will be
        stored locally with a temporary name.

        This method returns a FileReturned instance.
        """
        return Downloader.download_video(
            self.download_url,
            Output.get_filename(output_filename, FileType.VIDEO)
        )

@dataclass
class PixabayVideo:
    """
    Class to represent a video of the Pixabay platform and
    to handle it easier than as raw data. A video has the
    main information but also different video formats and
    qualities that can be used for different purposes.
    Maybe we want a landscape video or maybe a portrait, so
    both of them could be available as 'video_files' for
    the same video content.
    """

    @property
    def id(
        self
    ) -> int:
        """
        Unique identifier for this video in the Pixabay
        platform.
        """
        return self._data['id']
    
    @property
    def display_url(
        self
    ) -> str:
        """
        The url in which the video is displayed.
        """
        return self._data['pageURL']
    
    @property
    def type(
        self
    ) -> str:
        """
        The type of the video, that can be a parameter
        to filter the results.
        """
        return self._data['type']
    
    @property
    def duration(
        self
    ) -> int:
        """
        The duration in seconds, and I think that
        rounded up, provided by the platform.
        """
        return self._data['duration']
    
    @property
    def number_of_views(
        self
    ) -> int:
        """
        The amount of views the display url has
        received.
        """
        return self._data['views']
    
    @property
    def number_of_downloads(
        self
    ) -> int:
        """
        The amount of times the video has been
        downloaded.
        """
        return self._data['downloads']
    
    @property
    def number_of_likes(
        self
    ) -> int:
        """
        The amount of times the people liked the
        video.
        """
        return self._data['likes']
    
    @property
    def author(
        self
    ) -> dict:
        """
        The information about the author, including
        'id', 'name' and 'avatar_url'.
        """
        return {
            'id': self._data['user_id'],
            'name': self._data['user'],
            'avatar_url': self._data['userImageURL']
        }
    
    @property
    def sources(
        self
    ) -> list[PixabayVideoSource]:
        """
        The video sources but as instances and ordered
        by the lowest quality to the best one. If the
        quality does not exist ('large' quality could
        not exist) it is omitted.
        """
        if not hasattr(self, '_sources'):
            sources = [
                PixabayVideoSource(
                    quality = quality,
                    data = data
                )
                for quality, data in self._data['videos'].items()
            ]

            # Map 'id' -> position
            pos = {
                quality: i
                for i, quality in enumerate(PixabayVideoQuality.get_values_ordered())
            }

            # Order with that position
            self._sources = sorted(
                (
                    source
                    for source in sources
                    if source.quality in pos
                ),
                key = lambda source: pos[source.quality],
                # We want it from lower quality to the best one
                reverse = True
            )

        return self._sources
    
    @property
    def best_video(
        self
    ) -> Union[PixabayVideoSource, None]:
        """
        The information about the video source with
        the best quality found in the response.
        """
        return self.sources[-1]
    
    @property
    def as_json(
        self
    ) -> dict:
        """
        Return the object instance as a json to be
        displayed and debugged.
        """
        return {
            'id': self.id,
            'display_url': self.display_url,
            'type': self.type,
            'duration': self.duration,
            'number_of_views': self.number_of_views,
            'number_of_downloads': self.number_of_downloads,
            'number_of_likes': self.number_of_likes,
            'author': self.author,
            'sources': [
                source.as_json
                for source in self.sources
            ],
            'best_video': self.best_video.as_json
        }

    def __init__(
        self,
        data: any
    ):
        self._data: dict = data
        """
        The original data provided in the response.
        """
    
    # TODO: Implement a functionality to download
    # the different qualities
    def download(
        self,
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download this video to the provided local
        'output_filename'. If no 'output_filename'
        is provided, it will be stored locally with
        a temporary name.

        This method returns a FileReturned instance.
        """
        return self.best_video.download(
            output_filename = output_filename
        )


"""
Information for the developer:
The 'webformatURL' parameter can be modified to
choose another sizes according to the suffix
you use.

The default value is '_640', which is for the
image with 640 pixels of width.

Example of url:
- https://pixabay.com/get/g1947f60f32cb33a297990650daf95a92ed988e0af032dec98ea25bf4aee234542c7b0ec9febf9f871b576efb6c99b1dbd4049541ee1d7eb69898175b66b8b9c2_640.jpg

So we have:
- _180
- _340
- _640 (actual default value)
- _960 (it means 960 x 720)
"""