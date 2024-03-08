#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.device_interfaces.device_config import ConfigKey
from scas.logger import LOGGER
from scas.packet_type import DisplayFilter
from scas.packet_type.http2 import HTTP2Data, HTTP2HeaderPost

# Function: UDM
# Source: 33514-g40.md
# Section: 4.2.1.1
# Title: De-concealment of SUPI from the SUCI based on the protection scheme used to generate
# the SUCI.
# Purpose:
# Verify that the SIDF De-conceals the SUPI from the SUCI based on the protection scheme used to
# generate the SUCI.
#
# Execution Steps:
# ----------------
# Tester shall capture the entire authentication procedure between UE and AMF over N1, N12 and N13
# interface using any network analyser.
# 1. Tester shall filter the Nudm_Authentication_Get Response message sent from UDM to AUSF over
# N13 interface containing the SUPI.
# 2. Tester shall compare the SUPI gotten from UE and the SUPI retrieved from
# Nudm_Authentication_Get Response message.
# NOTE: The tester may filter the Nausf_UEAutentication_Authenticate Response message sent from the
# UDM/AUSF to the AMF over N12 interface containing the SUPI, if the UDM and AUSF network products
# are collocated without an open N13 interface.
#
# Expected Results:
# ----------------
# SIDF resolves the SUPI from the SUCI based on the protection scheme used to generate the SUCI.


def test_33514_g40_TC_DE_CONCEAL_SUPI_from_SUCI_UDM(provide_running_core, provide_core_config,
                                                    provide_running_ran, provide_ue):
    core = provide_running_core
    core_config = provide_core_config
    _ = provide_running_ran
    ue = provide_ue
    ue.setup()

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach_sbi.pcap") \
        .record_event(lambda: (ue.start()))

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

    supiorsuci = post_data_data.json()['supiOrSuci']

    # AUSF asks UDM for auth data (and for SUPI)
    # we need this to receive the http2 stream id
    post = HTTP2HeaderPost(
        additional_filters=[
            DisplayFilter("http2.headers.path", "==",
                          f"/nudm-ueau/v{core_config.read(ConfigKey.UDM_UEAU_OPENAPI_VERSION)}"
                          f"/{supiorsuci}/security-information/generate-auth-data"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.UDM_IP))
        ]
    )

    assert (real_post := cap.get_first_packet_of_type(post))
    LOGGER.info("UEAuthentication Request for UDM found.")

    data = HTTP2Data(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_post.streamid()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.UDM_IP))
        ]
    )

    assert (response_data := cap.get_first_packet_of_type(data))
    LOGGER.info("UEAuthentication Response for AUSF found.")

    supi = response_data.json()['supi']

    LOGGER.info(f"SUPI@UE: {ue.get_config().read(ConfigKey.UE_SUPI)}")
    LOGGER.info(f"SUPI@AR: {supi}")
    assert ue.get_config().read(ConfigKey.UE_SUPI) == supi
