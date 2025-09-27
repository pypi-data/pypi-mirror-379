"""
@DEPRECATED

Code migrated to other 4 libraries, better
organized and modularized. Code has changed
a bit from this project even in the first
versions of the other libraries. I commit
this just to push the code and mark it as
@deprecated.

See:
- 'yta_stock'
- 'yta_stock_pixabay'
- 'yta_stock_pexels'
- 'yta_stock_common'
"""
from yta_stock_downloader.pexels.enums import PexelsOrientation, PexelsSizeFilter
from yta_stock_downloader.pexels.settings import PexelsSettings
from yta_stock_downloader.pixabay.api import PixabayApi
from yta_stock_downloader.pexels.api import PexelsApi
from yta_stock_downloader.pixabay.dataclasses import PixabayImage, PixabayVideo
from yta_stock_downloader.pexels.dataclasses import PexelsImage, PexelsVideo
from yta_stock_downloader.pexels.enums import PexelsLocale
from yta_programming.output import Output
from yta_validation.parameter import ParameterValidator
from yta_constants.file import FileType
from typing import Union
from abc import ABC, abstractmethod
from typing import Union


__all__ = [
    'Stock'
]

class _StockDownloader(ABC):
    """
    Class to wrap the functionality related to
    downloading stock images and videos.

    This class must be inherited from the 
    specific classes that implement the 
    platform-specific functionality.
    """

    def __init__(
        self,
        do_ignore_ids: bool = False
    ):
        self._do_ignore_ids: bool = do_ignore_ids
        """
        The internal flag to indicate if the previously
        downloaded resources have to be ignored or not.
        """
        self._ids_to_ignore: list[int] = []
        """
        The internal list of ids that must be ignored
        when trying to download a new one.
        """

    def activate_ignore_ids(
        self
    ) -> None:
        """
        Set as True the internal flag that indicates 
        that the ids of the videos that are downloaded
        after being activated have to be ignored in 
        the next downloads, so each video is downloaded
        only once.
        """
        self._do_ignore_ids = True

    def deactivate_ignore_ids(
        self
    ) -> None:
        """
        Set as False the internal flag that indicates 
        that the ids of the videos that are downloaded
        after being activated have to be ignored in 
        the next downloads, so each video can be 
        downloaded an unlimited amount of times.
        """
        self._do_ignore_ids = True

    def reset(
        self
    ):
        """
        This method will empty the array that handles 
        the duplicated ids (if activated) to enable 
        downloading any image found again.
        """
        self._ids_to_ignore = []

    def _get_ids_to_ignore(
        self,
        ids_to_ignore: list[int]
    ):
        """
        *For internal use only*

        Get the list of ids to ignore based on the 
        'ids_to_ignore' passed as parameter and also
        the ones holded in the instance, without
        duplicities.

        If the option of the instance is set to not
        ignore ids, the only ids to ignore will be 
        the ones passed as the 'ids_to_ignore'
        parameter.
        """
        return (
            list(set(ids_to_ignore + self._ids_to_ignore))
            if self._do_ignore_ids else
            ids_to_ignore
        )
    
    def _append_id(
        self,
        id: int
    ):
        """
        *For internal use only*

        Append the provided 'id' to the internal list
        of ids to ignore, but only if the internal flag
        to do it is activated and the id is not already
        in the list.
        """
        if (
            self._do_ignore_ids and
            id not in self._ids_to_ignore
        ):
            self._ids_to_ignore.append(id)

    @abstractmethod
    def download(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ):
        """
        Download the first available image from the
        platform and stores it locally with the
        'output_filename' name provided.
        """
        pass

    @abstractmethod
    def download_random(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ):
        """
        Download a random available image from the
        platform and stores it locally with the
        'output_filename' name provided.
        """
        pass

# class StockImageDownloader(_StockDownloader):
#     """
#     Class to download stock images from the
#     different platforms available.
    
#     This is a general image downloader which
#     will choose by itself the platform from
#     which obtain the images. If you need a
#     platform-specific stock image downloader,
#     use one of the specific classes.
#     """

#     def __init__(
#         self,
#         do_ignore_ids: bool = False
#     ):
#         self._do_ignore_ids = do_ignore_ids
#         self._pexels_downloader = _PexelsImageDownloader(do_ignore_ids)
#         self._pixabay_downloader = _PixabayImageDownloader(do_ignore_ids)

#     def reset(
#         self
#     ):
#         """
#         This method will empty the array that handles 
#         the duplicated ids (if activated) to enable 
#         downloading any image found again. This method
#         will also reset its platform-specific 
#         downloader instances.
#         """
#         self._pexels_downloader.reset()
#         self._pixabay_downloader.reset()

