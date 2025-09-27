from yta_constants.enum import YTAEnum as Enum


class PexelsLocale(Enum):
    """
    Enum class to represent the languages that
    are available for the Pexels plataform.
    """
    
    ES_ES: str = 'es-ES'
    """
    Spanish of Spain.
    """

class PexelsOrientation(Enum):
    """
    Enum class to represent the options we
    have for the 'orientation' parameter.

    Check: https://www.pexels.com/api/documentation/#videos-search__parameters__orientation

    TODO: These ones are, at least, for
    the 'image' search.
    """

    LANDSCAPE: str = 'landscape'
    PORTRAIT: str = 'portrait'
    # TODO: Does 'square' exist (?)
    SQUARE: str = 'square'

# TODO: Maybe rename to PexelsQuality (?)
class PexelsImageSize(Enum):
    """
    Enum class to represent the options we
    have for the 'size' parameter when 
    receiving images in a response. These
    are the options we obtain inside the
    'src' attribute.

    Check:
    - https://www.pexels.com/api/documentation/#photos-overview__response__src

    TODO: These ones are, at least, for 
    the 'image' search.
    """

    # TODO: Is 'original' size or orientation (?)
    ORIGINAL: str = 'original'
    LARGE_2X: str = 'large2x'
    LARGE: str = 'large'
    """
    4K.
    """
    MEDIUM: str = 'medium'
    """
    Full HD.
    """
    SMALL: str = 'small'
    """
    HD.
    """
    TINY: str = 'tiny'

class PexelsSizeFilter(Enum):
    """
    Enum class to represent the size filters
    we can use when requesting for images or
    videos.

    Check:
    - https://www.pexels.com/api/documentation/#photos-search__parameters__size
    - https://www.pexels.com/api/documentation/#videos-search__parameters__size
    """
    LARGE = 'large'
    """
    A minimum of 24MP in images, 4K in videos.
    """
    MEDIUM = 'medium'
    """
    A minimum of 12MP in images, Full HD in videos.
    """
    SMALL = 'small'
    """
    A minimum of 4Mp in images, HD in videos.
    """

class PexelsVideoQuality(Enum):
    """
    The quality of the video files received
    as response when searching for videos
    in the Pexels platform.

    Check: https://www.pexels.com/api/documentation/#videos-overview__response__video_files____quality
    """

    HD = 'hd'
    SD = 'sd'
    HLS = 'hls'
    """
    This quality does not include size.
    """

"""
Be careful, there is a difference. The
filter we use when searching, that doesn't
include 'landscape' nor 'portrait' when
used as 'size', and other thing is the
'orientation', that is the one that includes
the 'landscape' and 'portrait' values. But
when we receive the response, all those are
mixed in the 'src' field, that includes
'tiny' but also 'landscape'.
"""