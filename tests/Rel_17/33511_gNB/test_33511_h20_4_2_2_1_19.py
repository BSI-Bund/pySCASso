#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-h20.md
# Section: 4.2.2.1.19
# Title: UP security activation in Inactive scenario
# Purpose:
# Verify that the target gNB/ng-eNB uses the UP security activation status to activate the
# UP security.
#
# Execution Steps:
# ----------------
# 1. The tester shall complete a Registration Procedure and PDU Session establishment procedure
# to make sure the gNB configure the UP security, and get the UP security activation status.
# 2. The gNB sends RRC Release message with a suspend config to the UE.
# 3. The tester deletes the UP security activation status of the UE.
# 4. The tester triggers the UE to send RRC Resume message.
#
# Expected Results:
# ----------------
# The gNB sends RRC Setup message to the UE.


def test_33511_h20_TC_GNB_INACTIVE_TO_ACTIVE():
    skip('Not implemented...')
