from yta_constants.enum import YTAEnum as Enum


class PixabayVideoType(Enum):
    """
    The different types of video we can use
    as filters.

    Check: https://pixabay.com/api/docs/#api_search_videos
    """

    ALL = 'all'
    """
    All the types at the same time.
    """
    FILM = 'film'
    ANIMATION = 'animation'

class PixabayVideoQuality(Enum):
    """
    The different video qualities we can obtain
    as response.

    Check: https://pixabay.com/api/docs/#api_search_videos
    """

    LARGE = 'large'
    """
    Usually has a dimension of 2840x2160. If not
    available, empty url returned and size of 0.
    """
    MEDIUM = 'medium'
    """
    Usually has a dimension of 1920x1080. Older
    videos have a dimension of 1280x720. Available
    for all the videos.
    """
    SMALL = 'small'
    """
    Usually has a dimension of 1280x720. Older videos
    have a dimension of 960x540. Available for all
    the videos.
    """
    TINY = 'tiny'
    """
    Usually has a dimension of 960x540. Older videos
    have a dimension of 640x360. Available for all
    the videos.
    """

    @staticmethod
    def get_values_ordered(
    ):
        """
        The values but ordered by priority. This method
        was built to make sure this order is specifically
        set here and switching the values above doesn't
        make the software malfunction.
        """
        return [
            PixabayVideoQuality.LARGE.value,
            PixabayVideoQuality.MEDIUM.value,
            PixabayVideoQuality.SMALL.value,
            PixabayVideoQuality.TINY.value
        ]

# TODO: Create 'PixabayVideoCategory' (?)