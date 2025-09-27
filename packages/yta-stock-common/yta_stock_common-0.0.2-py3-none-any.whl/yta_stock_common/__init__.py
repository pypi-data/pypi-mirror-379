from yta_programming.output import Output
from yta_constants.file import FileType
from abc import ABC, abstractmethod
from typing import Union


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

def _download_image(
    self: Union['_PixabayImageDownloader', '_PexelsImageDownloader'],
    image: Union['PixabayImage', 'PexelsImage'],
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
    self: Union['_PixabayVideoDownloader', '_PexelsImageDownloader'],
    video: Union['PixabayVideo', 'PexelsVideo'],
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