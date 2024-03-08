#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type import DisplayFilter
from scas.packet_type.http2 import HTTP2Data, HTTP2HeaderGet, HTTP2HeaderPost

# Function: SMF
# Source: 33515-g40.md
# Section: 4.2.2.1.1
# Title: Priority of UP security policy
# Purpose:
# Verify that the user plane security policy from the UDM takes precedence at the SMF under test
# over locally configured user plane security policy.
#
# Execution Steps:
# ----------------
# 1. The tester triggers PDU session establishment procedure by sending
# Nsmf_PDUSession_CreateSMContext Request message to the SMF.
# 2. The SMF under test retrieves the Session Management Subscription data using Nudm_SDM_Get
# service from UDM, where the Session Management Subscription data includes the user plane security
# policy stored in UDM.
# 3. The tester captures the Namf_Communication_N1N2MessageTransfer message sent from the SMF under
# test to the AMF.
#
# Expected Results:
# ----------------
# There is a Security Indication IE in the N2 SM information contained in the
# Namf_Communication_N1N2MessageTransfer message, which is the same with the UP security policy
# configured in the UDM.


def test_33515_g40_TC_UP_POLICY_PRECEDENCE_SMF(provide_core, provide_ran, provide_ue):
    core = provide_core
    core.setup()
    core.get_config().write(ConfigKey.SMF_NAS_SECURITY_INDICATION_INTEGRITY, "not-needed")
    core.get_config().write(
        ConfigKey.SMF_NAS_SECURITY_INDICATION_CONFIDENTIALITY, "not-needed")
    core.start()

    ran = provide_ran
    ran.setup()

    ue = provide_ue
    ue.setup()

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach_sbi.pcap") \
        .record_event(lambda: (ran.start(), ue.start()))

    # Step 1
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          "/nsmf-pdusession/v1/sm-contexts"),
            DisplayFilter("ip.dst", "==",
                          core.get_config().read(ConfigKey.SMF_IP))
        ]
    )
    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info(
        "HTTP POST Request /nsmf-pdusession/v1/sm-contexts for SMF found")

    post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("frame.number", ">=", real_post.frame_number()),
            DisplayFilter("ip.dst", "==",
                          core.get_config().read(ConfigKey.SMF_IP))
        ]
    )

    assert (post_data_data := cap.get_first_packet_of_type(post_data))
    LOGGER.info("HTTP Data /nsmf-pdusession/v1/sm-contexts for SMF found")

    supi = post_data_data.json()['supi']

    # Step 2
    get = HTTP2HeaderGet(
        additional_filters=[
            DisplayFilter("http2.headers.path", "contains",
                          f"/nudm-sdm/v{core.get_config().read(ConfigKey.UDM_SDM_OPENAPI_VERSION)}"
                          f"/{supi}/sm-data"),
            DisplayFilter("ip.dst", "==",
                          core.get_config().read(ConfigKey.UDM_IP))
        ]
    )

    assert (real_get := cap.get_first_packet_of_type(get))
    LOGGER.info(
        f"HTTP GET Request /nudm-sdm/v{core.get_config().read(ConfigKey.UDM_SDM_OPENAPI_VERSION)}"
        f"/{supi}/sm-data from SMF found (streamid: {real_get.streamid()})")

    get_response = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_get.streamid()),
            DisplayFilter("frame.number", ">=", real_get.frame_number()),
            DisplayFilter("ip.src", "==",
                          core.get_config().read(ConfigKey.UDM_IP))
        ]
    )

    assert (get_response_data := cap.get_first_packet_of_type(get_response))
    LOGGER.info(f"HTTP GET response found (streamid: {real_get.streamid()})")

    LOGGER.info(get_response_data.json())

    try:
        up_security_integrity_at_udm = get_response_data.json(
        )[0]['dnnConfigurations']['internet']['upSecurity']['upIntegr']
        up_security_confidentiality_at_udm = get_response_data.json(
        )[0]['dnnConfigurations']['internet']['upSecurity']['upConfid']
    except KeyError:
        assert False, "UP Security indication not send in Session Management Subscription data."

    # Step 3
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          f"/namf-comm/v1/ue-contexts/{supi}/n1-n2-messages"),
            DisplayFilter("ip.dst", "==",
                          core.get_config().read(ConfigKey.AMF_IP))
        ]
    )

    assert (post_header := cap.get_first_packet_of_type(post))
    LOGGER.info(
        "Namf_Communication_N1N2MessageTransfer message found (streamid: %s)",
        post_header.streamid())

    post_data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", post_header.streamid()),
            DisplayFilter("frame.number", ">=", post_header.frame_number()),
            DisplayFilter("ip.dst", "==",
                          core.get_config().read(ConfigKey.AMF_IP))
        ]
    )

    assert (post_data_data := cap.get_first_packet_of_type(post_data))
    LOGGER.info(
        "Namf_Communication_N1N2MessageTransfer data found (streamid: %s)",
        post_data_data.streamid())

    # The UP security indication is burried as part of ecapsulated multipart data inside http2 data
    try:
        integrity_protection_indication = post_data_data.packet.http2.get_field(
            'ngap_integrityProtectionIndication')
        confidentiality_protection_indication = post_data_data.packet.http2.get_field(
            'ngap_confidentialityProtectionIndication')
    except KeyError:
        assert False, \
            "No UP security indication found in Namf_Communication_N1N2MessageTransfer response"

    # compare the UP security policies

    # this is the mapping on the ngap layer - this can be different elsewhere!
    indicator_mapping = {"0": "REQUIRED", "1": "PREFERRED", "2": "NOT_NEEDED"}

    LOGGER.info("UP security indication integrity SMF local: NOT NEEDED")
    LOGGER.info("UP security indication integrity at UDM: %s", up_security_integrity_at_udm)
    LOGGER.info("UP security indication integrity at Namf_Communication_N1N2MessageTransfer: %s",
                indicator_mapping[integrity_protection_indication])

    LOGGER.info("UP security indication confidentiality SMF local: NOT NEEDED")
    LOGGER.info("UP security indication confidentiality at UDM: %s",
                up_security_confidentiality_at_udm)
    LOGGER.info(
        "UP security indication confidentiality at Namf_Communication_N1N2MessageTransfer: %s",
        indicator_mapping[confidentiality_protection_indication])

    assert up_security_integrity_at_udm == indicator_mapping[integrity_protection_indication]
    LOGGER.info("UP security integrity from UDM is applied")

    assert up_security_confidentiality_at_udm == indicator_mapping[
        confidentiality_protection_indication]
    LOGGER.info("UP security confidentiality from UDM is applied")
