"""Module providing http header definitions with wireshark dissectors"""
import json

from scas.packet_type.common import DisplayFilter, PacketType


class HTTP2Packet(PacketType):
    """Class representing basic http2 packet with wireshark dissecor
    """
    layer_name = "http2"
    layer_nr = PacketType.layer_nrs[layer_name]
    # TODO: the port 7777 is open5gs specific: find a generic/configurable ways to pass
    # http/http2 port here
    prefs = {"http2.tcp.port": "7777, 8000"}

    def streamid(self):
        """Returns the streamid for keeping track of http2 streams

        Returns:
            integer: the stream id
        """
        return int(self.packet.http2.get_field("streamid"))


class HTTP2Header(HTTP2Packet):
    """Class representing basic http2 header with wireshark dissecor
    """
    def __init__(self, packet=None, packet_raw=None, additional_filters=None):
        super().__init__(packet, packet_raw)
        self.packet_filter = [DisplayFilter("http2.type", "==", "1")]
        if additional_filters:
            self.packet_filter.extend(additional_filters)

    def status(self):
        """Returns the status value of a header (200, 404, 502 etc)

        Returns:
            integer: http status code
        """
        return int(self.packet.http2.get_field("headers.status"))


class HTTP2HeaderPost(HTTP2Header):
    """Class representing http2 post header with wireshark dissecor
    """
    def __init__(self, packet=None, packet_raw=None, additional_filters=None):
        super().__init__(packet, packet_raw)
        self.packet_filter = [DisplayFilter(
            "http2.headers.method", "==", "POST")]
        if additional_filters:
            self.packet_filter.extend(additional_filters)


class HTTP2HeaderGet(HTTP2Header):
    """Class representing http2 get header with wireshark dissecor
    """
    def __init__(self, packet=None, packet_raw=None, additional_filters=None):
        super().__init__(packet, packet_raw)
        self.packet_filter = [DisplayFilter(
            "http2.headers.method", "==", "GET")]
        if additional_filters:
            self.packet_filter.extend(additional_filters)


class HTTP2HeaderCreated(HTTP2Header):
    """Class representing http2 created header with wireshark dissecor
    """
    def __init__(self, packet=None, packet_raw=None, additional_filters=None):
        super().__init__(packet, packet_raw)
        self.packet_filter = [DisplayFilter("http2.header.value", "==", "201")]
        if additional_filters:
            self.packet_filter.extend(additional_filters)


class HTTP2HeaderPut(HTTP2Header):
    """Class representing http2 put header with wireshark dissecor
    """
    def __init__(self, packet=None, packet_raw=None, additional_filters=None):
        super().__init__(packet, packet_raw)
        self.packet_filter = [DisplayFilter(
            "http2.headers.method", "==", "PUT")]
        if additional_filters:
            self.packet_filter.extend(additional_filters)


class HTTP2Data(HTTP2Packet):
    """Class representing http2 data packet with wireshark dissecor
    """
    def __init__(self, packet=None, packet_raw=None, additional_filters=None):
        super().__init__(packet, packet_raw)
        self.packet_filter = [DisplayFilter("http2.type", "==", "0")]
        if additional_filters:
            self.packet_filter.extend(additional_filters)

    def json(self):
        """Tries to convert binary data to json format. The http2 data packet could be standalone
        part of a mime multipart http2 packet or part of a multilayer http2

        Returns:
            Any: json object
        """

        def json_string_from_data(data):
            hex_string = data.replace(":", "")
            return bytearray.fromhex(hex_string).decode("utf-8")

        def json_string_from_multipart(multipart):
            return bytearray.fromhex(multipart).decode("utf-8").split("\n", 1)[1]

        if hasattr(self.packet, 'get_multiple_layers'):
            for http2 in self.packet.get_multiple_layers('http2'):
                if http2.type == '0':
                    if hasattr(http2, 'mime_multipart_part'):
                        json_string = json_string_from_multipart(http2.mime_multipart_part)
                    else:
                        json_string = json_string_from_data(http2.data_data)
        elif hasattr(self.packet.http2, 'mime_multipart_part'):
            json_string = json_string_from_multipart(self.packet.http2.mime_multipart_part)
        elif hasattr(self.packet.http2, 'data_data'):
            json_string = json_string_from_data(self.packet.http2.data_data)
        
        if not json_string:
            raise RuntimeError("Could not obtain requested json data from http.")
        else:
            return json.loads(json_string)