#     def download(
#         self,
#         query: str,
#         ids_to_ignore: list[int] = [],
#         output_filename: Union[str, None] = None
#     ) -> 'FileReturned':
#         """
#         Download an image from the first platform that
#         has results according to the provided 'query'
#         and stores it locally.
#         """
#         output_filename = Output.get_filename(output_filename, FileType.IMAGE)

#         image = self._pexels_downloader.download(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if image is not None:
#             return image
        
#         image = self._pixabay_downloader.download(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if image is not None:
#             return image
        
#         # TODO: Use another provider when available
#         raise Exception('No results found with any of our providers.')
    
#     def download_random(
#         self,
#         query: str,
#         ids_to_ignore: list[int] = [],
#         output_filename: Union[str, None] = None
#     ) -> 'FileReturned':
#         """
#         Download a random image from the first platform
#         that has results according to the provided 'query'
#         and stores it locally.
#         """
#         output_filename = Output.get_filename(output_filename, FileType.IMAGE)

#         image = self._pexels_downloader.download_random(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if image is not None:
#             return image
        
#         image = self._pixabay_downloader.download_random(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if image is not None:
#             return image
        
#         # TODO: Use another provider when available
#         raise Exception('No results found with any of our providers.')

# class StockVideoDownloader(_StockDownloader):
#     """
#     Class to download stock videos from the
#     different platforms available.
    
#     This is a general video downloader which
#     will choose by itself the platform from
#     which obtain the videos. If you need a
#     platform-specific stock video downloader,
#     use one of the specific classes.
#     """

#     def __init__(
#         self,
#         do_ignore_ids: bool = False
#     ):
#         self._do_ignore_ids = do_ignore_ids
#         self._pexels_downloader = _PexelsVideoDownloader(do_ignore_ids)
#         self._pixabay_downloader = _PixabayVideoDownloader(do_ignore_ids)

#     def reset(
#         self
#     ):
#         """
#         This method will empty the array that handles 
#         the duplicated ids (if activated) to enable 
#         downloading any image found again. This method
#         will also reset its platform-specific 
#         downloader instances.
#         """
#         self._pexels_downloader.reset()
#         self._pixabay_downloader.reset()

#     def download(
#         self,
#         query: str,
#         ids_to_ignore: list[int] = [],
#         output_filename: Union[str, None] = None
#     ) -> 'FileReturned':
#         """
#         Download a video from the first platform that
#         has results according to the provided 'query'
#         and stores it locally.
#         """
#         output_filename = Output.get_filename(output_filename, FileType.VIDEO)

#         video = self._pexels_downloader.download(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if video is not None:
#             return video
        
#         video = self._pixabay_downloader.download(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if video is not None:
#             return video
        
#         # TODO: Use another provider when available
#         raise Exception('No results found with any of our providers.')
    
#     def download_random(
#         self,
#         query: str,
#         ids_to_ignore: list[int] = [],
#         output_filename: Union[str, None] = None
#     ) -> 'FileReturned':
#         """
#         Download a random video from the first platform
#         that has results according to the provided 'query'
#         and stores it locally.
#         """
#         output_filename = Output.get_filename(output_filename, FileType.VIDEO)

#         video = self._pexels_downloader.download_random(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if video is not None:
#             return video
        
#         video = self._pixabay_downloader.download_random(
#             query = query,
#             ids_to_ignore = ids_to_ignore,
#             output_filename = output_filename
#         )

#         if video is not None:
#             return video
        
#         # TODO: Use another provider when available
#         raise Exception('No results found with any of our providers.')


class StockPlatforms:
    """
    Class to handle the functionality related
    to downloading stock images or videos with
    different stock APIs.

    It is just a wrapper of the different
    providers we have, but doesn't add any
    extra functionality.
    """

    def __init__(
        self,
        do_ignore_repeated: bool = False
    ):
        self._do_ignore_repeated: bool = do_ignore_repeated
        """
        Internal flag to indicate if we are 
        ignoring the repeated resources or not.
        """
        self.pixabay: Pixabay = Pixabay(
            do_ignore_repeated_images = do_ignore_repeated,
            do_ignore_repeated_videos = do_ignore_repeated
        )
        """
        The Pixabay stock handler.
        """
        self.pexels: Pexels = Pexels(
            do_ignore_repeated_images = do_ignore_repeated,
            do_ignore_repeated_videos = do_ignore_repeated
        )
        """
        The Pexels stock handler.
        """

    def reset(
        self
    ):
        """
        This method will empty the array that handles 
        the duplicated ids (if activated) to enable 
        downloading any image found again. This method
        will also reset its platform-specific 
        downloader instances.
        """
        self.pexels.reset()
        self.pixabay.reset()


