from yta_stock_pexels.enum import PexelsLocale, PexelsImageSize, PexelsOrientation, PexelsSizeFilter
from yta_file_downloader import Downloader
from yta_programming.output import Output
from yta_constants.file import FileType
from typing import Union
from dataclasses import dataclass


@dataclass
class PexelsImageSource:
    """
    Class to wrap a source of a Pexels image.
    """

    @property
    def as_json(
        self
    ) -> dict:
        """
        The instance as a json dict for debugging.
        """
        return {
            'quality': self.quality,
            'download_url': self.download_url
        }

    def __init__(
        self,
        quality: str,
        download_url: str
    ):
        self.quality: str = quality
        """
        The quality of the image source.
        """
        self.download_url: str = download_url
        """
        The url to download that image file.
        """

@dataclass
class PexelsImage:
    """
    Class to represent a Pexels image and to
    simplify the way we work with its data.
    """

    @property
    def id(
        self
    ) -> int:
        """
        Unique identifier of this image in Pexels
        platform. Useful to avoid using it again
        in the same project.
        """
        return self._data['id']
    
    @property
    def size(
        self
    ) -> tuple[int, int]:
        """
        The size of the image expressed as (width,
        height).
        """
        return (self._data['width'], self._data['height'])
    
    @property
    def display_url(
        self
    ) -> str:
        """
        The url in which the image is displayed but
        not to download it.
        """
        return self._data['url']
    
    @property
    def author(
        self
    ) -> dict:
        """
        The author of the image, including 'id',
        'name' and 'url'.
        """
        return {
            'id': self._data['photographer_id'],
            'name': self._data['photographer'],
            'url': self._data['photographer_url']
        }
    
    @property
    def average_color(
        self
    ) -> str:
        """
        The average color, provided by the Pexels
        platform, in hexadecimal format like
        `#9D9485`.
        """
        return self._data['avg_color']
    
    @property
    def alt(
        self
    ) -> str:
        """
        Alternative text that describes the image,
        used when the image cannot be displayed but
        also useful to understand what is shown in
        the scene.
        """
        return self._data['alt']
    
    @property
    def sources(
        self
    ) -> list[PexelsImageSource]:
        """
        The image file sources ordered from the
        lowest quality to the biggest one.
        """
        if not hasattr(self, '_sources'):
            sources = [
                PexelsImageSource(
                    quality = quality,
                    download_url = download_url
                )
                for quality, download_url in self._data['src'].items()
            ]

            # We want the orientations at the end
            qualities = PexelsImageSize.get_all_values() + PexelsOrientation.get_all_values()

            # Map 'id' -> position
            pos = {
                quality: i
                for i, quality in enumerate(qualities)
            }

            # Order with that position
            self._sources = sorted(
                sources,
                key = lambda source: pos.get(source.quality, float('inf')),
                # We want it from lower quality to the best one
                reverse = True
            )

        return self._sources
    
    @property
    def best_image(
        self
    ) -> PexelsImageSource:
        """
        The best image as a dict including the quality
        as the key and the url to download it as the
        value.
        """
        return self.sources[-1]
    
    @property
    def download_url(
        self
    ) -> str:
        """
        The download url of the option highest quality
        option available. This download url is found in
        the 'src' attribute by searching in desc. order.
        """
        return self.best_image.download_url
    
    @property
    def as_json(
        self
    ):
        """
        Return the object instance as a json to be
        displayed and debugged.
        """
        return {
            'id': self.id,
            'size': self.size,
            'display_url': self.display_url,
            'download_url': self.download_url,
            'author': self.author,
            'average_color': self.average_color,
            'alt': self.alt,
            'sources': [
                source.as_json
                for source in self.sources
            ],
            'best_image': self.best_image.as_json
        }

    def __init__(
        self,
        data: dict
    ):
        self._data: dict = data
        """
        The raw data as it was provided in the
        response.
        """

    def get_download_url(
        self,
        quality: Union[PexelsImageSize, PexelsOrientation, None] = None
    ) -> Union[str, None]:
        """
        Get the download url for the quality provided.
        If 'quality' is None, the best quality will be
        provided.
        """
        if quality is not None:
            try:
                quality = PexelsImageSize.to_enum(quality).value
            except:
                try:
                    quality = PexelsOrientation.to_enum(quality).value
                except:
                    raise Exception('The "quality" provided is not a valid value.')
                
        return (
            self.download_url
            if quality is None else
            getattr(self._data['src'], quality, None) 
        )

    def download(
        self,
        output_filename: Union[str, None] = None
    ) -> 'FileReturned':
        """
        Download this image to the provided local
        'output_filename'. If no 'output_filename'
        is provided, it will be stored locally with
        a temporary name.

        This method returns the final downloaded
        image filename.
        """
        return Downloader.download_image(
            self.download_url,
            Output.get_filename(output_filename, FileType.IMAGE)
        )
    
