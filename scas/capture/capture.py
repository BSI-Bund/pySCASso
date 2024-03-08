"""Module holding the capture object definition."""
from abc import ABC, abstractmethod
from enum import Enum, auto

import pytest
from pyshark import FileCapture

from scas.packet_type.common import PacketType


class Capture(ABC):
    """Abstract Capture Class

    Args:
        ABC (_type_): Helper class that provides a standard way to create an ABC using inheritance
    """
    def __init__(self):
        self._dummy_file = None
        self._capture_file = None
        self._include_raw = False

    def set_capture_file(self, capture_file):
        """Sets the capture file

        Args:
            capture_file (_type_): string with the capture file path

        Returns:
            Capture: returns self for method chaining syntax
        """
        self._capture_file = capture_file
        return self

    def set_dummy_file(self, dummy_file):
        """Sets the dummy capture file for dummy test cases (offline, prerecorded etc)

        Args:
            dummy_file (_type_): string with path to dummy capture file

        Returns:
            Capture: returns self for method chaining syntax
        """
        self._dummy_file = dummy_file
        return self

    def set_include_raw(self, include_raw):
        """Should the capture object include raw data bytes or just the object.

        Args:
            include_raw (boolean): true or false

        Returns:
            Capture: returns self for method chaining syntax
        """
        self._include_raw = include_raw
        return self

    def get_current_file(self):
        """
            returns the currently "active" file of the capture object
            this basically switches between a "real" capture file and a dummy file
        """
        if pytest.dummy_capture:
            return self._dummy_file
        return self._capture_file

    def name(self) -> str:
        """returns the capture objects class name for better logging

        Returns:
            str: name of the capture class instance
        """
        return self.__class__.__name__

    def extract_pcap_by_packet_type(self, packet: PacketType,
                                    extracted_pcap_name_and_path=None) -> str:
        """This method strips a specified packet type from an existing capture file/pcap
        and saves a new pcap containing this specific packet.

        Args:
            packet (PacketType): the specific packet type to extract
            extracted_pcap_name_and_path (_type_, optional): Optional name of the new pcap.
                Defaults to None.

        Returns:
            str: the path to the extracted pcap
        """
        new_pcap = extracted_pcap_name_and_path if extracted_pcap_name_and_path else \
            f"/tmp/{packet.__class__.__name__}.pcap"
        disp_filter = f"frame.number=={packet.frame_number()}"
        new_cap = FileCapture(
            self.get_current_file(), display_filter=disp_filter, output_file=new_pcap)
        new_cap.load_packets()
        return new_pcap  # returns path to new pcap

    @abstractmethod
    def record_event(self, event=None, timeout_sec=None, continue_after_event_sec=None):
        """Abtract method for recording events with a capture object

        Args:
            event (lamda/functional expression, optional): this must be a blocking piece of code
                that contains the event you want to record. Defaults to None.
            timeout_sec (integer, optional): Event timeout in seconds. The blocking event can
                timeout if you wish. Defaults to None.
            continue_after_event_sec (integer, optional): If you want to wait some seconds after
                the event has been executed (e.g. capture some reaction to this event) you can
                use this variable. Defaults to None.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError


class CaptureTarget(Enum):
    """Enum for defining capture targets. The generic target is the local machine.
    If there are other (e.g. remote machine) devices to capture from, there should
    be a specific implementation and new CaptureTarget case.
    See NRF target for reference
    """
    GENERIC = auto()
    NRF = auto()
