#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import ActionKey, CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type import DisplayFilter
from scas.packet_type.http2 import HTTP2Data, HTTP2HeaderPost
from scas.packet_type.nas_5gs import AuthenticationFailure

# Function: UDM
# Source: 33514-g40.md
# Section: 4.2.2.1
# Title: Synchronization failure handling
# Purpose:
# Verify that synchronization failure is recovered correctly in the home network.
#
# Execution Steps:
# ----------------
# 1. The AUSF sends an Nudm_UEAuthentication_Get Request message to the UDM with a
# "synchronisation failure indication" and parameters RAND and AUTS.
# 2. The UDM/ARPF performs steps 1-5 as described in TS 33.102, clause 6.3.5.
#
# Expected Results:
# ----------------
# The UDM sends an Nudm_UEAuthentication_Get Response message with a new authentication vector to
# the AUSF.
# NOTE: The expected results would be that the UDM/AUSF sends an
# Nausf_UEAuthentication_Authenticate Response message with EAP Request/AKA'-Challenge for
# EAP AKA', or 5G SE AV for 5G AKA to the AMF, if the UDM and AUSF network products are collocated
# without an open N13 interface.


def test_33514_g40_4_2_2_1(provide_running_core, provide_core_config, provide_running_ran,
                           provide_ue):
    core = provide_running_core
    core_config = provide_core_config
    _ = provide_running_ran

    ue = provide_ue
    ue.setup()
    ue.start()

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_sync_failure.pcap") \
        .record_event(lambda: (ue.perform(ActionKey.SYNC_FAILURE)))

    # Get the SUCI
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          "/nausf-auth/v1/ue-authentications"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP)),
        ]
    )

    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info("HTTP POST /nausf-auth found")

    auth_post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP)),
        ]
    )

    assert (auth_post_data_data := cap.get_first_packet_of_type(auth_post_data))
    LOGGER.info("HTTP DATA /nausf-auth found")

    suci = auth_post_data_data.json()['supiOrSuci']

    # Step 0
    assert (auth_failure := cap.get_first_packet_of_type(AuthenticationFailure()))
    LOGGER.info("Found Authentication Failure")

    assert auth_failure.failure_cause() == 21  # 21 is sync failure
    LOGGER.info("Authentication Failure cause is Synchronization Failure")

    # Step 1
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          f"/nudm-ueau/v{core_config.read(ConfigKey.UDM_UEAU_OPENAPI_VERSION)}"
                          f"/{suci}/security-information/generate-auth-data"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.UDM_IP)),
            DisplayFilter("frame.number", ">", auth_failure.frame_number()),
        ]
    )

    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info(
        "HTTP POST /nudm-ueau/v%s/%s/security-information/generate-auth-data for UDM found",
        core_config.read(ConfigKey.UDM_UEAU_OPENAPI_VERSION), suci)

    post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.UDM_IP)),
            # DisplayFilter("json.member", "==", "resynchronizationInfo"),
            # DisplayFilter("json.member", "==", "rand"),
            # DisplayFilter("json.member", "==", "auts"),
        ]
    )

    assert (post_data_data := cap.get_first_packet_of_type(post_data))
    LOGGER.info(
        "HTTP DATA /nudm-ueau/v%s/%s/security-information/generate-auth-data for UDM found",
        core_config.read(ConfigKey.UDM_UEAU_OPENAPI_VERSION), suci)

    # Result
    post_response = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", post_data_data.streamid()),
            DisplayFilter("frame.number", ">=", post_data_data.frame_number()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.UDM_IP)),
            # DisplayFilter("json.member", "==", "authenticationVector")
        ]
    )

    assert (real_post_response := cap.get_first_packet_of_type(post_response))
    LOGGER.info("HTTP POST with new Auth Vector found\n%s", real_post_response.json())
