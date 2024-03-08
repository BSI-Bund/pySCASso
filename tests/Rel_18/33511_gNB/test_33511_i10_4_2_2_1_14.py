#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-i10.md
# Section: 4.2.2.1.14
# Title: Bidding down prevention in Xn-handovers
# Purpose:
# Verify that bidding down is prevented in Xn-handovers.
#
# Execution Steps:
# ----------------
# The target gNB sends the path-switch message to the AMF.
#
# Expected Results:
# ----------------
# The UE NR security capabilities are in the path-switch message.


def test_33511_i10__TC_Xn_handover_bid_down_gNB():
    skip('Not implemented...')
