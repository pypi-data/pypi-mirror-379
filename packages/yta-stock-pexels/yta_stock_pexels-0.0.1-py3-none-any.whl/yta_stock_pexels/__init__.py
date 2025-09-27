from yta_stock_pexels.enum import PexelsOrientation, PexelsSizeFilter, PexelsLocale
from yta_stock_pexels.settings import PexelsSettings
from yta_stock_pexels.api import PexelsApi
from yta_stock_pexels.dataclasses import PexelsImage, PexelsVideo
from yta_stock_common import _StockDownloader, _download_image, _download_video
from yta_validation.parameter import ParameterValidator
from typing import Union


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
    ) -> 'Pexels':
        """
        Reset the ids stored to be ignored and not
        repeated when downloading, for both images
        and videos.
        """
        self.images.reset()
        self.videos.reset()

        return self