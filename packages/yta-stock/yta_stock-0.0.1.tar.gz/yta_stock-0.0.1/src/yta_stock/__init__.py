from yta_stock_pexels import Pexels
from yta_stock_pexels.enum import PexelsSizeFilter, PexelsOrientation, PexelsLocale
from yta_stock_pixabay import Pixabay
from yta_programming.output import Output
from yta_constants.file import FileType
from typing import Union
from typing import Union


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