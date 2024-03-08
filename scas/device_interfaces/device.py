"""Module containing the generic device implementation"""
from abc import ABC, abstractmethod
from enum import Enum, auto
from os import path

import pytest

import scas
from scas.device_interfaces.device_config import DeviceConfig
from scas.capture.capture import Capture, CaptureTarget


class ActionKey(Enum):
    """Enum representing several actions/events that could be part of a test case
    and that could be executed by a device"""
    EXEC_IN_CONTEXT = auto()
    SYNC_FAILURE = auto()
    REPLAY_PACKET = auto()
    NRF_REGISTRATION = auto()
    NRF_DISCOVERY = auto()


class Device(ABC):
    """
    Abstract base class for devices.
    Typical lifecycle of a device while runniung a test function:
     1. setup()
     2. start()
     3. stop()
     4. teardown()

    Attributes:
        proc        This is a handle to a process. Usually a device
                    should be some sort of external program that is
                    executed by the start() method and killed by the
                    stop() method. To keep track of the program the
                    proc handle should be used.

        paths       This is a dict of file system paths the device
                    depends on, together with a descriptive key
                    (e.g. installation files and dirs).
    """

    def __init__(self):
        self.pid = None
        self.paths = {}
        self.config = None
        if self.is_available() is False:
            pytest.skip(f"{self.name()} not available. Check local installation paths in "
                        f"tests/test_config.yaml.")

    def name(self) -> str:
        """return the class name as string"""
        return self.__class__.__name__

    def paths_exist(self) -> bool:
        """checkes if the given pathes exist"""
        for _, value in self.paths.items():
            if not path.exists(value):
                scas.LOGGER.error("%s: Path %s does not exist. (config: %s)",
                                  self.name(), value, pytest.test_config_file)
                pytest.exit("Device path does not exist.")
        return True

    def get_config(self) -> DeviceConfig:
        """returns the config for this device"""
        if self.config is None:
            scas.LOGGER.warning("%s: Tried to get uninitialized config.", self.name())
            pytest.fail("Tried to get uninitialized config.")
        return self.config

    @abstractmethod
    def is_available(self) -> bool:
        """useful to check if device is available"""
        raise NotImplementedError

    @abstractmethod
    def setup(self):
        """useful to do setup before using device"""
        raise NotImplementedError

    @abstractmethod
    def start(self):
        """start the device"""
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        """stop the device"""
        raise NotImplementedError

    @abstractmethod
    def teardown(self):
        """cleanup after device was stopped"""
        raise NotImplementedError

    @abstractmethod
    def perform(self, action: ActionKey):
        """device performing a defined action"""
        raise NotImplementedError

    @abstractmethod
    def create_capture(self, target: CaptureTarget = CaptureTarget.GENERIC) -> Capture:
        """creates and returns a device specific capture target"""
        raise NotImplementedError
