#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.2.4
# Title: Not forwarding EPS authentication data to SGSN
# Purpose:
# Verify that EPS authentication data remains in the EPC.
#
# Execution Steps:
# ----------------
# The MME receives an Identification Request message from the SGSN.
#
# Expected Results:
# ----------------
# The response to the SGSN does not include EPS authentication data.


def test_33116_g10_4_2_2_2_4():
    skip('Missing test case name...')
