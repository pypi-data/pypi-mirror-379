import json
import logging
import pathlib
import tempfile
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal, Optional

import soundfile

if TYPE_CHECKING:
    import os

    from .interface import Interface
    from .typing import ABuffer

logger = logging.getLogger(__name__)


class AFile(soundfile.SoundFile):  # type: ignore[misc]
    def __init__(self,
                 interface: "Interface",
                 mode: Literal["r", "w", "w+"] = "r",
                 path: Optional["str|os.PathLike[str]"] = None,
                 channels: Optional[int] = None,
                 temp: bool = False,
                 subtype: Optional[str] = None,
                 format: Optional[str] = None) -> None:
        """The AFile class handles sound files. Metadata is used to store and load additional settings.
        It is recommended to open AFile's in a `with` context manager.
        To determine the correct subtype and format,
        have a look at the [soundfile documentation](https://python-soundfile.readthedocs.io).

        Args:
            interface: Reference to an Interface instance.
            mode: The mode to open the file with..
            path: The filepath.
            channels: Number of channels.
            temp: When true, the file is temporary and deleted on close, otherwise the file is persistent.
            subtype: The subtype of the sound file. The value is read from the file or depends on the format.
                Defaults to "WAV" for write modes.
            format: The major format of the sound file. Usually read from from the file or determined by the extension.
                Defaults to "FLOAT" for write modes.

        Raises:
            ValueError: For incorrect input arguments
            FileNotFoundError: When the path does not exist.

        Example: Find shape of an audio file
            ```python
            import asmu
            with asmu.AFile(interface, mode = "r", path="myfile.wav") as afile:
                print(afile.data.shape)
            ```
        """
        # Check input
        if mode not in ["r", "w", "w+"]:
            raise ValueError("Specify a valid mode of [\"r\", \"w\", \"w+\"].")
        if path is None and temp is False:
            raise ValueError("For non-temporary files, a path has to be specified")
        if mode != "r" and channels is None:
            raise ValueError("Either read (mode = \"r\") a file or specify channels.")

        if mode != "r" and (subtype is None and format is None):
            # default, because readable by most systems but also accurate
            self._format: Optional[str] = "WAV"
            self._subtype: Optional[str] = "FLOAT"
        else:
            self._format = format
            self._subtype = subtype  # if None us default_subtype(format)

        self._interface = interface
        self._mode = mode
        if path is not None:
            self.path = pathlib.Path(path)
        else:
            self.path = path

        self._channels = channels
        self._temp = temp

        self._settings: dict[str, Any] = {}

    @property
    def path(self) -> Optional[pathlib.Path]:
        return self._path

    @path.setter
    def path(self, value: Optional[pathlib.Path]) -> None:
        self._path = value
        if value is not None:
            if not value.exists() and self._mode == "r":
                raise FileNotFoundError(f"File {value} does not exist.")
            if value.exists():
                logger.debug(f"File {value} exists.")

    # store settings as json string in metadata "comment"
    @property
    def settings(self) -> dict[str, Any]:
        """Additional JSON settings in the metadata's comment field."""
        return self._settings

    @settings.setter
    def settings(self, value: dict[str, Any]) -> None:
        self._settings = value
        self.comment = json.dumps(self.settings)

    @property
    def data(self) -> "ABuffer":
        """This property can be used to access the data of the AFile.
        Dont use it during an active audio stream, as it resets the file pointer to the
        start of the file.

        Returns:
            Data of AFile as numpy array of shape (Samples x Channels).
        """
        self.flush()
        self.seek(0)
        return self.read(dtype="float32", always_2d=True)   # type: ignore[no-any-return]

    def __enter__(self) -> "soundfile.SoundFile":
        return self.open()

    def __exit__(self, *args) -> None:  # type: ignore[no-untyped-def]
        self.close()

    def open(self) -> "AFile":
        """Open a file, with respect to the settings specified at initialization.

        Returns:
            An instance of th opened AFile.
        """
        if self._mode == "r":
            super().__init__(self._path, mode=self._mode)
            # load settings
            if self.comment:
                self._settings = json.loads(self.comment)
        else:
            if self._temp:
                if self._path is None:
                    tmp = tempfile.NamedTemporaryFile(suffix=f".{self._format}", delete=True)
                else:
                    tmp = tempfile.NamedTemporaryFile(prefix=self._path.stem, suffix=self._path.suffix,
                                                      dir=self._path.parent, delete=True)
                super().__init__(tmp,
                                 mode=self._mode,
                                 samplerate=self._interface.samplerate,
                                 channels=self._channels,
                                 subtype=self._subtype,
                                 format=self._format)
            else:
                super().__init__(self._path,
                                 mode=self._mode,
                                 samplerate=self._interface.samplerate,
                                 channels=self._channels,
                                 subtype=self._subtype,
                                 format=self._format)
                assert (self._path is not None)
                self.title = self._path.stem
            now = datetime.now()
            # set wav metadata
            self.date = now.strftime("%Y-%m-%dT%H:%M:%S%z")  # ISO 8601
        return self
