#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.4.1
# Title: Bidding down prevention in Xn-handover
# Purpose:
# Verify that bidding down is prevented by the AMF under test in Xn handovers.
#
# Execution Steps:
# ----------------
# 1. The tester sends 5G security capabilities for the UE, different from the ones stored in the
# AMF, to the AMF under test using a Path-Switch message.
# 2. The tester captures the Path-Switch Acknowledge message sent by AMF under test to the target
# gNB.
# 3. The tester examines the AMF log regarding the capability mismatch.
#
# Expected Results:
# ----------------
# The Path-Switch Acknowledge message sent by AMF under test to the target gNB, which includes the
# locally stored 5G security capabilities in the AMF under test for that UE.
# The log entry shows that the capability mismatch is logged.


def test_33512_i10__TC_BIDDING_DOWN_XN_AMF():
    skip('Not implemented...')
