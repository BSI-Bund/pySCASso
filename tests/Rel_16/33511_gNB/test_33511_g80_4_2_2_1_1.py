#!/usr/bin/python3

from pytest import skip

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


def test_33511_g80_TC_CP_DATA_INT_RRC_SIGN_gNB():
    skip('Not implemented...')
