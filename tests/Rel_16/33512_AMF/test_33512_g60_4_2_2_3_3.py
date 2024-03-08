#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type import UE5GSecurityCapabilities
from scas.packet_type.nas_5gs import (
    RegistrationRequest,
    SecurityModeCommand,
    SecurityModeComplete,
)

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.3.3
# Title: NAS integrity algorithm selection and use
# Purpose:
# Verify that the AMF selects the NAS integrity algorithm which has the highest priority according
# to the ordered list of supported integrity algorithms and is contained in the 5G security
# capabilities supported by the UE.
# Verify that the selected NAS security algorithm is being used.
#
# Execution Steps:
# ----------------
# 1. The UE sends a Registration Request with Initial Registration type to the AMF unders test.
# 2. The tester filters the Security Mode Command and Security Mode Complete messages.
# 3. The tester examines the selected integrity algorithm in the SMC against the list of ordered
# NAS integrity algorithm and the 5G security capabilities supported by the UE. The tester examines
# the MAC verification of the Security Mode Complete at the AMF under test.
#
# Expected Results:
# ----------------
# The selected integrity algorithm has the highest priority according to the list of ordered NAS
# integrity algorithm and is contained in the UE 5G security capabilities.
# The MAC verification of the Security Mode Complete message is successful.


def test_33512_g60_AMF_TC_NAS_INT_SELECTION_USE_AMF(provide_running_core, provide_core_config,
                                                    provide_running_ran, provide_ue):
    core = provide_running_core
    core_config = provide_core_config
    _ = provide_running_ran

    ue = provide_ue
    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach.pcap") \
        .record_event(lambda: ue.start())

    assert (rr := cap.get_first_packet_of_type(RegistrationRequest()))
    LOGGER.info("Registration Request found")

    assert rr.fivegs_reg_type() == 1
    LOGGER.info("RegistrationRequest type is \"initial registration\"")

    assert (SMComm := cap.get_first_packet_of_type(SecurityModeCommand()))
    LOGGER.info("Security Mode Command found")

    # get integrity protection algorithm selected in Security Mode Command
    selected_integ_prot_alg = SMComm.nas_sec_algo_integrity()

    # get ordered list of integrity protection algorithms of AMF config
    config_ordered_list_of_integrity_algo = core_config.read(
        ConfigKey.AMF_INTEGRITY_PROT_ALG_ORDERED_LIST)

    assert config_ordered_list_of_integrity_algo and len(
        config_ordered_list_of_integrity_algo) > 0
    LOGGER.info("Got ordered list of integrity algorithms from AMF config: %s",
                config_ordered_list_of_integrity_algo)

    # get the highest order integrity protection algorithm that is also supported by the UE
    sec_caps = UE5GSecurityCapabilities(rr)
    highest_supported_integrity_algo = next(
        (algo for algo in config_ordered_list_of_integrity_algo
         if sec_caps.supports_algorithm(algo)), None)

    assert highest_supported_integrity_algo
    LOGGER.info("Found integrity protection algorithm supported by UE with highest order: %s",
                highest_supported_integrity_algo)

    assert selected_integ_prot_alg == highest_supported_integrity_algo
    LOGGER.info("Correct algorithm selected in Security Mode Command")

    assert (SMComp := cap.get_first_packet_of_type(SecurityModeComplete()))
    LOGGER.info("Security Mode Complete found")

    LOGGER.info("Security Mode Complete MAC: %s", SMComp.msg_auth_code())

    # TODO: log the MAC verification at the AMF

    # skip("WIP")
