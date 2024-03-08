#!/usr/bin/python3

from pytest import skip

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.logger import LOGGER
from scas.packet_type.nas_5gs import (FiveGGUTI, RegistrationAccept,
                                      RegistrationRequest, ServiceAccept,
                                      ServiceRequest,
                                      UEConfigurationUpdateCommand)

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.5.1
# Title: 5G-GUTI allocation
# Purpose:
# Verify that a new 5G-GUTI is allocated by the AMF under test in these scenarios accordingly.
#
# Execution Steps:
# ----------------
# Test case 1:
# Upon receiving Registration Request message of type "initial registration" from a UE, the AMF
# sends a new 5G-GUTI to the UE during the registration procedure.
# Test case 2:
# Upon receiving Registration Request message of type "mobility registration update" from a UE, the
# AMF sends a new 5G-GUTI to the UE during the registration procedure.
# Test case 3:
# Upon receiving Service Request message sent by the UE in response to a Paging message, the AMF
# sends a new 5G-GUTI to the UE.
#
# Expected Results:
# ----------------
# For Test case 1, 2, 3, the tester retrieves a new 5G-GUTI by accessing the NAS signalling packets
# sent by the AMF under test over N1 interface during registration procedure.
# For Test case 1, 2, 3, the NAS message encapsulating the new 5G-GUTI is confidentiality and
# integrity protected by the AMF under test using the NAS security context, which is same as the
# UE's NAS security context.
# The new 5G-GUTI is different from the old 5G-GUTI.


def test_33512_g60_AMF_TC_5G_GUTI_ALLOCATION_AMF_1(provide_running_core, provide_running_ran,
                                                   provide_ue):
    core = provide_running_core
    _ = provide_running_ran
    ue = provide_ue
    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach_reattach.pcap") \
        .record_event(lambda: (ue.start(), ue.stop(), ue.start()))

    assert (rr := cap.get_first_packet_of_type(RegistrationRequest()))
    LOGGER.info("Registration Request found")

    assert rr.fivegs_reg_type() == 1
    LOGGER.info(
        f"Registration type: {rr.fivegs_reg_type()} (1==initial registration)")

    assert (ras := cap.get_packets_of_type(RegistrationAccept()))

    # we assume we get (at least) 2 registration accept messages!
    assert len(ras) >= 2
    LOGGER.info(f"Registration Accept messages found: {len(ras)}")

    assert ras[0].mobile_identity_type_id() == 2
    LOGGER.info(
        f"RA message 0: Mobile identity type: {ras[0].mobile_identity_type_id()} (2==5G-GUTI)")

    assert ras[1].mobile_identity_type_id() == 2
    LOGGER.info(
        f"RA message 1: Mobile identity type: {ras[1].mobile_identity_type_id()} (2==5G-GUTI)")

    # import pdb; pdb.set_trace()

    # crafting 5G-GUTIs
    old_guti = FiveGGUTI.create(ras[0])
    new_guti = FiveGGUTI.create(ras[1])

    assert old_guti != new_guti
    LOGGER.info("5G-GUTIs differ between 2 RA messages.")


def test_33512_g60_AMF_TC_5G_GUTI_ALLOCATION_AMF_2():
    # TODO: in order to get the "mobility registration update", we need to cause a TAI update
    # mobility registration update procedure is performed if the current TAI of the serving
    # cell is not in the list of TAIs that the UE received from the network...
    # TAI = Tracking Area Identity
    # The Tracking Area identity is the identity used to identify tracking areas. The Tracking Area
    # Identity is constructed from the MCC (Mobile Country Code), MNC (Mobile Network Code) and
    # TAC (Tracking Area Code).
    # skip("not implemented")ruff
    skip("not implemented")


def test_33512_g60_AMF_TC_5G_GUTI_ALLOCATION_AMF_3(provide_running_core, provide_running_ran,
                                                   provide_ue):
    core = provide_running_core
    _ = provide_running_ran
    ue = provide_ue
    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach_reattach.pcap") \
        .record_event(lambda: (ue.start(), ue.stop(), ue.start()))

    # TODO: should we check for paging message first?

    assert cap.get_first_packet_of_type(ServiceRequest())
    LOGGER.info("Service Request found")

    assert cap.get_first_packet_of_type(ServiceAccept())
    LOGGER.info("Service Accept found")

    # Upon receiving network triggered Service Request message from the UE
    # (i.e., Service Request message sent by the UE in response to a Paging message),
    # the AMF shall use a UE Configuration Update procedure to send a new 5G-GUTI to the UE

    assert (_cucs := cap.get_first_packet_of_type(
        UEConfigurationUpdateCommand()))
    LOGGER.info("UE configuration update command found")

    # assert (new_guti := GUTI.create(cucs[0]))

    skip("WIP")

    assert (_cucs := cap.get_first_packet_of_type(
        UEConfigurationUpdateCommand()))
    LOGGER.info("UE configuration update command found")

    # assert (new_guti := GUTI.create(cucs[0]))

    skip("WIP")
