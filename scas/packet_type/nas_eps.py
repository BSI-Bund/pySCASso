"""Module providing subclass definition for NAS (non access stratum) and EPS packets"""
from scas.packet_type.common import DisplayFilter, PacketType


class NASEPSPacket(PacketType):
    """Subclass for EPS packets, layer_name is reflecting a wireshark dissector"""
    layer_name = "nas-eps"
    layer_nr = PacketType.layer_nrs[layer_name]


class S1APPacket(PacketType):
    """Subclass for S1AP packets, layer_name is reflecting a wireshark dissector"""
    layer_name = "s1ap"
    layer_nr = PacketType.layer_nrs[layer_name]


class SecurityModeCommand4G(S1APPacket):
    """Subclass for SecurityModeCommand message (4G), packet_filter is reflecting a wireshark
    dissector"""
    packet_filter = [DisplayFilter('nas_eps.nas_msg_emm_type', "==", '0x5d')]

    def toc(self):
        """returns the type of ciphering algorithm"""
        return int(self.packet.s1ap.nas_eps_emm_toc)

    def toi(self):
        """returns the type of integrity protection algorithm"""
        return int(self.packet.s1ap.nas_eps_emm_toi)

    def security_capabilities(self):
        """returns an object that represents the security capabilities with lists of booleans.
        The index of the boolean represents the specidic algorithm."""
        sec_caps = {
            "eea": [],
            "eia": [],
            "uea": [],
            "uia": [],
            "gea": []
        }
        for cap_key, cap_value in sec_caps.items():
            for i in range(0, 8):
                if cap_key == "uia" and i == 0:
                    cap_value.append(False)
                    continue
                pfx = "128" if i in [1, 2] and cap_key in ["eea", "eia"] else ""
                k = f"nas_eps.emm.{pfx}{cap_key}{str(i)}"
                cap_value.append(self.packet.s1ap.get_field(k))
        return sec_caps
