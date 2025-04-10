"""Module containing the generic packet type definition and some helper functions"""
import ipaddress
import re
from collections import namedtuple
from enum import Enum
from typing import Dict

from scas.logger import LOGGER

DisplayFilter = namedtuple('DisplayFilter', ['key', 'operator', 'value'])


def is_valid_ip_address(sample_str):
    """Validates of a given string is a ip v4 address

    Args:
        sample_str (str): string to check for ip v4

    Returns:
        boolean: true if valid ipv4, otherwise false
    """
    try:
        ipaddress.ip_network(sample_str)
        return True
    except ValueError:
        return False


def is_valid_hex_string(string):
    """Validates if string only contains hex chars

    Args:
        string (str): string to check

    Returns:
        boolean: True if string only contains hex chars, else False
    """
    match = re.search(r'^0x(?:[0-9a-fA-F]*)$', string)
    if match:
        return True
    return False

# These classes serve as function library to be used by the actual tests


class PacketType():
    """base-class: derive dedicated PacketClasses from this"""
    def __init__(self, packet=None, packet_raw=None):
        self.packet = packet
        self.packet_raw = packet_raw

    prefs: Dict[str, str] = {}
    packet_filter = []
    layer_name = ""
    # TODO this does not work since e.g. with http2 there can be more than one http2 layer
    # in on packet
    layer_nr = -1
    layer_nrs = {
        "frame": 0,
        "ip": 1,
        "tcp": 2,
        "nr-rrc": 2,
        "f1ap": 3,
        "ngap": 3,
        "http": 3,
        "http2": 3,
        "s1ap": 3,
        "nas-eps": 4,
        "nas-5gs": 4,
    }

    def frame_number(self):
        """Returns the ethernet frame number of this packet
        """
        return int(self.packet.frame_info.number)

    def match_in_layer(self, _packet_layer, _target_layer_name, _disp_filter):
        """DEPRECATED
        """
        return True
        # check if our disp_filter is specific for our top level layer name
        # we do the rest afterwards
        # if target_layer_name not in disp_filter.key:
        #     return False

        # # check if disp_filter field is inside the layer fields
        # if disp_filter.key not in packet_layer._all_fields:
        #     return False

        # # check if the disp_filter fields value matches the one in the packet
        # match disp_filter.operator:
        #     case "==":
        #         if packet_layer._all_fields[disp_filter.key] != f"{disp_filter.value}":
        #             return False
        #     case "!=":
        #         if packet_layer._all_fields[disp_filter.key] == f"{disp_filter.value}":
        #             return False
        #     case "<":
        #         if packet_layer._all_fields[disp_filter.key] >= f"{disp_filter.value}":
        #             return False
        #     case ">":
        #         if packet_layer._all_fields[disp_filter.key] <= f"{disp_filter.value}":
        #             return False
        #     case "<=":
        #         if packet_layer._all_fields[disp_filter.key] > f"{disp_filter.value}":
        #             return False
        #     case ">=":
        #         if packet_layer._all_fields[disp_filter.key] < f"{disp_filter.value}":
        #             return False

        # return True

    # TODO: do we actually need this match method?
    # if we make our display filter precise enough, there will be only one filtered packet...
    # FIXME: yes we need this at least for HTTP2 messages that can be concatenated
    # e.g. SETTINGS and HEADER types in one TCP packet
    def matches(self, _packet):
        """DEPRECATED
        """
        return True

        # cls = self.__class__
        # # check if there are enough layers in our packet
        # if len(packet.layers) <= cls.layer_nr:
        #     return False

        # # get the top level layer corresponding to our packet type
        # clayer = packet.layers[cls.layer_nr]

        # # check if the top level layer name matches, as same layer nr can be applied to
        # # different layer names
        # if clayer.layer_name != cls.layer_name:
        #     return False

        # lower_level_filters = []

        # # packet_filter is a dictionary
        # for disp_filter in self.packet_filter:
        #     # check if our filter is specific for our top level layer name
        #     # we do the rest afterwards
        #     if cls.layer_name not in disp_filter.key:
        #         lower_level_filters.append(disp_filter)
        #         continue

        #     # check if disp_filter field is inside the layer fields
        #     if disp_filter.key not in clayer._all_fields:
        #         return False

        #     # check if the disp_filter fields value matches the one in the packet
        #     match disp_filter.operator:
        #         case "==":
        #             if clayer._all_fields[disp_filter.key] != f"{disp_filter.value}":
        #                 return False
        #         case "!=":
        #             if clayer._all_fields[disp_filter.key] == f"{disp_filter.value}":
        #                 return False
        #         case "<":
        #             if clayer._all_fields[disp_filter.key] >= f"{disp_filter.value}":
        #                 return False
        #         case ">":
        #             if clayer._all_fields[disp_filter.key] <= f"{disp_filter.value}":
        #                 return False
        #         case "<=":
        #             if clayer._all_fields[disp_filter.key] > f"{disp_filter.value}":
        #                 return False
        #         case ">=":
        #             if clayer._all_fields[disp_filter.key] < f"{disp_filter.value}":
        #                 return False

        # # check lower level filters
        # for disp_filter in lower_level_filters:
        #     match disp_filter.key.split(".")[0]:
        #         case "frame":
        #             # unfortunatly the frame data is an object not present in the layer list
        #             layer_nr = None
        #             layer_name = "frame"
        #             pass
        #         case "eth":
        #             layer_nr = PacketType.layer_nrs["eth"]
        #             layer_name = "eth"
        #         case "ip":
        #             layer_nr = PacketType.layer_nrs["ip"]
        #             layer_name = "ip"
        #         case "tcp":
        #             layer_nr = PacketType.layer_nrs["tcp"]
        #             layer_name = "tcp"
        #         case "http":
        #             layer_nr = PacketType.layer_nrs["http"]
        #             layer_name = "http"
        #         case _:
        #             LOGGER.debug(
        #                 f"Filter field {disp_filter.key} queried"
        #                 f"but not in packet that matches top layer.")
        #             continue

        #     if layer_nr:
        #         lower_layer = packet.layers[layer_nr]
        #     else:
        #         lower_layer = packet.frame_info

        #     if not self.match_in_layer(lower_layer, layer_name, disp_filter):
        #         return False

        # return True

    def create(self, packet, packet_raw=None):
        """Generic factory method for packets"""
        return self.__class__(
            packet=packet, packet_raw=packet_raw) if self.matches(packet) else False

    def get_filter_string(self):
        """Creates and returns the filter string for a packet.
            This string is a wireshark display filter.

        Returns:
            str: filter string
        """
        display_filter = self.__class__.layer_name

        if len(self.packet_filter) == 0:
            return display_filter

        for disp_filter in self.packet_filter:
            # NOTE: filters for label-type fields do not have a value
            if disp_filter.value == None or disp_filter.value == '':
                display_filter += f' and {disp_filter.key}'
                continue
            if isinstance(disp_filter.value, str):
                if (disp_filter.value.isdigit() or
                        is_valid_ip_address(disp_filter.value) or
                        is_valid_hex_string(disp_filter.value)):
                    display_filter += (
                        f' and {disp_filter.key} {disp_filter.operator} '
                        f'{disp_filter.value}')
                else:
                    display_filter += (
                        f' and {disp_filter.key} {disp_filter.operator} '
                        f'"{disp_filter.value}"')
            else:
                display_filter += (
                    f' and {disp_filter.key} {disp_filter.operator} '
                    f'{disp_filter.value}')
        return display_filter

    def get_layer(self, layer=None):
        """returns the highest or a specific layer of a packet

        Args:
            layer (integer, optional): The requested layers index. Defaults to None.

        Returns:
            PacketLayer: the requested layer
        """
        if len(self.packet.layers) != self.layer_nr + 1:
            LOGGER.warning(
                "highest layer %s != layer_nr %s + 1"
                "(could be caused by multiple http2 streams in one packet)",
                len(self.packet.layers), self.layer_nr)
            # TODO return the highest layer - should we always do this? (currently we do)
            return self.packet.layers[-1]

        return self.packet.layers[layer if layer else self.layer_nr]


