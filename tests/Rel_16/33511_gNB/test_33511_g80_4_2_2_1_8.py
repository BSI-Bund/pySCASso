#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.8
# Title: Replay protection of user data between the UE and the gNB
# Purpose:
#  To verify that the user data packets are replay protected over the NG RAN air interface.
#
# Execution Steps:
# ----------------
# 1. The tester shall capture the user plane data sent between UE and gNB using any network
# analyser over the NG RAN air interface.
# 2. Tester shall filter user plane data packets sent between UE and gNB.
# 3. Tester shall replay the captured user plane packets or shall use any packet crafting tool to
# create a user plane packet similar to the captured user plane packet and replay to the gNB.
# 4. Tester shall check whether the replayed user plane packets were processed by the gNB by
# capturing over NG RAN air interface to see if any corresponding response message is received from
# the gNB.
# 5. Tester shall confirm that gNB provides replay protection by dropping/ignoring the replayed
# packet if no corresponding response is received from the gNB to the replayed packet.
# 6. Tester shall verify from the result that if the replayed user plane packets are not accepted
# by gNB, the NG RAN air interface is replay protected.
#
# Expected Results:
# ----------------
# The user plane packets sent between the UE and gNB over the NG air interface is replay protected.


def test_33511_g80_TC_UP_DATA_REPLAY_gNB():
    skip('Not implemented...')
