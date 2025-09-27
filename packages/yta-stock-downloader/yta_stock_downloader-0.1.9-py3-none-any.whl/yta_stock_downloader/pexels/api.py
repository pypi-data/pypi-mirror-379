"""
Pexels image and video download API.

Check these files for some response
examples:
- test_files/pexels_image_request.json
- test_files/pexels_video_request.json

See more: https://www.pexels.com/api/documentation/
"""
from yta_stock_downloader.pexels.settings import PexelsSettings, PexelsEndpoints
from yta_stock_downloader.pexels.dataclasses import PexelsImage, PexelsVideo, PexelsImagesPageResult, PexelsVideosPageResult
from yta_stock_downloader.pexels.enums import PexelsLocale, PexelsOrientation, PexelsSizeFilter
from yta_programming.output import Output
from yta_constants.file import FileType
from random import choice
from typing import Union

import requests


class _PexelsRawImagesApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the images in the raw Pexels API.
    """

    @staticmethod
    def get(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        page: int = 1
    ) -> dict:
        """
        Send a search request throw the Pexels
        images with the provided 'query' and get
        the ones matching that query.

        TODO: This is not handling pages.
        """
        locale = PexelsLocale.to_enum(locale).value
        orientation = PexelsOrientation.to_enum(orientation).value
        size = PexelsSizeFilter.to_enum(size).value

        response = requests.get(
            PexelsEndpoints.SEARCH_IMAGE_API_ENDPOINT_URL,
            {
                'query': query,
                'orientation': orientation,   # landscape | portrait | square
                'size': size,   # large | medium | small
                'locale': locale, # 'es-ES' | 'en-EN' ...
                'per_page': per_page,
                'page': page
            },
            headers = PexelsSettings.HEADERS
        )

        # The important information is in 'photos',
        # but this is a page of results
        return response.json()

class _PexelsRawVideosApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the videos in the raw Pexels API.
    """

    @staticmethod
    def get(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE
    ) -> dict:
        """
        Send a search request throw the pixabay
        videos with the provided 'query' and get
        the ones matching that query.

        TODO: This is not handling pages.
        """
        locale = PexelsLocale.to_enum(locale).value

        response = requests.get(
            url = PexelsEndpoints.SEARCH_VIDEOS_URL,
            params = {
                'query': query,
                'locale': locale,
                'orientation': orientation,   # landscape | portrait | square
                'size': size,   # large | medium | small
                'per_page': per_page
            },
            headers = PexelsSettings.HEADERS
        )

        # The important information is in 'videos',
        # but this is a page of results
        return response.json()

class PexelsRawApi:
    """
    Class to wrap the functionality related
    to the raw Pexels API with no data
    conversion, handling the information as
    it is returned by the official endpoints.

    You need a valid API KEY activated and
    set in the .env file to be able to obtain
    a valid response.
    """

    video: _PexelsRawVideosApi = _PexelsRawVideosApi
    """
    Shortcut to the endpoints related to videos.
    """
    image: _PexelsRawImagesApi = _PexelsRawImagesApi
    """
    Shortcut to the endpoints related to images.
    """

