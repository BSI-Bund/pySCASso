import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.logger import LOGGER
from scas.packet_type.nas_eps import SecurityModeCommand4G

# Function: eNB
# Source: 33216-g70.md
# Section: 4.2.2.1.5
# Title: AS algorithms selection
# Purpose:
# Verify that the eNB selects the algorithms with the highest priority in its configured list.
#
# Execution Steps:
# ----------------
# 1. The UE sends attach request message to the eNB.
# 2. The eNB receives S1 context setup request message.
# 3. The eNB sends the SECURITY MODE COMMAND message.
# 4. The UE replies with the AS SECURITY MODE COMPLETE message.
#
# Expected Results:
# ----------------
# The eNB initiates the SECURITY MODE COMMAND message that includes the chosen algorithm with the
# highest priority according to the ordered lists and is contained in the UE EPS security
# capabilities. The MAC in the AS SECURITY MODE COMPLETE message is verified, and the AS protection
# algorithms are selected and applied correctly.


def test_33216_g70_eNB_4_2_2_1_5(provide_core):
    core = provide_core

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/oneplus8_attach.pcap") \
        .record_event()

    # Assert
    assert (smc := cap.get_first_packet_of_type(SecurityModeCommand4G()))
    LOGGER.info(f"Security capabilities: {smc.security_capabilities()}")

    assert (smc.toc() == 2)
    LOGGER.info(f"Ciphering algorithm: {smc.toc()}")

    assert (smc.toi() == 2)
    LOGGER.info(f"Integrity protection algorithm: {smc.toi()}")
