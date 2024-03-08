#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.5.2
# Title: No access with 2G SIM via handover
# Purpose:
# Verify that GSM subscribers cannot obtain service in EPS via handovers.
#
# Execution Steps:
# ----------------
# Forward Location Request message indicating GSM security mode.
#
# Expected Results:
# ----------------
# Forward Relocation Request from the SGSN with an appropriate failure cause.


def test_33116_g10_4_2_2_5_2():
    skip('Missing test case name...')
