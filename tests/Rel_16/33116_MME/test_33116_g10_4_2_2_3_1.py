#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.3.1
# Title: Bidding down prevention
# Purpose:
# Verify that bidding down by eliminating certain UE capabilities on the interface from UE to MME
# is not possible.
#
# Execution Steps:
# ----------------
# Attach request message includes security capabilities of the UE.
#
# Expected Results:
# ----------------
# MME includes the same security capabilities of the UE in the SECURITY MODE COMMAND message.


def test_33116_g10_4_2_2_3_1():
    skip('Missing test case name...')
