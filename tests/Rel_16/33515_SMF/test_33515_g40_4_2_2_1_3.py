#!/usr/bin/python3

from pytest import skip

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type import DisplayFilter
from scas.packet_type.http2 import HTTP2Data, HTTP2Header, HTTP2HeaderPost

# import httpx

# Function: SMF
# Source: 33515-g40.md
# Section: 4.2.2.1.3
# Title: Security functional requirements on the SMF checking UP security policy
# Purpose:
# Verify that the SMF checks the UP security policy that is sent by the ng-eNB/gNB during handover.
#
# Execution Steps:
# ----------------
# 1. The tester sends the Nsmf_PDUSession_UpdateSMContext Request message to the SMF under test. A
# UE UP security policy different than the one preconfigured at the SMF under test is included in
# the Request message.
# 2. The tester captures the Nsmf_PDUSession_UpdateSMContext Response message sent from the SMF
# under test.
#
# Expected Results:
# ----------------
# The preconfigured UE security policy is contained in the 'n2SmInfo' IE in the captured Response
# message.


def test_33515_g40_TC_UP_SECURITY_POLICY_SMF(provide_running_core, provide_core_config,
                                             provide_running_ran, provide_ue):
    core = provide_running_core
    core_config = provide_core_config
    _ = provide_running_ran

    ue = provide_ue
    ue.setup()

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach_sbi.pcap") \
        .record_event(lambda: (ue.start()))

    # Receive information to craft Nsmf_PDUSession_UpdateSMContext Request message
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          "/nsmf-pdusession/v1/sm-contexts"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.SMF_IP))
        ]
    )
    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info(
        "HTTP POST Request /nsmf-pdusession/v1/sm-contexts for SMF found")

    post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.SMF_IP))
        ]
    )

    assert (post_data_data := cap.get_first_packet_of_type(post_data))
    LOGGER.info("HTTP Data /nsmf-pdusession/v1/sm-contexts for SMF found")

    _supi = post_data_data.json()['supi']

    # get the smContextRef
    response_header = HTTP2Header(additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">", post_data_data.frame_number()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.SMF_IP))
        ]
    )

    assert (real_response_header :=
            cap.get_first_packet_of_type(response_header))

    # open5gs has a url as smContextRef
    # free5gc has a uuid as smContextRef
    # free5gc does not comply to the standard here, hence the clunky workaround
    header_location = real_response_header.packet.http2.headers_location
    smContextRef = core_config.read(
        ConfigKey.SM_CONTEXT_REF, header_location=header_location)

    _api_path = f"/nsmf-pdusession/v1/sm-contexts/{smContextRef}/modify"

    _headers = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
    }

    skip("WIP - needs NAS 5GS packet crafting")

    # TODO: we need to append an n2SmInfo IE here, which will point to a encapsulated multipart
    # field
    # that will be a Plain NAS 5GS Message of type

    # with httpx.Client(http1=False, http2=True) as client:
    #     response = client.post(f"http://{core_config.read(ConfigKey.SMF_IP)}:"
    #                            f"{core_config.read(ConfigKey.SMF_PORT)}{api_path}",
    #                            data=data, headers=headers)
