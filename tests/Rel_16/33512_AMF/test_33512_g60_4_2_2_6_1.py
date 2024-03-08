#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type.nas_5gs import RegistrationReject

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.6.1
# Title: Invalid or unacceptable UE security capabilities handling
# Purpose:
# Verify that UE security capabilities invalid or unacceptable are not accepted by the AMF under
# test in registration procedure.
#
# Execution Steps:
# ----------------
# The UE sends UE security capabilities to the AMF under test using registration request message.
#
# Expected Results:
# ----------------
# The tester captures the Registration reject message sent by AMF under test to the UE.


def test_33512_g60_TC_UE_SEC_CAP_HANDLING_AMF(provide_running_core, provide_running_ran,
                                              provide_ue):
    core = provide_running_core
    _ = provide_running_ran
    ue = provide_ue

    # store original values
    IA1_value = ue.get_config().read(ConfigKey.UE_INTEGRITY_ALG_IA1)
    IA2_value = ue.get_config().read(ConfigKey.UE_INTEGRITY_ALG_IA2)
    IA3_value = ue.get_config().read(ConfigKey.UE_INTEGRITY_ALG_IA3)
    EA1_value = ue.get_config().read(ConfigKey.UE_CIPHERING_ALG_EA1)
    EA2_value = ue.get_config().read(ConfigKey.UE_CIPHERING_ALG_EA2)
    EA3_value = ue.get_config().read(ConfigKey.UE_CIPHERING_ALG_EA3)

    # write garbage values
    ue.get_config().write(ConfigKey.UE_INTEGRITY_ALG_IA1, "false")
    ue.get_config().write(ConfigKey.UE_INTEGRITY_ALG_IA2, "false")
    ue.get_config().write(ConfigKey.UE_INTEGRITY_ALG_IA3, "false")
    ue.get_config().write(ConfigKey.UE_CIPHERING_ALG_EA1, "false")
    ue.get_config().write(ConfigKey.UE_CIPHERING_ALG_EA2, "false")
    ue.get_config().write(ConfigKey.UE_CIPHERING_ALG_EA3, "false")

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach_invalid_ue_caps.pcap") \
        .record_event(lambda: (ue.start(), ue.stop()))

    # reset ue config to normal
    ue.get_config().write(ConfigKey.UE_INTEGRITY_ALG_IA1, IA1_value)
    ue.get_config().write(ConfigKey.UE_INTEGRITY_ALG_IA2, IA2_value)
    ue.get_config().write(ConfigKey.UE_INTEGRITY_ALG_IA3, IA3_value)
    ue.get_config().write(ConfigKey.UE_CIPHERING_ALG_EA1, EA1_value)
    ue.get_config().write(ConfigKey.UE_CIPHERING_ALG_EA2, EA2_value)
    ue.get_config().write(ConfigKey.UE_CIPHERING_ALG_EA3, EA3_value)

    # NOTE free5gc fails this test, open5gs works fine
    assert (rr := cap.get_first_packet_of_type(RegistrationReject()))
    LOGGER.info(f"Registration Reject message received. Cause: {rr.reject_cause()}")
