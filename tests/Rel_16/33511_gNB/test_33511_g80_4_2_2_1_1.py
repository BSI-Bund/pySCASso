#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import CaptureTarget
from scas.packet_type.common import SecurityAlgorithm
from scas.packet_type.nr_rrc import (SecurityModeCommand, SecurityModeComplete,
                                     DLDCCHMessage, RRCRelease)
from scas.packet_type.f1ap import UEContextReleaseCommand
from scas.logger import LOGGER

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.1
# Title: Integrity protection of RRC-signalling
# Purpose:
#  To verify that the RRC-signalling data sent between UE and gNB over the NG RAN air interface are
# integrity protected.
#
# Execution Steps:
# ----------------
# 1. The NIA0 is disabled at UE and gNB.
# 2. gNB sends AS SMC message to the UE, and UE responses AS SMP.
# 3. Check any RRC message sent by gNB after sending AS SMC and before UE enters CM-Idle state is
# integrity protected.
#
# Expected Results:
# ----------------
# Any RRC-signalling over the NG RAN air interface is integrity protected after gNB sending AS SMC.


def test_33511_g80_TC_CP_DATA_INT_RRC_SIGN_gNB(provide_running_core, provide_running_ran, provide_ue):
    core = provide_running_core
    _ = provide_running_ran
    ue = provide_ue

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/oai_split_attach.pcap") \
        .record_event(lambda: ue.start())

    assert (SMComm := cap.get_first_packet_of_type(SecurityModeCommand()))
    LOGGER.info("AS Security Mode Command message found")

    # get integrity protection algorithm selected in AS Security Mode Command
    selected_integ_prot_alg = SMComm.rrc_sec_algo_integrity()
    assert (selected_integ_prot_alg != SecurityAlgorithm.NIA0)
    LOGGER.info(f"{selected_integ_prot_alg.name} was chosen for RRC integrity protection")

    # get AS SecurityModeComplete message sent from the UE
    assert (SMComp := cap.get_first_packet_of_type(SecurityModeComplete()))
    LOGGER.info("AS Security Mode Complete message found")

    assert (SMComp.msg_auth_code_present())
    LOGGER.info(f"AS Security Mode Complete MAC is present")

    # INFO: we consider a message integrity protected if the MAC-I is present and is not zero
    #  (the probability of MAC-I being 0 with a non-NIA0 algorithm is negligible)
    assert (SMComp.msg_auth_code().hex_value != 0)
    LOGGER.info(f"AS Security Mode Complete MAC is {SMComp.msg_auth_code()}")
    
    # check any RRC messages sent by gNB after sending AS SMC and before UE enters CM-Idle state 
    # first get all RRC messages of type DL-DCCH-Message (i.e. from gNB to UE) from the capture
    # as per TS 38.331, these messages must be integrity protected after AS security activation
    assert (len(rrc_pkts := cap.get_packets_of_type(DLDCCHMessage())) != 0)
    LOGGER.info(f"{len(rrc_pkts)} RRC DL-DCCH-Message packets found in the capture")

    # filter only packets after AS SMC
    # NOTE: AS SMC itself must be integrity protected 
    rrc_pkts_after_smcomm = [pkt for pkt in rrc_pkts if pkt.frame_number() >= SMComm.frame_number()]
    LOGGER.info(f"{len(rrc_pkts_after_smcomm) - 1} RRC DL-DCCH-Message packets found after AS SMC")

    # INFO: RRCRelease message is used to command the release of an RRC connection or
    #  the suspension of the RRC connection (see TS 38.331)
    rrc_release_pkt = cap.get_first_packet_of_type(RRCRelease())
    # NOTE: this is a workaround when capturing from the F1 interface (for CU-DU split)
    #  (for some reason, tshark/pyshark does not match the RRCRelease filter in the test capture)
    f1ap_release_pkt = cap.get_first_packet_of_type(UEContextReleaseCommand())
    if rrc_release_pkt: 
        last_frame_num = rrc_release_pkt.frame_number()
        LOGGER.info(f"RRCRelease message found - iterating until RRCRelease")
    elif f1ap_release_pkt and f1ap_release_pkt.is_normal_release():
        last_frame_num = f1ap_release_pkt.frame_number()
        LOGGER.info(f"F1AP UEContextReleaseCommand message found with 'normal-release' cause - iterating until UEContextReleaseCommand")
        # NOTE: RRCRelease must be integrity protected after AS security activation, as per TS 38.331
        #  in this case, RRCRelease is encapsulated inside RRCContainer
        assert (f1ap_release_pkt.msg_auth_code() != 0), f"RRCRelease in F1AP UEContextReleaseCommand has a zero MAC"
    else:
        last_frame_num = rrc_pkts_after_smcomm[-1].frame_number() 
        LOGGER.info(f"Neither RRCRelease nor F1AP UEContextReleaseCommand message found - iterating until the last packet")

    # check that all packets from gNB to UE after AS SMC (including AS SMC itself) are integrity protected 
    for rrc_pkt in rrc_pkts_after_smcomm:
        assert (rrc_pkt.msg_auth_code_present()), f"Packet with frame number {rrc_pkt.frame_number()} does not have a MAC"
        assert (rrc_pkt.msg_auth_code().hex_value != 0), f"Packet with frame number {rrc_pkt.frame_number()} has a zero MAC"
        if rrc_pkt.frame_number() == last_frame_num:
            LOGGER.info(f"The {'RRCRelease packet' if rrc_release_pkt or f1ap_release_pkt else 'last RRC packet'} encountered - done")
            break
