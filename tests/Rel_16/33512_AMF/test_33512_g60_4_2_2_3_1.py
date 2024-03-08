#!/usr/bin/python3

import project_paths
from scas.device_interfaces.device import ActionKey, CaptureTarget
from scas.logger import LOGGER
from scas.packet_type.nas_5gs import SecurityModeCommand, SecurityModeComplete
from scas.packet_type.ngap import NGAPPacket

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.3.1
# Title: Replay protection of NAS signalling messages
# Purpose:
# Verify that the NAS signalling messages are replay protected by AMF over N1 interface between UE
# and AMF.
#
# Execution Steps:
# ----------------
# 1. The tester shall capture the NAS SMC procedure taking place between UE and AMF over N1
# interface using any network analyser.
# 2. The tester shall filter the NAS Security Mode Complete message by using a filter.
# 3. The tester shall check for the NAS SQN of filtered NAS Security Mode Complete message and
# using any packet crafting tool the tester shall create a NAS Security Mode Complete message
# containing same NAS SQN of the filtered NAS Security Mode Complete message or the tester shall
# replay the captured NAS signalling packets.
# 4. Tester shall check whether the replayed NAS signalling packets were processed by the AMF by
# capturing over N1interface to see if any corresponding response message is received from the AMF.
# 5. Tester shall confirm that AMF provides replay protection by dropping/ignoring the replayed
# packet if no corresponding response is sent by the AMF to the replayed packet.
# 6. Tester shall verify from the result that if the crafted NAS Security Mode Complete message
# or replayed NAS signalling messages are not processed by the AMF when the N1 interface is
# replay protected
#
# Expected Results:
# ----------------
# The NAS signalling messages sent between UE and AMF over N1 interface are replay protected.


def test_33512_g60_AMF_TC_NAS_REPLAY_AMF(provide_running_core, provide_running_ran, provide_ue):
    core = provide_running_core
    _ = provide_running_ran
    ue = provide_ue

    cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/open5gs_attach.pcap") \
        .record_event(lambda: ue.start())

    assert cap.get_first_packet_of_type(SecurityModeCommand())
    LOGGER.info("Security Mode Command message found")

    assert (original_smc := cap.get_first_packet_of_type(SecurityModeComplete()))
    LOGGER.info("Security Mode Complete message found")

    original_smc_sqn = original_smc.seq_nr()
    LOGGER.info(f"Security Mode Complete SQN: {original_smc_sqn}")

    packet = cap.extract_pcap_by_packet_type(original_smc)

    # after replay we should check for any (other) ngap activity
    # if we don't receive any activity, the test is done
    replay_cap = core.create_capture(target=CaptureTarget.GENERIC) \
        .set_dummy_file(f"{project_paths.PCAPS}/SecurityModeComplete.pcap") \
        .record_event(event=lambda: core.perform(ActionKey.REPLAY_PACKET, packet=packet),
                      timeout_sec=5, continue_after_event_sec=5)

    assert (replayed_smc := replay_cap.get_first_packet_of_type(
        SecurityModeComplete()))
    LOGGER.info("New Security Mode Complete message found")

    assert replayed_smc.seq_nr() == original_smc_sqn
    LOGGER.info("SQN of original and replayed SMC are equal")

    # the one available NGAP packet is our replayed SMC message
    assert len(replay_cap.get_packets_of_type(NGAPPacket())) == 1
    LOGGER.info("No more ngap packets received. AMF is replay protected.")
