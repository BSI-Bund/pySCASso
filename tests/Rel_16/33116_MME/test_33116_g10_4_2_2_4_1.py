#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.4.1
# Title: Bidding down prevention in X2-handovers
# Purpose:
# Verify that bidding down is prevented in X2-handovers.
#
# Execution Steps:
# ----------------
# The MME receives the path-switch message with the UE EPS security capabilities different from the
# ones stored in the MME for that UE.
#
# Expected Results:
# ----------------
# The MME logs the event.


def test_33116_g10_4_2_2_4_1():
    skip('Missing test case name...')
