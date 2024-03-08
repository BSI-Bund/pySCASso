"""Module implementing NAS 5GS packets"""
from dataclasses import dataclass
from typing import Union

from scas.packet_type.common import (DisplayFilter, PacketType,
                                     SecurityAlgorithm,
                                     UE5GSecurityCapabilities)
from scas.packet_type.ngap import NGAPPacket


class Nas5gsPacket(NGAPPacket):
    """Subclass for NAS packets (5G), packet_filter is reflecting a wireshark dissector"""
    def seq_nr(self):
        """returns the NAS sequence number"""
        return int(self.packet.ngap.nas_5gs_seq_no)


# TODO: rework this container to remove cross-inheritance
class FiveGGutiContainer(PacketType):
    """Class representing GUTI fields in packets. Can be added to other packet implementations."""
    def mobile_identity_type_id(self):
        """returns the mobile identities type id"""
        return int(self.packet.ngap.nas_5gs_mm_type_id)

    def mcc(self):
        """returns the mcc of the mobile identity"""
        return int(self.packet.ngap.e212_guami_mcc)

    def mnc(self):
        """returns the mnc of the mobile identity"""
        return int(self.packet.ngap.e212_guami_mnc)

    def amf_region_id(self):
        """returns the amf_region_id of the mobile identity"""
        return int(self.packet.ngap.amfregionid)

    def amf_set_id(self):
        """returns the amf_set_id of the mobile identity"""
        return int(self.packet.ngap.amfsetid.replace(":", ""), 16)

    def fiveg_tmsi(self):
        """returns the 5g tmsi of the mobile identity"""
        return int(self.packet.ngap.nas_5gs_5g_tmsi)


class AuthenticationRequest(Nas5gsPacket):
    """Subclass for AuthenticationRequest messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter("nas_5gs.mm.message_type", "==", "0x56")]


class AuthenticationResponse(Nas5gsPacket):
    """Subclass for AuthenticationResponse messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter("nas_5gs.mm.message_type", "==", "0x57")]


class AuthenticationFailure(Nas5gsPacket):
    """Subclass for AuthenticationFailure messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter("nas_5gs.mm.message_type", "==", "0x59")]

    def failure_cause(self):
        """returns the failure cause of AuthenticationFailure message"""
        return int(self.packet.ngap.nas_5gs_mm_5gmm_cause)


class ServiceRequest(Nas5gsPacket):
    """Subclass for ServiceRequest messages, packet_filter is equal to the wireshark dissector."""
    packet_filter = [DisplayFilter("nas_5gs.mm.message_type", "==", "0x4c")]


class ServiceAccept(Nas5gsPacket):
    """Subclass for ServiceAccept messages, packet_filter is equal to the wireshark dissector."""
    packet_filter = [DisplayFilter("nas_5gs.mm.message_type", "==", "0x4e")]
    prefs = {"nas-5gs.null_decipher": "TRUE"}


class UEConfigurationUpdateCommand(Nas5gsPacket, FiveGGutiContainer):
    """Subclass for UEConfigurationUpdateCommand messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter("nas_5gs.mm.message_type", "==", "0x54")]
    prefs = {"nas-5gs.null_decipher": "TRUE"}


class RegistrationAccept(Nas5gsPacket, FiveGGutiContainer):
    """Subclass for RegistrationAccept messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nas-5gs.mm.message_type', "==", '0x42')]
    prefs = {"nas-5gs.null_decipher": "TRUE"}


class RegistrationReject(Nas5gsPacket, FiveGGutiContainer):
    """Subclass for RegistrationReject messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nas-5gs.mm.message_type', "==", '0x44')]

    def reject_cause(self):
        """returns the reject cause of RegistrationReject message"""
        return int(self.packet.ngap.nas_5gs_mm_5gmm_cause)


class RegistrationRequest(Nas5gsPacket, UE5GSecurityCapabilities):
    """Subclass for RegistrationRequest messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nas-5gs.mm.message_type', "==", '0x41')]

    def fivegs_reg_type(self):
        """returns the registration type (e.g. initial)"""
        return int(self.packet.ngap.nas_5gs_mm_5gs_reg_type)


class SecurityModeComplete(Nas5gsPacket):
    """Subclass for SecurityModeComplete messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nas-5gs.mm.message_type', "==", '0x5e')]
    prefs = {"nas-5gs.null_decipher": "TRUE"}

    def msg_auth_code(self):
        """returns the mac as string"""
        return self.packet.ngap.nas_5gs_msg_auth_code


class SecurityModeCommand(Nas5gsPacket, UE5GSecurityCapabilities):
    """Subclass for SecurityModeCommand messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nas-5gs.mm.message_type', "==", '0x5d')]

    def nas_sec_algo_integrity(self) -> SecurityAlgorithm:
        """returns the chosen integrity protection algorithm"""
        code = int(self.packet.ngap.nas_5gs_mm_nas_sec_algo_ip)
        return SecurityAlgorithm.algorithm_by_name(f"NIA{code}")

    def nas_sec_algo_encryption(self):
        """returns the chosen integrity protection algorithm"""
        code = int(self.packet.ngap.nas_5gs_mm_nas_sec_algo_enc)
        return SecurityAlgorithm.algorithm_by_name(f"NEA{code}")

    def security_header_type(self):
        """returns the security header type"""
        return int(self.packet.ngap.nas_5gs_security_header_type)


@dataclass
class Guti:
    """Dataclass capturing only guti data.
    This exists mainly to prevent too-many-arguments / R0913 of pylint.
    """
    mcc: int
    mnc: int
    amf_region_id: int
    amf_set_id: int
    tmsi: int


class FiveGGUTI():
    """Class representing GUTI data and some useful methods."""
    __create_key = object()

    @classmethod
    def create(cls, packet: Union[RegistrationAccept, UEConfigurationUpdateCommand]):
        """Factory method that creates a GUTI object from a given packet

        Args:
            packet (Union[RegistrationAccept, UEConfigurationUpdateCommand]):   packet containing
                                                                                GUTI data
        Returns:
            FiveGGUTI: GUTI object
        """
        try:
            mcc = packet.mcc()
            mnc = packet.mnc()
            amf_region_id = packet.amf_region_id()
            amf_set_id = packet.amf_set_id()
            tmsi = packet.fiveg_tmsi()
            guti = Guti(mcc, mnc, amf_region_id, amf_set_id, tmsi)
            return FiveGGUTI(cls.__create_key, guti)
        except KeyError:
            return None

    def __init__(self, create_key, guti: Guti):
        assert (create_key == FiveGGUTI.__create_key), \
            "GUTI object must be created using GUTI.create"
        self.mcc = guti.mcc
        self.mnc = guti.mnc
        self.amf_region_id = guti.amf_region_id
        self.amf_set_id = guti.amf_set_id
        self.tmsi = guti.tmsi

    def __cmp__(self, other):
        return self.mcc == other.mcc and \
            self.mnc == other.mnc and \
            self.amf_region_id == other.amf_region_id and \
            self.amf_set_id == other.amf_set_id and \
            self.tmsi == other.tmsi

    def __str__(self):
        return (f"mcc: {self.mcc} mnc: {self.mnc} "
                f"amf_region_id: {self.amf_region_id} amf_set_id: "
                f"{self.amf_set_id} tmsi: {self.tmsi}")
