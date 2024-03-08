#!/usr/bin/python3

from datetime import datetime

import project_paths
from scas.device_interfaces.device import ActionKey, CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type.common import DisplayFilter
from scas.packet_type.http2 import (
    HTTP2Data,
    HTTP2Header,
    HTTP2HeaderCreated,
    HTTP2HeaderPost,
)
from scas.packet_type.nas_5gs import AuthenticationFailure, RegistrationReject

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.1.1
# Title: Synchronization failure handling
# Purpose:
# Verify that synchronization failure is correctly handled by the SEAF/AMF.
#
# Execution Steps:
# ----------------
# Test A:
# 1. The UE sends an authentication failure message to the SEAF/AMF with
# *synchronisation failure* (AUTS).
# 2. The SEAF/AMF sends a Nausf_UEAuthentication_Authenticate Request message with a
# "*synchronisation failure indication*" to the AUSF.
# 3. The AUSF sends a Nausf_UEAuthentication_Authenticate Response message to the SEAF/AMF
# immediately after receiving the request from the SEAF/AMF, to make sure the SEAF/AMF will receive
# the response before timeout.
# Test B:
# 1. The UE sends an authentication failure message to the SEAF/AMF with
# *synchronisation failure* (AUTS).
# 2. The SEAF/AMF sends a Nausf_UEAuthentication_Authenticate Request message with a
# "*synchronisation failure indication*" to the AUSF.
# 3. The AUSF does not send a Nausf_UEAuthentication_Authenticate Response message to the SEAF/AMF
# before timeout.
#
# Expected Results:
# ----------------
# Before receiving Nausf_UEAuthentication_Authenticate Response message from the AUSF and before
# the timer for receiving Nausf_UEAuthentication_Authenticate Response message runs out,
# For Test B, the SEAF/AMF does not send an    authentication towards the UE.


def test_33512_g60_TC_SYNC_FAIL_SEAF_AMF_A(provide_running_core, provide_core_config,
                                           provide_running_ran, provide_ue):
    core = provide_running_core
    core_config = provide_core_config
    _ = provide_running_ran

    ue = provide_ue
    ue.setup()
    ue.start()

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_sync_failure.pcap") \
        .record_event(lambda: (ue.perform(ActionKey.SYNC_FAILURE)))

    # Get the Auth Failure from the UE
    assert (ue_auth_fail := cap.get_first_packet_of_type(AuthenticationFailure()))
    LOGGER.info("Authentication Failure message from UE found")

    # Get the Nausf_UEAuthentication_Authenticate Request message after the Auth Fail
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          "/nausf-auth/v1/ue-authentications"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP)),
            DisplayFilter("frame.number", ">", ue_auth_fail.frame_number()),
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

    auth_post_json = auth_post_data_data.json()

    assert "resynchronizationInfo" in auth_post_json
    LOGGER.info(
        "resynchronizationInfo in Nausf_UEAuthentication_Authenticate Request message found")

    # Get the Nausf_UEAuthentication_Authenticate Response message from AUSF to AMF/SEAF
    response_header = HTTP2Header(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.AUSF_IP)),
            DisplayFilter("frame.number", ">",
                          auth_post_data_data.frame_number()),
        ]
    )

    assert (real_response_header :=
            cap.get_first_packet_of_type(response_header))
    LOGGER.info("Nausf_UEAuthentication_Authenticate Response message found")

    response_header_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==",
                          real_response_header.streamid()),
            DisplayFilter("frame.number", ">=",
                          real_response_header.frame_number()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.AUSF_IP)),
        ]
    )

    assert (real_response_header_data :=
            cap.get_first_packet_of_type(response_header_data))
    LOGGER.info(
        "Nausf_UEAuthentication_Authenticate Response message DATA found")

    start = float(
        auth_post_data_data.packet.frame_info.get_field_value('time_epoch'))
    end = float(
        real_response_header_data.packet.frame_info.get_field('time_epoch'))
    diff = datetime.fromtimestamp(end - start)

    diff_milliseconds = diff.microsecond / 1000

    assert diff_milliseconds < 15000
    LOGGER.info("Nausf_UEAuthentication_Authenticate Response message after %s ms - "
                "NAS Timer T3520 is usualy 15 seconds ", diff_milliseconds)


def test_33512_g60_4_2_2_1_1_B(provide_running_core, provide_core_config, provide_running_ran,
                               provide_ue):
    core = provide_running_core
    core_config = provide_core_config
    _ = provide_running_ran
    ue = provide_ue
    ue.setup()
    ue.start()

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_sync_failure_timeout.pcap") \
        .record_event(lambda: (ue.perform(ActionKey.SYNC_FAILURE)))

    # Get the SUCI
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          "/nausf-auth/v1/ue-authentications"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP))
        ]
    )

    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info(
        "HTTP POST Response /nausf-auth/v1/ue-authentications for AUSF found")

    post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP))
        ]
    )

    assert (post_data_data := cap.get_first_packet_of_type(post_data))
    LOGGER.info("HTTP Data /nausf-auth/v1/ue-authentications for AUSF found")

    _supiorsuci = post_data_data.json()['supiOrSuci']

    # Step 1
    assert (_rr := cap.get_first_packet_of_type(AuthenticationFailure()))
    LOGGER.info("Authentication failure found")

    # Step 2
    nausf_post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          "/nausf-auth/v1/ue-authentications"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP)),
            DisplayFilter("frame.number", ">", post_data_data.frame_number()),
        ]
    )

    assert (real_nausf_post := cap.get_first_packet_of_type(nausf_post))
    LOGGER.info(
        "HTTP POST /nausf-auth/v1/ue-authentications with AUTS for AUSF found")

    nausf_post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.AUSF_IP)),
            DisplayFilter("http2.streamid", "==", real_nausf_post.streamid()),
            DisplayFilter("frame.number", ">=",
                          real_nausf_post.frame_number()),
            # pyshark is unable to match this :(
            # DisplayFilter("json.member", "==", "resynchronizationInfo"),
            # DisplayFilter("json.member", "==", "rand"),
            # DisplayFilter("json.member", "==", "auts"),
        ]
    )

    assert (real_nausf_post_data :=
            cap.get_first_packet_of_type(nausf_post_data))
    assert real_nausf_post_data.json()['resynchronizationInfo']
    LOGGER.info("Nausf_UEAuthentication_Authenticate Request message with a synchronisation "
                "failure indication found")

    # Step 3
    response = HTTP2HeaderCreated(
        additional_filters=[
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.AUSF_IP)),
            DisplayFilter("http2.streamid", "==", real_nausf_post.streamid()),
            DisplayFilter("frame.number", ">", real_nausf_post.frame_number()),
        ]
    )

    # TODO: this only works if we prepair the AUSF to not send the response or we intercept and
    # drop the response from the AUSF
    assert cap.get_first_packet_of_type(response) is False
    LOGGER.info(
        "HTTP POST Response /nausf-auth/v1/ue-authentications from AUSF not found")

    # Result
    assert (_result := cap.get_first_packet_of_type(RegistrationReject()))