class SecurityAlgorithm(Enum):
    """Enum to hold and convert security algorithms.
    This is a useful abstraction cause every core, ran, ue implementation uses its
    own names for the algorithms and we want generic test implementations.
    """
    EEA0 = 0
    EEA1 = 1
    EEA2 = 2
    EEA3 = 3
    EEA4 = 4
    EEA5 = 5
    EEA6 = 6
    EEA7 = 7
    EIA0 = 8
    EIA1 = 9
    EIA2 = 10
    EIA3 = 11
    EIA4 = 12
    EIA5 = 13
    EIA6 = 14
    EIA7 = 15
    NEA0 = 16
    NEA1 = 17
    NEA2 = 18
    NEA3 = 19
    NEA4 = 20
    NEA5 = 21
    NEA6 = 22
    NEA7 = 23
    NIA0 = 24
    NIA1 = 25
    NIA2 = 26
    NIA3 = 27
    NIA4 = 28
    NIA5 = 29
    NIA6 = 30
    NIA7 = 31

    def __eq__(self, __o: object) -> bool:
        if self.__class__ is __o.__class__:
            return self.value == __o.value
        return NotImplementedError

    @classmethod
    def algorithm_by_name(cls, name: str):
        """
            Get an algorithm enum item by name.
            Returns None if name is invalid.
        """
        try:
            return getattr(cls, name)
        except AttributeError:
            return None


