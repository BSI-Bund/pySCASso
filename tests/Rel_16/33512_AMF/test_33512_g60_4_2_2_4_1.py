#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-g60.md
# Section: 4.2.2.4.1
# Title: Bidding down prevention in Xn-handover
# Purpose:
# Verify that bidding down is prevented by the AMF under test in Xn handovers.
#
# Execution Steps:
# ----------------
# The tester sends 5G security capabilities for the UE, different from the ones stored in the AMF,
# to the AMF under test using a Path-Switch message.
#
# Expected Results:
# ----------------
# The tester captures the Path-Switch Acknowledge message sent by AMF under test to the target gNB,
# which includes the locally stored 5G security capabilities in the AMF under test for that UE.
# The tester verifies that a log entry showing the capability mismatch is logged.


def test_33512_g60_TC_BIDDING_DOWN_XN_AMF():
    skip('Not implemented...')
