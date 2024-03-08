#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.10
# Title: Bidding down prevention in X2-handovers
# Purpose:
# Verify that bidding down is prevented in X2-handovers.
#
# Execution Steps:
# ----------------
# The target eNB sends the path-switch message to the MME.
#
# Expected Results:
# ----------------
# The UE EPS security capabilities are in the path-switch message.


def test_33216_i00_4_2_2_1_10():
    skip('Missing test case name...')
