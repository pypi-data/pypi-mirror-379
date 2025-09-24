from pathlib import Path
import logging

class VirtualSerialDevice:
    def __init__(
            self, 
            port: str ='/tmp/vserial',
            callback = None):
        self.__port = Path(port)

        self._logger = logging.getLogger(__name__)

        raise NotImplementedError("NOT YET IMPLEMENTED ON WINDOWS")