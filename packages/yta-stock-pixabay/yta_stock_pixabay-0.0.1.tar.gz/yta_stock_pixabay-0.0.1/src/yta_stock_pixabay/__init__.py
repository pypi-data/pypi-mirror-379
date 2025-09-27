from yta_stock_common import _download_image, _download_video
from yta_stock_pixabay.dataclasses import PixabayImage, PixabayVideo
from yta_stock_pixabay.api import PixabayApi
from yta_stock_common import _StockDownloader
from yta_validation.parameter import ParameterValidator
from typing import Union


class _PixabayImageDownloader(_StockDownloader):
    """
    Class to provide images and videos from the Pixabay
    platform.

    This class uses the Pixabay API and our registered
    API key to obtain the results.

    See: https://pixabay.com/
    """

    def get_first(
        self,
        query: str,
        ids_to_ignore: list[int] = []
    ) -> Union[PixabayImage, None]:
        """
        Obtain the first image that is available in the
        Pexels provider for the given 'query'.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        return PixabayApi.image.get_one(
            query = query,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )
    
    def get_random(
        self,
        query: str,
        ids_to_ignore: list[int] = []
    ) -> Union[PixabayImage, None]:
        """
        Obtain a random image that is available in the
        Pexels provider for the given 'query'.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        return PixabayApi.image.get_random(
            query = query,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )
    
    def download(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download the first image that is available in the
        Pexels platform for the given 'query'.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        image = self.get_first(query, ids_to_ignore)

        return (
            # This is to add the 'id' to the list
            _download_image(self, image, output_filename)
            if image is not None else
            None
        )
    
    def download_random(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download a random image that is available in the
        Pexels platform for the given 'query'.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        image = self.get_random(query, ids_to_ignore)

        return (
            # This is to add the 'id' to the list
            _download_image(self, image, output_filename)
            if image is not None else
            None
        )
    
class _PixabayVideoDownloader(_StockDownloader):
    """
    Class to provide videos from the Pixabay platform.

    This class uses the Pixabay API and our registered
    API key to obtain the results.

    See: https://pixabay.com/
    """

    def get_first(
        self,
        query: str,
        ids_to_ignore: list[int] = []
    ) -> Union[PixabayVideo, None]:
        """
        Obtain the first video that is available in the
        Pixabay platform for the given 'query'.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        return PixabayApi.video.get_one(
            query = query,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )
    
    def get_random(
        self,
        query: str,
        ids_to_ignore: list[int] = []
    ) -> Union[PixabayVideo, None]:
        """
        Obtain a random video that is available in the
        Pixabay platform for the given 'query'.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        return PixabayApi.video.get_random(
            query = query,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )

    def download(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download the first video that is available in the
        Pexels platform for the given 'query' avoiding
        the ones in the 'ids_to_ignore' list.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        video = self.get_first(
            query = query,
            ids_to_ignore = ids_to_ignore
        )

        return (
            _download_video(self, video, output_filename)
            if video is not None else
            None
        )
    
    def download_random(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download a random video that is available in the
        Pexels platform for the given 'query' avoiding
        the ones in the 'ids_to_ignore' list.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)

        video = self.get_random(
            query = query,
            ids_to_ignore = ids_to_ignore
        )
        
        return (
            _download_video(self, video, output_filename)
            if video is not None else
            None
        )
    
class Pixabay:
    """
    Class to wrap the functionality related to
    the Pixabay images and videos provider.
    """

    def __init__(
        self,
        do_ignore_repeated_images: bool = False,
        do_ignore_repeated_videos: bool = False
    ):
        """
        If you download a resource (image or video)
        and the corresponding boolean parameter is
        False, that same resource could be downloaded
        again in the next requests if the filters
        match it. Set it at True to avoid downloading
        repeated resources (during the life time of
        this instance).

        If you are downloading videos or images to
        build a big video, set it at False so you
        make sure the resources are not repeated in
        your final video and the repeated ones are
        ignored when trying to download.
        """
        self.images: _PixabayImageDownloader = _PixabayImageDownloader(
            do_ignore_ids = do_ignore_repeated_images
        )
        """
        Shortcut to the image related functionalities.
        """
        self.videos: _PixabayVideoDownloader = _PixabayVideoDownloader(
            do_ignore_ids = do_ignore_repeated_videos
        )
        """
        Shortcut to the video related functionalities.
        """

    def reset(
        self
    ) -> 'Pixabay':
        """
        Reset the ids stored to be ignored and not
        repeated when downloading, for both images
        and videos.
        """
        self.images.reset()
        self.videos.reset()

        return self