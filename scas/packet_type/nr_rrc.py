"""Module providing subclass definition for NR RRC packets"""
from scas.packet_type.common import (DisplayFilter, PacketType,
                                     SecurityAlgorithm)


class NRRRCPacket(PacketType):
    """Subclass for RRC (NR) packets, layer_name is reflecting a wireshark dissector"""
    layer_name = "nr-rrc"
    layer_nr = PacketType.layer_nrs[layer_name]

class DLDCCHMessage(NRRRCPacket):
    """Subclass for DL-DCCH-Message messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nr-rrc.DL_DCCH_Message_element', None, None)]

    def msg_auth_code_present(self):
        """returns True if the pdcp mac-i is present"""
        if 'f1ap' in self.packet:
            return self.packet.f1ap.pdcp_nr_maci_present
        else:
            raise NotImplementedError("Only F1AP/RRC messages are supported")

    def msg_auth_code(self):
        """returns the pdcp mac-i as string"""
        if 'f1ap' in self.packet:
            return self.packet.f1ap.pdcp_nr_mac
        else:
            raise NotImplementedError("Only F1AP/RRC messages are supported")

class ULDCCHMessage(NRRRCPacket):
    """Subclass for UL-DCCH-Message messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nr-rrc.UL_DCCH_Message_element', None, None)]

    def msg_auth_code_present(self):
        """returns True if the pdcp mac-i is present"""
        if 'f1ap' in self.packet:
            return self.packet.f1ap.pdcp_nr_maci_present
        else:
            raise NotImplementedError("Only F1AP/RRC messages are supported")

    def msg_auth_code(self):
        """returns the pdcp mac-i as string"""
        if 'f1ap' in self.packet:
            return self.packet.f1ap.pdcp_nr_mac
        else:
            raise NotImplementedError("Only F1AP/RRC messages are supported")

class SecurityModeComplete(ULDCCHMessage):
    """Subclass for SecurityModeComplete messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nr-rrc.securityModeComplete_element', None, None)]

class SecurityModeCommand(DLDCCHMessage):
    """Subclass for SecurityModeCommand messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nr-rrc.securityModeCommand_element', None, None)]

    def rrc_sec_algo_integrity(self) -> SecurityAlgorithm:
        """returns the chosen integrity protection algorithm"""
        if 'f1ap' in self.packet:
            code = int(self.packet.f1ap.nr_rrc_integrityprotalgorithm)
        else:
            raise NotImplementedError("Only F1AP/RRC messages are supported")
        return SecurityAlgorithm.algorithm_by_name(f"NIA{code}")

    def rrc_sec_algo_encryption(self):
        """returns the chosen ciphering algorithm"""
        if 'f1ap' in self.packet:
            code = int(self.packet.f1ap.nr_rrc_cipheringalgorithm)
        else:
            raise NotImplementedError("Only F1AP/RRC messages are supported")
        return SecurityAlgorithm.algorithm_by_name(f"NEA{code}")

class RRCRelease(DLDCCHMessage):
    """Subclass for RRCRelease messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('nr-rrc.rrcRelease_element', None, None)]