class SecurityAlgorithmMapping():
    """Class implementing sec algo mapping and enum/string conversion"""
    def __init__(self):
        """ dict with Sec. Algorithm names (from the enum) as keys
        # and the provided mapping strings as values, e.g.:
        # {"NIA0": "nia0", "NEA1": "5g_nea1", ...}"""
        self.mapping = {}

        """initialize all mappings to 1:1 (exact name, e.g. NIA1)"""
        for algo in list(SecurityAlgorithm):
            self.mapping[algo.name] = algo.name

    def get_mapping(self, algo: SecurityAlgorithm) -> str:
        """returns the string mapped to a given sec. algorithm"""
        return str(self.mapping[algo.name])

    def get_original(self, mapping_value: str) -> SecurityAlgorithm:
        """
            Returns the Sec. Algorithm for a given mapping value.
            Returns None if the value cannot be found.
            Always returns the first matching algorithm
            (possibly, there could be >1 with the same mapping value).
        """
        for name, value in self.mapping.items():
            if value == mapping_value:
                return SecurityAlgorithm.algorithm_by_name(name)
        LOGGER.warning("Failed to map sec alg: %s", mapping_value)
        return None  # nothing found

    def set_single_mapping(self, algo: SecurityAlgorithm, value: str) -> None:
        """sets a new string to be mapped to a given sec. algorithm"""
        self.mapping[algo.name] = value

    def set_mappings(self, algos: list[(SecurityAlgorithm, str)]) -> None:
        """
            Bulk-sets new strings to be mapped to given sec. algorithms.
            the provided list must contain 0..n tuples of 1 Enum(SecurityAlgorithm) and 1 string.
        """
        for algo, value in algos:
            self.mapping[algo.name] = value


