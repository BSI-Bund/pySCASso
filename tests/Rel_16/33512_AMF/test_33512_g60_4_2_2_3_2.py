#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.logger import LOGGER
from scas.packet_type import SecurityAlgorithm
from scas.packet_type.nas_5gs import SecurityModeCommand

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.3.2
# Title: NAS NULL integrity protection
# Purpose:
# Verify that NAS NULL integrity protection algorithm is used correctly.
#
# Execution Steps:
# ----------------
# 1. The AMF derives the K~AMF~ and NAS signalling keys after successful authentication of the UE.
# 2. The AMF sends the NAS Security Mode Command message to the UE containing the selected
# NAS algorithms.
#
# Expected Results:
# ----------------
# The integrity algorithm selected by the AMF in NAS SMC message is different from NIA0.
# The NAS Security Mode Command message is integrity protected by the AMF.


def test_33512_g60_AMF_TC_NAS_NULL_INT_AMF(provide_running_core, provide_running_ran, provide_ue):
    core = provide_running_core
    _ = provide_running_ran
    ue = provide_ue
    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach.pcap") \
        .record_event(lambda: ue.start())

    assert (smc := cap.get_first_packet_of_type(SecurityModeCommand()))
    LOGGER.info("Security Mode Command message found")

    assert smc.nas_sec_algo_integrity() != SecurityAlgorithm.NIA0
    LOGGER.info(
        f"Integrity protection algorithm: {smc.nas_sec_algo_integrity()}")

    assert smc.security_header_type() != 0
    LOGGER.info("Security Mode Command is (at least) integrity protected")