@dataclass
class _PexelsVideoSource:
    """
    Class to represent one source of a video from
    the Pexels platform, that has specific fps
    and quality.

    A video is uploaded to the platform and has
    different resolutions and file sizes. This
    class represent each of those resolutions.

    This class is to instantiate each of the
    results contained in the 'video_files' field.
    """

    @property
    def id(
        self
    ) -> int:
        """
        The unique identifier of this video source
        in the Pexels platform.
        """
        return self._data['id']
    
    # TODO: Is this, as a str, interesting (?)
    @property
    def quality(
        self
    ) -> str:
        """
        The quality of the video.
        """
        return self._data['quality']
    
    @property
    def file_extension(
        self
    ) -> str:
        """
        The file extension of the video.
        """
        return self._data['file_type'].split('/')[-1]
    
    @property
    def size(
        self
    ) -> tuple[int, int]:
        """
        The size of this video source, represent as
        (width, height).
        """
        return (self._data['width'], self._data['height'])
        
    @property
    def fps(
        self
    ) -> float:
        """
        The frames per second (fps) of this video
        source.
        """
        return self._data['fps']
    
    @property
    def download_url(
        self
    ) -> str:
        """
        The url from which you can download the video
        source.
        """
        return self._data['link']
    
    @property
    def file_size(
        self
    ) -> int:
        """
        The size of the video file (in bytes?).
        """
        return self._data['size']
    
    @property
    def as_json(
        self
    ) -> dict:
        """
        The instance but as a json dict for debugging.
        """
        return {
            'id': self.id,
            'quality': self.quality,
            'file_extension': self.file_extension,
            'size': self.size,
            'fps': self.fps,
            'download_url': self.download_url,
            'file_size': self.file_size
        }

    def __init__(
        self,
        data: dict
    ):
        self._data: dict = data
        """
        The raw data of the source that has been
        provided in the response.
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
class _PexelsVideoPicture:
    """
    Class to represent a picture of a video
    requested on the Pexels platform.
    """

    @property
    def id(
        self
    ) -> int:
        """
        The unique identifier of the video picture
        in the Pexels platform.
        """
        return self._data['id']
    
    @property
    def download_url(
        self
    ) -> str:
        """
        The url from which you can download the picture.
        """
        return self._data['picture']
    
    @property
    def index(
        self
    ) -> int:
        """
        The index of the picture, that is the position
        of the picture, respect to the other pictures,
        in the video. A lower value means being taken
        near the begining of the video.
        """
        return self._data['nr']
    
    @property
    def as_json(
        self
    ) -> dict:
        """
        The instance but as a json dict for debugging.
        """
        return {
            'id': self.id,
            'download_url': self.download_url,
            'index': self.index
        }

    def __init__(
        self,
        data: dict
    ):
        self._data = data
        """
        The raw data obtained in the request.
        """
        
@dataclass
class PexelsVideo:
    """
    Class to represent a video of the Pexels platform and
    to handle it easier than as raw data. A video has the
    main information but also different video files, or
    video formats, that can be used for different purposes.
    Maybe we want a landscape video or maybe a portrait,
    so both of them could be available as 'video_files'
    for the same video content.
    """

    @property
    def id(
        self
    ) -> int:
        """
        Unique identifier of this video in Pexels
        platform. Useful to avoid using it again
        in the same project.
        """
        return self._data['id']
    
    @property
    def display_url(
        self
    ) -> str:
        """
        The url in which the video is displayed but
        not to download it.
        """
        return self._data['url']
    
    @property
    def size(
        self
    ) -> tuple[int, int]:
        """
        The size of the video expressed as (width,
        height).
        """
        return (self._data['width'], self._data['height'])
    
    @property
    def duration(
        self
    ) -> int:
        """
        The duration of the video, rounded up I think,
        provided by the platform.
        """
        return self._data['duration']
    
    @property
    def thumbnail_url(
        self
    ) -> str:
        """
        The url to obtain the thumbnail of the video.
        """
        return self._data['image']
    
    @property
    def tags(
        self
    ) -> list[str]:
        """
        The tags of the image.
        """
        return self._data['tags']
    
    @property
    def author(
        self
    ) -> dict:
        """
        The author of the video, including the
        'id', 'name' and 'url'.
        """
        return {
            'id': self._data['user']['id'],
            'name': self._data['user']['name'],
            'url': self._data['user']['url'],
        }
    
    @property
    def sources(
        self
    ) -> list[_PexelsVideoSource]:
        """
        The different video sources (video files) of
        this video, as our own instances, ordered from
        smaller width to bigger width.
        """
        if not hasattr(self, '_sources'):
            self._sources = sorted(
                [
                    _PexelsVideoSource(video_file_data)
                    for video_file_data in self._data['video_files']
                ],
                key = lambda video_file_data: video_file_data.size[0],
            )
            
        return self._sources
    
    @property
    def pictures(
        self
    ) -> list[_PexelsVideoPicture]:
        """
        The pictures of the video as our own custom
        instances, ordered from the begining to the
        end.
        """
        if not hasattr(self, '_pictures'):
            self._pictures = sorted(
                [
                    _PexelsVideoPicture(video_picture_data)
                    for video_picture_data in self._data['video_pictures']
                ],
                key = lambda video_picture_data: video_picture_data.index
            )
            
        return self._pictures

    @property
    def best_video(
        self
    ) -> _PexelsVideoSource:
        """
        The video source with the best quality (the max
        width) which is available on the platform.
        """
        return self.sources[-1]
    
    @property
    def as_json(
        self
    ) -> dict:
        """
        The information as a json dict.
        """
        return {
            'id': self.id,
            'display_url': self.display_url,
            'size': self.size,
            'duration': self.duration,
            'thumbnail_url': self.thumbnail_url,
            'tags': self.tags,
            'author': self.author,
            'sources': [
                source.as_json
                for source in self.sources
            ],
            'pictures': [
                picture.as_json
                for picture in self.pictures
            ]
        }

    def __init__(
        self,
        data: any
    ):
        self._data: dict = data
        """
        The raw data as received in the response.
        """

    # TODO: This is downloading the best quality
    # by now, but we need to implement other
    # options
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

from abc import ABC
@dataclass
class _PexelsPageResult(ABC):
    """
    Dataclass to be inherited by the other
    dataclasses that include information about
    a page of results obtained from the Pexels
    API.
    """

    @property
    def total_pages(
        self
    ):
        """
        The total amount of pages according to the
        search, items per page and pages found. This
        is a value we calculate to know how many 
        pages we can use in the search to be able to
        jump to a specific page.
        """
        total = int(self.total_results / self.per_page)

        return (
            total + 1
            if self.total_results % self.per_page > 0 else
            total
        )

    @property
    def as_json(
        self
    ):
        """
        Return the object instance as a json to be
        displayed and debugged.
        """
        # TODO: Review this due to new changes
        return {
            'query': self.query,
            'locale': self.locale,
            'orientation': self.orientation,
            'size': self.size,
            'page': self.page,
            'per_page': self.per_page,
            'total_results': self.total_results,
            'total_pages': self.total_pages,
            'next_page_api_url': self.next_page_api_url,
        }
    
    def __init__(
        self,
        query: str,
        locale: PexelsLocale,
        orientation: PexelsOrientation,
        size: PexelsSizeFilter,
        data: dict
    ):
        self.query: str = query
        """
        The query used in the request.
        """
        self.locale: PexelsLocale = locale
        """
        The locale used in the request.
        """
        self.orientation: PexelsOrientation = orientation
        """
        The orientation used in the request.
        """
        self.size: PexelsSizeFilter = size
        """
        The size filter used in the request.
        """
        self.page: int = data['page']
        """
        The current page of Pexels video results.
        """
        self.per_page: int = data['per_page']
        """
        The amount of videos that are being obtained
        per page for the request.
        """
        self.total_results: int = data['total_results']
        """
        The amount of results obtained with the request,
        that is the sum of all existing results 
        considering not pagination nor current page.
        """
        self.next_page_api_url: str = data['next_page']
        """
        The API url to make a request to obtain the next
        results page.

        TODO: How do you actually use this url (?)
        """
        self.raw_json: dict = data
        """
        The whole raw json data provided by Pexels. This
        is for debugging purposes only.
        """

@dataclass
class PexelsImagesPageResult(_PexelsPageResult):
    """
    A page of results obtained when requesting
    images to the Pexels API.
    """

    @property
    def images(
        self
    ) -> list[PexelsImage]:
        """
        The images but as PexelsImage instances.
        """
        return [
            PexelsImage(image)
            for image in self.images_raw
        ]

    def __init__(
        self,
        query: str,
        locale: PexelsLocale,
        orientation: PexelsOrientation,
        size: PexelsSizeFilter,
        data: dict
    ):
        super().__init__(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            data = data
        )

        self.images_raw: list[dict] = [
            image
            for image in data['photos']
        ]
        """
        The array containing all the images found in the
        current page according to the query.
        """

@dataclass
class PexelsVideosPageResult(_PexelsPageResult):
    """
    A page of results obtained when requesting
    videos to the Pexels API.
    """

    @property
    def videos(
        self
    ) -> list[PexelsVideo]:
        """
        The videos but as PexelsVideo instances.
        """
        return [
            PexelsVideo(video)
            for video in self.videos_raw
        ]

    def __init__(
        self,
        query: str,
        locale: PexelsLocale,
        orientation: PexelsOrientation,
        size: PexelsSizeFilter,
        data: dict
    ):
        super().__init__(
            query = query,
            locale = locale,
            orientation = orientation,
            size = size,
            data = data
        )

        self.videos_raw: list[dict] = [
            video
            for video in data['videos']
        ]
        """
        The array containing all the videos found in the
        current page according to the query.
        """