class UE5GSecurityCapabilities():
    """Class for mapping UE 5G security capabilities"""
    FILTER_KEY = "wireshark_nas5gs_filter"
    SUPPORTED_KEY = "supported"

    algorithms = {
        SecurityAlgorithm.EEA0.name: {
            FILTER_KEY: "nas-5gs.mm.eea0",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EEA1.name: {
            FILTER_KEY: "nas-5gs.mm.128eea1",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EEA2.name: {
            FILTER_KEY: "nas-5gs.mm.128eea2",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EEA3.name: {
            FILTER_KEY: "nas-5gs.mm.eea3",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EEA4.name: {
            FILTER_KEY: "nas-5gs.mm.eea4",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EEA5.name: {
            FILTER_KEY: "nas-5gs.mm.eea5",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EEA6.name: {
            FILTER_KEY: "nas-5gs.mm.eea6",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EEA7.name: {
            FILTER_KEY: "nas-5gs.mm.eea7",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA0.name: {
            FILTER_KEY: "nas-5gs.mm.eia0",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA1.name: {
            FILTER_KEY: "nas-5gs.mm.128eia1",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA2.name: {
            FILTER_KEY: "nas-5gs.mm.128eia2",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA3.name: {
            FILTER_KEY: "nas-5gs.mm.eia3",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA4.name: {
            FILTER_KEY: "nas-5gs.mm.eia4",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA5.name: {
            FILTER_KEY: "nas-5gs.mm.eia5",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA6.name: {
            FILTER_KEY: "nas-5gs.mm.eia6",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.EIA7.name: {
            FILTER_KEY: "nas-5gs.mm.eia7",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA0.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ea0",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA1.name: {
            FILTER_KEY: "nas-5gs.mm.128_5g_ea1",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA2.name: {
            FILTER_KEY: "nas-5gs.mm.128_5g_ea2",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA3.name: {
            FILTER_KEY: "nas-5gs.mm.128_5g_ea3",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA4.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ea4",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA5.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ea5",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA6.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ea6",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NEA7.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ea7",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA0.name: {
            FILTER_KEY: "nas-5gs.mm.ia0",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA1.name: {
            FILTER_KEY: "nas-5gs.mm.5g_128_ia1",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA2.name: {
            FILTER_KEY: "nas-5gs.mm.5g_128_ia2",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA3.name: {
            FILTER_KEY: "nas-5gs.mm.5g_128_ia3",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA4.name: {
            FILTER_KEY: "nas-5gs.mm.5g_128_ia4",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA5.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ia5",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA6.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ia6",
            SUPPORTED_KEY: False
        },
        SecurityAlgorithm.NIA7.name: {
            FILTER_KEY: "nas-5gs.mm.5g_ia7",
            SUPPORTED_KEY: False
        }
    }

    def __init__(self, from_packet: PacketType = None) -> None:
        if from_packet:
            for algo, value in self.algorithms.items():
                value[self.SUPPORTED_KEY] = self.algorithm_in_packet(
                    from_packet, SecurityAlgorithm.algorithm_by_name(algo))

    def supports_algorithm(self, algo: SecurityAlgorithm) -> bool:
        """check if a given algorithm is set to be supported"""
        return self.algorithms[algo.name][self.SUPPORTED_KEY]

    def all_algorithms(self) -> dict[dict]:
        """Returns a list of all algorithms stored in a sec. capabilities object."""
        return self.algorithms

    def get_algorithm(self, algo: SecurityAlgorithm) -> dict:
        """Get an algorithm dict by its enum (e.g. SecurityAlgorithm.NIA0)."""
        return self.algorithms[algo.name]

    def algorithm_in_packet(self, packet: PacketType, algo: SecurityAlgorithm) -> bool:
        """check if a given algorithm is supported in a given network packet"""
        return bool(packet.packet.ngap.get_field(self.get_algorithm(algo)[self.FILTER_KEY]))

    def supported_algorithms(self) -> list[SecurityAlgorithm]:
        """get a list with all algorithms that are set to supported"""
        return [SecurityAlgorithm.algorithm_by_name(algo)
                for algo, value in self.algorithms.items() if value[self.SUPPORTED_KEY]]