# TODO: The format is very similar so we
# could refactor and have a common class
# to be inherited by images and videos
class _PexelsImagesApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the images of our own Pexels API 
    that formats and wraps the raw API.
    """

    @staticmethod
    def get(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        # TODO: What about the page (?)
        ids_to_ignore: list[str] = []
    ) -> list[PexelsImage]:
        """
        Search videos for the given 'query' ignoring
        the ones with an id that is contained in the
        'ids_to_ignore' parameter provided. They will
        be returned in the order they were given but
        as PexelsImage instances.

        TODO: This is not handling pages.
        """
        response = PexelsRawApi.image.get(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page
        )

        # Turn into a page result object
        response_page = PexelsImagesPageResult(
            query = query,
            locale = locale,
            data = response
        )

        if response_page.total_results == 0:
            return []

        # Ignore images with ids to ignore
        images = [
            image
            for image in response_page.images
            if image.id not in ids_to_ignore
        ]

        # TODO: Think about an strategy to apply when 'images'
        # are not enough and we should make another request.
        # But by now we are just returning nothing, we don't 
        # want infinite requests loop or similar
        if len(images) == 0:
            # TODO: Make another request if possible (?)
            if response_page.page < response_page.total_pages:
                # TODO: Can we request a new page (?)
                pass
            pass

        return images
    
    def get_one(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        # TODO: What about the page (?)
        ids_to_ignore: list[str] = []
    ) -> Union[PexelsImage, None]:
        """
        Search for the images with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        the first one (if results available).
        """
        images = _PexelsImagesApi.get(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            images[0]
            if len(images) > 0 else
            None
        )
    
    def get_random(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        # TODO: What about the page (?)
        ids_to_ignore: list[str] = []
    ) -> Union[PexelsImage, None]:
        """
        Search for the images with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        a random one (if results available).
        """
        images = _PexelsImagesApi.get(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            choice(images)
            if len(images) > 0 else
            None
        )
    
    def download_one(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        # TODO: What about the page (?)
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
        image = _PexelsImagesApi.get_one(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            image.download(Output.get_filename(output_filename, FileType.IMAGE))
            if image is not None else
            None
        )
    
    def download_random(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        # TODO: What about the page (?)
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
        image = _PexelsImagesApi.get_random(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            image.download(Output.get_filename(output_filename, FileType.IMAGE))
            if image is not None else
            None
        )

class _PexelsVideosApi:
    """
    *For internal use only*

    Class to wrap the functionality related
    to the videos of our own Pexels API 
    that formats and wraps the raw API.
    """

    @staticmethod
    def get(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: str = PexelsOrientation.LANDSCAPE,
        size: str = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        ids_to_ignore: list[str] = []
    ) -> list[PexelsVideo]:
        """
        Search videos for the given 'query' ignoring
        the ones with an id that is contained in the
        'ids_to_ignore' parameter provided. They will
        be returned in the order they were given but
        as PexelsVideo instances.

        TODO: This is not handling pages.
        """
        response = PexelsRawApi.video.get(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page
        )

        # Turn into a page result object
        response_page = PexelsVideosPageResult(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            data = response
        )

        if response_page.total_results == 0:
            return []

        # Ignore videos with ids to ignore
        videos = [
            video
            for video in response_page.videos
            if video.id not in ids_to_ignore
        ]

        # TODO: Think about an strategy to apply when 'videos'
        # are not enough and we should make another request.
        # But by now we are just returning nothing, we don't 
        # want infinite requests loop or similar
        if len(videos) == 0:
            # TODO: Make another request if possible (?)
            if response_page.page < response_page.total_pages:
                # TODO: Can we request a new page (?)
                pass
            pass

        return videos
    
    def get_one(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        ids_to_ignore: list[str] = []
    ) -> Union[PexelsVideo, None]:
        """
        Search for the videos with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        the first one (if results available).
        """
        videos = _PexelsVideosApi.get(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            videos[0]
            if len(videos) > 0 else
            None
        )
    
    def get_random(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
        ids_to_ignore: list[str] = []
    ) -> Union[PexelsVideo, None]:
        """
        Search for the videos with the given 'query',
        ignoring the ones with an id that is included
        in the 'ids_to_ignore' parameter, and return
        a random one (if results available).
        """
        videos = _PexelsVideosApi.get(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            choice(videos)
            if len(videos) > 0 else
            None
        )
    
    def download_one(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
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
        video = _PexelsVideosApi.get_one(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            video.download(Output.get_filename(output_filename, FileType.VIDEO))
            if video is not None else
            None
        )
    
    def download_random(
        query: str,
        locale: PexelsLocale = PexelsLocale.ES_ES,
        orientation: PexelsOrientation = PexelsOrientation.LANDSCAPE,
        size: PexelsSizeFilter = PexelsSizeFilter.LARGE,
        per_page: int = PexelsSettings.RESULTS_PER_PAGE,
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
        video = _PexelsVideosApi.get_random(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            per_page = per_page,
            ids_to_ignore = ids_to_ignore
        )

        return (
            video.download(Output.get_filename(output_filename, FileType.VIDEO))
            if video is not None else
            None
        )

class PexelsApi:
    """
    Class to wrap the functionality related
    to our own Pexels API, which uses the
    raw Pexels API and formats and wraps
    the information to make easier reading
    and manipulating the data.
    """

    video: _PexelsVideosApi = _PexelsVideosApi
    """
    Shortcut to the endpoints related to videos.
    """
    image: _PexelsImagesApi = _PexelsImagesApi
    """
    Shortcut to the endpoints related to images.
    """