#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.9
# Title: Replay protection of RRC-signalling
# Purpose:
#  To verify the replay protection of RRC-signalling between UE and gNB over the NG RAN air
# interface.
#
# Execution Steps:
# ----------------
# 1. The tester shall capture the data sent between UE and the gNB using any network analyser over
# the NG RAN air interface.
# 2. Tester shall filter RRC signalling packets.
# 3. Tester shall check for the RRC SQN of the filtered RRC signalling packets and shall use any
# packet crafting tool to create RRC signalling packets similar to the captured packets or the
# tester shall replay the captured RRC uplink packet to the gNB to perform the replay attack over
# gNB.
# 4. Tester shall check whether the replayed RRC signalling packets were processed by the gNB or
# not, by capturing over NG RAN air interface to see if any corresponding response message is
# received from the gNB.
# 5. Tester shall confirm that gNB provides replay protection by dropping/ignoring the replayed
# packet if no corresponding response is sent by the gNB to the replayed packet.
#
# Expected Results:
# ----------------
# The RRC signalling over the NG RAN air interface is replay protected.


def test_33511_g80_TC_UP_DATA_RRC_REPLAY_gNB():
    skip('Not implemented...')
