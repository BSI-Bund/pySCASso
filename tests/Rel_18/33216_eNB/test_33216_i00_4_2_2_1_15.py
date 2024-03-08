#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.15
# Title: Bidding down prevention in X2-handovers when target eNB receives a NR security capability
# Purpose:
# Verify that bidding down is prevented in X2-handovers when target eNB receives a NR security
# capability.
#
# Execution Steps:
# ----------------
# The target eNB sends the path-switch message to the MME.
#
# Expected Results:
# ----------------
# The UE NR security capability is in the path-switch message.


def test_33216_i00__TC_BID_DOWN_X2():
    skip('Not implemented...')
