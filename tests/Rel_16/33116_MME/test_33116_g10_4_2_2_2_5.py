#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.2.5
# Title: Not forwarding unused EPS authentication data between different security domains
# Purpose:
# Verify that unused EPS authentication data remains in the same serving domain.
#
# Execution Steps:
# ----------------
# The old MME receives an Identification Request message from the new MME.
#
# Expected Results:
# ----------------
# The response to the new MME does not include unused EPS authentication data.


def test_33116_g10_4_2_2_2_5():
    skip('Missing test case name...')
