"""Module providing subclass definition for F1AP packets"""
# NOTE: This packet is needed for encapsulation of RRC messages
#  inside F1AP, when capturing traffic between gNB-DU and gNB-CU
from scas.packet_type.common import DisplayFilter, PacketType

class F1APPacket(PacketType):
    """Subclass for F1AP packets, layer_name is reflecting a wireshark dissector"""
    layer_name = "f1ap"
    layer_nr = PacketType.layer_nrs[layer_name]

class UEContextReleaseCommand(F1APPacket):
    """Subclass for UEContextReleaseCommand messages, packet_filter is equal to the wireshark
    dissector."""
    packet_filter = [DisplayFilter('f1ap.UEContextReleaseCommand_element', None, None)]

    def cause(self):
        """returns the cause of UEContextReleaseCommand message"""
        return int(self.packet.f1ap.cause)

    def cause_radionetwork(self):
        """returns the Radio Network Layer cause of UEContextReleaseCommand message if present"""
        if self.packet.f1ap.has_field('radionetwork'):
            return int(self.packet.f1ap.radionetwork)
        else:
            return -1;

    def is_normal_release(self):
        """returns True if the Radio Network Layer cause of UEContextReleaseCommand message is 'normal-release'
        This means that the action is due to a normal release of the UE
        (e.g. because of mobility) and does not indicate an error (see TS 38.473)

            cause == 0 means CauseRadioNetwork
            radionetwork == 10 means normal-release
        """
        return self.cause() == 0 and self.cause_radionetwork() == 10

    def msg_auth_code(self):
        """returns the pdcp mac-i as string"""
        # NOTE: this is a workaround, since the RRCContainer field is not properly decoded
        rrccontainer_str = self.packet.f1ap.rrccontainer.replace(":", '')
        rrccontainer_hex = int(rrccontainer_str, 16)
        maci = rrccontainer_hex & 0xffffffff  # MAC-I is the last 32 bits
        return maci
