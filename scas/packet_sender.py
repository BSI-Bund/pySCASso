"""Module for sending a crafted packet"""
from dataclasses import dataclass

from scapy.all import send, sendp
from scapy.layers.inet import IP, Ether
from scapy.layers.sctp import SCTP, SCTPChunkData


@dataclass
class Address:
    """Dataclass to capture address data
    """
    mac: str = None
    ip_add: str = "0.0.0.0"
    port: int = 0


def send_ngap_packet(data, src_address: Address, dst_address: Address):
    """ Sends a NGAP packet

    Parameters
    ----------
    data : bytes
        NGAP data, if the data is in hex it needs to be passed with `bytes.fromhex()`
    src_ip : str
        Source IP
    dst_ip : str
        Destination IP
    src_port : int
        Source Port
    dst_port : int
        Destionation Port
    src_mac : str, optional
        Source MAC address, if not defined the default is `00:00:00:00:00:00`
    dst_mac : str, optional
        Destination MAC address, if not defined the default is `ff:ff:ff:ff:ff:ff` (Broadcast)
    """

    src_mac, src_ip, src_port = src_address
    dst_mac, dst_ip, dst_port = dst_address

    eth_ip = Ether(src=src_mac, dst=dst_mac) / IP(src=src_ip, dst=dst_ip)

    sctp = SCTP(src=src_port, dst=dst_port)
    sctp_data_payload = data
    sctp_data_hdr = SCTPChunkData(
        data=sctp_data_payload, proto_id=60, beginning=1, ending=1)

    pkt = eth_ip / sctp / sctp_data_hdr

    # If a MAC address is not defined scapy routes the packet.
    # This may lead to a malformed packet, if the destionation MAC is not found.
    if (src_mac or dst_mac):
        sendp(pkt)
    else:
        send(pkt)
