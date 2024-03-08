"""Module providing subclass definition for NGAP packets"""
from scas.packet_type.common import PacketType


class NGAPPacket(PacketType):
    """Subclass for NGAP packets, layer_name is reflecting a wireshark dissector"""
    layer_name = "ngap"
    layer_nr = PacketType.layer_nrs[layer_name]
