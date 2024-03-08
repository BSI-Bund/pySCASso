#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.5.1
# Title: No access with 2G SIM via idle mode mobility
# Purpose:
# Verify that 2G subscribers cannot obtain service in EPS via idle mode mobility.
#
# Execution Steps:
# ----------------
# Context Response indicating GSM security mode.
#
# Expected Results:
# ----------------
# Context Response from the SGSN with an appropriate failure cause.


def test_33116_g10_4_2_2_5_1():
    skip('Missing test case name...')
