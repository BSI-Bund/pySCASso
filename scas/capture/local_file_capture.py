"""Module for loading a localy available capture file (pcap) and analysing it"""
import hashlib
import os
import shutil

import pytest
from pyshark import FileCapture

from scas.capture.capture import Capture
from scas.logger import LOGGER
from scas.packet_type.common import PacketType


def get_md5sum(file) -> str:
    """helper function returning md5 hash of a given file

    Args:
        file (str): filepath/name to be md5 digested

    Returns:
        str: md5 hash of file
    """
    if not os.path.exists(file):
        return ""
    with open(file, "rb") as file_handle:
        digest = hashlib.file_digest(file_handle, "md5")
    return digest.hexdigest()


def process_packets_cb(packet: PacketType, target_packet: PacketType):
    """callback method that filters a packet based on some defined condition

    Args:
        packet (PacketType): the checked packet
        target_packet (PacketType): packet type defining the condition

    Returns:
        boolean: true if condition was met, false otherwise
    """
    # LOGGER.debug(f"#{str(packet.number)}: {packet.layers}")
    if target_packet:
        if target_packet.matches(packet):
            # TODO process further packet conditions, if they are not in the target_packet
            return True
    return False


class LocalFileCapture(Capture):
    """Capture implementation for local files. This actualy does no capturing, but loads a locally
    available capture file (pcap) for analysis.
    """
    def set_capture_file(self, capture_file):
        """define the capture file to load

        Args:
            capture_file (str): filename/path of capture file to load

        Returns:
            LocalFileCapture: returns self for method chaining syntax
        """
        super().set_capture_file(capture_file)

        # or copy that file to reports
        if pytest.create_report:
            pcap_name = f"{pytest.report_path}/{pytest.current_test_name}_00.pcap"
            old_name = pcap_name
            i = 1
            while os.path.exists(pcap_name):
                pcap_name = pcap_name.replace(
                    f"{i-1:02d}.pcap", f"{i:02d}.pcap")
                i += 1

            # check, if the file was already copied
            if get_md5sum(old_name) != get_md5sum(self.get_current_file()):
                shutil.copy(self.get_current_file(), pcap_name)

        return self

    def record_event(self, event=None, timeout_sec=None, continue_after_event_sec=None):
        """this is not used in this instance"""
        # we dont record events here - we just open an existing pcap
        return self

    def get_packet_count(self):
        """Returns the packet count of the current prerecorded capture file."""
        cap = FileCapture(self.get_current_file())
        cap.load_packets()
        return len(cap)

    def get_first_packet_of_type(self, target_packet: PacketType):
        """Returns the first packet of a given type from the current prerecorded capture file."""
        packets = self.get_packets_of_type(target_packet)
        if packets:
            return packets[0]
        return False

    def get_packets_of_type(self, target_packet: PacketType):
        """Returns a packet list of a given type from the current prerecorded capture file."""
        if self.get_current_file() is None:
            return []

        display_filter = target_packet.get_filter_string()

        matched_packets = self._open_capture(process_packets_cb,
                                             displ_filter=display_filter,
                                             target_packet=target_packet,
                                             prefs=target_packet.prefs)

        if len(matched_packets) > 0:
            # p.packet_raw is eithe None or has a valid raw packet
            return [target_packet.create(p, p.packet_raw) for p in matched_packets]
        return False

    def _open_capture(self, packet_callback, target_packet, displ_filter=None, prefs=None):
        """Loads a capture file

        Args:
            packet_callback (Condition): Self defined condition to be checked for when loading the
                capture file
            displ_filter (string, optional): Condition to be checked for when loading the capture
                file based in wireshark display filters. Defaults to None.
            prefs (_type_, optional): Wireshark preferences to be applied when opening the file;
                e.g. NAS Null ciphering decryption. Defaults to None.

        Returns:
            _type_: _description_
        """
        pcap = self.get_current_file()

        if not os.path.exists(pcap):
            LOGGER.warning("Could not open %s. Skipping this test...", pcap)
            pytest.skip(f"Could not open {pcap}.")

        cap = FileCapture(pcap, display_filter=displ_filter, override_prefs=prefs)

        try:
            cap.load_packets()
        except TimeoutError as ex:
            LOGGER.warning("Error loading %s: %s", pcap, ex)
            return []

        cap_raw = None
        if self._include_raw:
            cap_raw = FileCapture(pcap, use_json=True, include_raw=True,
                                  display_filter=displ_filter, override_prefs=prefs)
            cap_raw.load_packets()

        LOGGER.info("%s (%s packets filtered with [%s])", pcap, len(cap), displ_filter)

        matched_packets = []
        for num, pkt in enumerate(cap):

            # for convenience we add this member to the existing class object
            pkt.packet_raw = None

            if packet_callback(pkt, target_packet):
                if self._include_raw:
                    if num < len(cap_raw) and pkt.frame_info.time == cap_raw[num].frame_info.time:
                        pkt.packet_raw = cap_raw[num]
                matched_packets.append(pkt)
                # break TODO: do we always assume that there is only one matching packet?
        return matched_packets