class _PexelsImageDownloader(_StockDownloader):
    """
    Class to provide images from the Pexels platform.

    This class uses the Pexels API and our registered
    API key to obtain the results.

    See: https://www.pexels.com/
    """

    def get_first(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        ids_to_ignore: list[int] = []
    ) -> Union[PexelsImage, None]:
        """
        Obtain the first available image from the Pexels
        provider for the given 'query' and 'locale' (if
        available).
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        return PexelsApi.image.get_one(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )
    
    def get_random(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        ids_to_ignore: list[int] = []
    ) -> Union[PexelsImage, None]:
        """
        Obtain a random image from the Pexels provider
        for the given 'query' and 'locale' (if available).
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        return PexelsApi.image.get_random(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )
    
    def download(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download the first image that is available in the
        Pexels provider for the given 'query' and 'locale'
        (if available).
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        image = self.get_first(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            _download_image(self, image, output_filename)
            if image is not None else
            None
        )
    
    def download_random(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download a random image that is available in the
        Pexels provider for the given 'query' and 'locale'
        (if available).
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        image = self.get_random(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            _download_image(self, image, output_filename)
            if image is not None else
            None
        )
    
class _PexelsVideoDownloader(_StockDownloader):
    """
    Class to provide videos from the Pexels platform.

    This class uses the Pexels API and our registered
    API key to obtain the results.

    See: https://www.pexels.com/
    """

    def get_first(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        ids_to_ignore: list[int] = []
    ) -> Union[PexelsVideo, None]:
        """
        Obtain the first available video from the Pexels
        provider for the given 'query' and 'locale' (if
        available).
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        return PexelsApi.video.get_one(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )
    
    def get_random(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        ids_to_ignore: list[int] = []
    ) -> Union[PexelsVideo, None]:
        """
        Obtain a random video that is available in the
        Pexels provider for the given 'query' and
        'locale' (if available).
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        return PexelsApi.video.get_random(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            ids_to_ignore = self._get_ids_to_ignore(ids_to_ignore)
        )

    def download(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download the first video available in the Pexels
        platform with the given 'query' and 'locale' (if
        existing), avoiding the ones in the 'ids_to_ignore' 
        list.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        video = self.get_first(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            ids_to_ignore = ids_to_ignore,
        )

        return (
            _download_video(self, video, output_filename)
            if video is not None else
            None
        )
    
    def download_random(
        self,
        query: str,
        locale: Union[PexelsLocale, str] = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> Union['FileReturned', None]:
        """
        Download a random video available in the Pexels
        platform with the given 'query' and 'locale' (if
        existing), avoiding the ones in the 'ids_to_ignore' 
        list.
        """
        ParameterValidator.validate_mandatory_string('query', query, do_accept_empty = False)
        ParameterValidator.validate_list_of_string('ids_to_ignore', ids_to_ignore)
        locale = PexelsLocale.to_enum(locale)

        video = self.get_random(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            ids_to_ignore = ids_to_ignore,
        )

        return (
            _download_video(self, video, output_filename)
            if video is not None else
            None
        )
    
class Pexels:
    """
    Class to wrap the functionality related to
    the Pexels images and videos provider.
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
        self.images: _PexelsImageDownloader = _PexelsImageDownloader(
            do_ignore_ids = do_ignore_repeated_images
        )
        """
        Shortcut to the image related functionalities.
        """
        self.videos: _PexelsVideoDownloader = _PexelsVideoDownloader(
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
    

    
# TODO: I should implement a way of using pagination
# and look for next page results if not found in the
# current page and a behaviour like that

class _StockImage:
    """
    The images section of the main stock class,
    to be instantiated and used internally by 
    the Stock class.
    """

    def __init__(
        self,
        pixabay: Pixabay,
        pexels: Pexels
    ):
        self._pixabay: Pixabay = pixabay
        """
        The Pixabay stock handler.
        """
        self._pexels: Pexels = pexels
        """
        The Pexels stock handler.
        """

    def reset(
        self
    ):
        """
        This method will empty the array that handles 
        the duplicated ids (if activated) to enable 
        downloading any image found again. This method
        will also reset its platform-specific 
        downloader instances.
        """
        self._pixabay.images.reset()
        self._pexels.images.reset()

    def download(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download an image from the first platform that
        has results according to the provided 'query'
        and stores it locally.
        """
        output_filename = Output.get_filename(output_filename, FileType.IMAGE)

        image = self._pexels.images.download(
            query = query,
            # TODO: This cannot be customized by now
            locale = PexelsLocale.ES_ES,
            orientation = PexelsOrientation.LANDSCAPE,
            size = PexelsSizeFilter.LARGE,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if image is not None:
            return image
        
        image = self._pixabay.images.download(
            query = query,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if image is not None:
            return image
        
        # TODO: Use another provider when available
        raise Exception('No results found with any of our providers.')
    
    def download_random(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download a random image from the first platform
        that has results according to the provided 'query'
        and stores it locally.
        """
        output_filename = Output.get_filename(output_filename, FileType.IMAGE)

        image = self._pexels.images.download_random(
            query = query,
            # TODO: This cannot be customized by now
            locale = PexelsLocale.ES_ES,
            orientation = PexelsOrientation.LANDSCAPE,
            size = PexelsSizeFilter.LARGE,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if image is not None:
            return image
        
        image = self._pixabay.images.download_random(
            query = query,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if image is not None:
            return image
        
        # TODO: Use another provider when available
        raise Exception('No results found with any of our providers.')
        
class _StockVideo:
    """
    The videos section of the main stock class,
    to be instantiated and used internally by 
    the Stock class.
    """

    def __init__(
        self,
        pixabay: Pixabay,
        pexels: Pexels
    ):
        """
        The StockB class must instantiate this one
        by providing its own providers instances.
        """
        self._pixabay: Pixabay = pixabay
        """
        The Pixabay stock handler.
        """
        self._pexels: Pexels = pexels
        """
        The Pexels stock handler.
        """

    def reset(
        self
    ):
        """
        This method will empty the array that handles 
        the duplicated ids (if activated) to enable 
        downloading any image found again. This method
        will also reset its platform-specific 
        downloader instances.
        """
        self._pixabay.videos.reset()
        self._pexels.videos.reset()

    def download(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download a video from the first platform that
        has results according to the provided 'query'
        and stores it locally.
        """
        output_filename = Output.get_filename(output_filename, FileType.VIDEO)

        video = self._pexels.videos.download(
            query = query,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if video is not None:
            return video
        
        video = self._pixabay.videos.download(
            query = query,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if video is not None:
            return video
        
        # TODO: Use another provider when available
        raise Exception('No results found with any of our providers.')
    
    def download_random(
        self,
        query: str,
        ids_to_ignore: list[int] = [],
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download a random video from the first platform
        that has results according to the provided 'query'
        and stores it locally.
        """
        output_filename = Output.get_filename(output_filename, FileType.VIDEO)

        video = self._pexels.videos.download_random(
            query = query,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if video is not None:
            return video
        
        video = self._pixabay.videos.download_random(
            query = query,
            ids_to_ignore = ids_to_ignore,
            output_filename = output_filename
        )

        if video is not None:
            return video
        
        # TODO: Use another provider when available
        raise Exception('No results found with any of our providers.')

class Stock:
    """
    Class to handle the functionality related
    to downloading stock images or videos with
    different stock APIs.
    """

    def __init__(
        self,
        do_ignore_repeated: bool = False
    ):
        self._do_ignore_repeated: bool = do_ignore_repeated
        """
        Internal flag to indicate if we are 
        ignoring the repeated resources or not.
        """

        self._pixabay: Pixabay = Pixabay(
            do_ignore_repeated_images = do_ignore_repeated,
            do_ignore_repeated_videos = do_ignore_repeated
        )
        """
        The Pixabay stock handler.
        """
        self._pexels: Pexels = Pexels(
            do_ignore_repeated_images = do_ignore_repeated,
            do_ignore_repeated_videos = do_ignore_repeated
        )
        """
        The Pexels stock handler.
        """

        self.images: _StockImage = _StockImage(
            pixabay = self._pixabay,
            pexels = self._pexels
        )
        """
        Handling images using different providers.
        """
        self.videos: _StockVideo = _StockVideo(
            pixabay = self._pixabay,
            pexels = self._pexels
        )
        """
        Handling videos using different providers.
        """

    def reset(
        self
    ):
        """
        This method will empty the array that handles 
        the duplicated ids (if activated) to enable 
        downloading any image found again. This method
        will also reset its platform-specific 
        downloader instances.
        """
        self.videos.reset()
        self.images.reset()

def _download_image(
    self: Union[_PixabayImageDownloader, _PexelsImageDownloader],
    image: Union[PixabayImage],
    output_filename: Union[str, None] = None
):
    """
    *For internal use only*

    Method to try to download the image and
    store, if successfully downloaded, the
    id in the 'self' instance list of ids to
    ignore.
    """
    try:
        download = image.download(Output.get_filename(output_filename, FileType.IMAGE))
        self._append_id(image.id)
    except:
        # TODO: Handle the exception
        download = None

    return download

def _download_video(
    self: Union[_PixabayVideoDownloader, _PexelsImageDownloader],
    video: Union[PixabayVideo, PexelsVideo],
    output_filename: Union[str, None] = None
):
    """
    *For internal use only*

    Method to try to download the video and
    store, if successfully downloaded, the
    id in the 'self' instance list of ids to
    ignore.
    """
    try:
        download = video.download(Output.get_filename(output_filename, FileType.VIDEO))
        self._append_id(video.id)
    except:
        # TODO: Handle the exception
        download = None

    return download