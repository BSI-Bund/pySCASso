#!/usr/bin/python3

import project_paths
from scas.device_interfaces import ConfigKey
from scas.device_interfaces.device import ActionKey, CaptureTarget
from scas.logger import LOGGER
from scas.packet_type.common import DisplayFilter
from scas.packet_type.http2 import HTTP2Header, HTTP2HeaderGet

# Function: NRF
# Source: 33518-g20.md
# Section: 4.2.2.2.1
# Title: NF discovery authorization for specific slice
# Purpose:
# Verify that the NRF under test does not authorize slice specific discovery request for the NF
# instance which is not part of the requested slice, according to the slice specific discovery
# configuration of the requested NF instance.
#
# Execution Steps:
# ----------------
# 1. The NF2 registers at the NRF under test with a list of S-NSSAI.
# 2. The NF1 sends an Nnrf_NFDiscovery_Request to the NRF under test with the expected service name
# of NF2, NF type of the expected NF2.
# 3. The NRF under test determines that NF2 instance only allows discovery from NFs belonging to
# slice A, according to the "allowedNssais" list stored in NF2 Profile.
#
# Expected Results:
# ----------------
# The NRF under test returns a response with "403 Forbidden" status code, as specified in
# clause 5.3.2.2.2 of TS 29.510 [5].


def test_33518_g20_TC_DISC_AUTHORIZATION_SLICE_NRF(provide_running_core, provide_core_config):
    core = provide_running_core
    core_config = provide_core_config

    requester_nf_type = "AMF"
    requester_nf_nssais_sd = "0BEEF0"

    target_nf_type = "SMF"
    _target_nf_nssais_sd = "0CAFE0"

    def reg_reg_disc():
        core.perform(ActionKey.NRF_REGISTRATION,
                     requester_nf_type=requester_nf_type,
                     requester_nf_nssais_sd=requester_nf_nssais_sd,
                     requester_nf_ip_addr="127.0.0.1",
                     requester_nf_instance_id="589af3ae-14cf-41ee-8887-37aa46161e81")
        # we could register only the requester because there already will be a lot of nfs available
        # in a different slice
        # core.perform(ActionKey.NRF_REGISTRATION, requester_nf_type=target_nf_type,
        #              requester_nf_nssais_sd=target_nf_nssais_sd,
        #              requester_nf_ip_addr="127.0.0.1",
        #              requester_nf_instance_id="589af3ae-14cf-41ee-8887-37aa46161e85")
        core.perform(ActionKey.NRF_DISCOVERY, requester_nf_type=requester_nf_type,
                     target_nf_type=target_nf_type, requester_nf_nssais_sd=requester_nf_nssais_sd)

    cap = core.create_capture(target=CaptureTarget.NRF) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_nrf_reg_disc.pcapng") \
        .record_event(lambda: reg_reg_disc())

    get = HTTP2HeaderGet(
        additional_filters=[
            DisplayFilter("http2.headers.path", "contains",
                          f"/nnrf-disc/v1/nf-instances?target-nf-type={target_nf_type}&"
                          f"requester-nf-type={requester_nf_type}"),
            DisplayFilter("ip.dst", "==", core_config.read(ConfigKey.NRF_IP))
        ]
    )

    assert (real_get := cap.get_first_packet_of_type(get))
    LOGGER.info("NRF discovery request found")

    response_header = HTTP2Header(
        additional_filters=[
            DisplayFilter("http2.streamid", "==", real_get.streamid()),
            DisplayFilter("frame.number", ">", real_get.frame_number()),
            DisplayFilter("ip.src", "==", core_config.read(ConfigKey.NRF_IP)),
        ]
    )

    assert (real_response_header := cap.get_first_packet_of_type(response_header))
    LOGGER.info("NRF discovery response header found")

    status = real_response_header.status()

    assert status == 403  # open5gs and free5gc fail this!
    LOGGER.info("NF2 discovery from NF1 was rejected")
