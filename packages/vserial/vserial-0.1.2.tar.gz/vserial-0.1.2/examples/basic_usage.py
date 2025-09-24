from pathlib import Path

import vserial


class MockHelm:
    def __init__(self, name='mock', directory=Path('/tmp')):
        self.name = name
        self.port = directory / name

        self.vsd = vserial.VirtualSerialDevice(
            port = self.port,
            callback=self._read
        )

    def _read(self, data):
        print(data)

    def start(self):
        self.vsd.open()

    def close(self):
        self.vsd.close()

