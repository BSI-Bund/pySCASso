"""Module for crafting/building packets"""
from ast import literal_eval

import pytest
from pycrate_mobile.NAS import parse_NAS5G
from pyshark import FileCapture

from scas.logger import LOGGER


class Builder:
    """ Class to decode, modify and encode a packet
    """

    def nas_decoder(self, capture, frame_number=0):
        """ Function that decodes the NAS-5G Messages in a NGAP packet

        Attributes
        ----------
        capture : str
            Path to .pcap file
        frame_number : int, optional
            Number of packet that needs to be decoded (default is 0)

        Returns
        -------
        list
            A list of NAS Messages
        """

        messages = []

        packet = FileCapture(capture)[frame_number]
        nas_5gs_binary, err = parse_NAS5G(packet.ngap.nas_pdu.binary_value)

        if err:
            LOGGER.error("Parsing was unsuccessful. Error code: %s", err)
            pytest.exit()

        messages += [nas_5gs_binary]

        # For security protected messages
        if "NASMessage" in nas_5gs_binary.to_json():
            nas_5gs_binary, err = parse_NAS5G(
                nas_5gs_binary['NASMessage'].to_bytes())

            if err:
                LOGGER.error("Parsing was unsuccessful. Error code: %s", err)
                pytest.exit()

            messages += [nas_5gs_binary]

        return messages

    def ngap_builder(self, data, capture, frame_number=0):
        """ Function that builds a NGAP packet based on a previous NGAP packet

        Attributes
        ----------
        data : str
            NAS-5G message that should be replaced
        capture : str
            Path to .pcap file
        frame_number : int, optional
            Number of packet that needs to be decoded (default is 0)

        Returns
        -------
        str
            NGAP packet with NAS-5G messages edited
        """

        packet = FileCapture(capture)[frame_number]
        packet_raw_binary = FileCapture(capture, use_json=True,
                                        include_raw=True)[frame_number].get_raw_packet()

        no_nas = packet_raw_binary.split(packet.ngap.nas_pdu.binary_value)

        return data.join(no_nas)

    def ngap_modify_capture(self, _ies, capture, frame_number=0):
        """ Function that modifys a NAS message based in the NGAP packet

        Attributes
        ----------
        ies : [str]
            Dict with Parameters that should be edited
        capture : str
            Path to .pcap file
        frame_number : int, optional
            Number of packet that needs to be decoded (default is 0)

        Returns
        -------
        str
            NGAP packet with NAS-5G messages edited
        """

        _packet = FileCapture(capture)[frame_number]
        _messages = self.nas_decoder(capture, frame_number)

        # TODO ies need to be replaced in given packet

    def ngap_modify_type(self, ies, ie_type, capture, frame_number=0):
        """ Function that modifys a NAS message based on type but only the first occurrens

        Attributes
        ----------
        ies : [str]
            Dict with Parameters that should be edited
        type : str
            Messagetype that should be created
        capture : str
            Path to .pcap file
        frame_number : int, optional
            Number of packet that needs to be decoded (default is 0)

        Returns
        -------
        str
            NGAP packet with NAS-5G messages edited
        """
        # Cleans the type since a function cannot start with an interger
        raw_ie_type = ie_type
        if ie_type[0] == '5':
            ie_type = 'F' + ie_type[1:]
        elif ie_type[0].isdigit():
            LOGGER.error("Cannot clean type!")
            pytest.exit()

        messages = self.nas_decoder(capture, frame_number)

        path_ie = self.find_ie(messages, ie_type, raw_ie_type, [])

        # Modifies the message based on the path and the IEs
        if path_ie is not None:
            literal_eval("messages" + str(path_ie)[1:-1].replace(", ", "")).set_val(ies)
        else:
            LOGGER.error("Couldn't find IE")
            pytest.exit()

        # If the message is protected the protected part need to be changed in the header
        if len(messages) == 1:
            return self.ngap_builder(messages[0].to_bytes(), capture, frame_number)

        messages[0]['NASMessage'].set_val(messages[1].to_bytes())
        return self.ngap_builder(messages[0].to_bytes(), capture, frame_number)

    def ngap_replay(self, capture, frame_number=0):
        """ Function to extract a NGAP packet out of a frame

        Attributes
        ----------
        capture : str
            Path to .pcap file
        frame_number : int, optional
            Number of packet that needs to be decoded (default is 0)

        Returns
        -------
        str
            NGAP packet from the frame
        """

        packet = FileCapture(capture)[frame_number]
        return packet.ngap.nas_pdu.binary_value

    # Ugly recursive solution to finding the IE
    def find_ie(self, message, ie_type, raw_ie_type, path):
        """ Function to extract the path to a given type

        Attributes
        ----------
        message : [pycrate_objects]
            Message in which the type should be found
        ie_type : str
            Clean name of the searched message type
        raw_ie_type : str
            Name of the searched message type
        path : [[int]]
            Path of the type in the message

        Returns
        -------
        [[int]]
            Path of the type in the message
        """
        if isinstance(type(message), list):
            length = len(message)
        else:
            length = message.get_len()

        for i in range(0, length):
            # Found the IE
            if ie_type in str(type(message[i])) or message[i].show().startswith('<' + raw_ie_type):
                path += [[i]]
                return path
            if raw_ie_type in message[i].show():
                path += [[i]]
                return self.find_ie(message[i], ie_type, raw_ie_type, path)

        # Didn't find IE
        LOGGER.error("Could not find the IE!")
        raise RuntimeError
