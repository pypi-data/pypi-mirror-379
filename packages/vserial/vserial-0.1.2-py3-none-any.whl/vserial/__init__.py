import sys

if sys.platform.startswith('linux'):
    from vserial.vserial_posix import VirtualSerialDevice

elif sys.platform.startswith("win"):
    from vserial.vserial_win import VirtualSerialDevice
            

