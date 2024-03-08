#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.2.3
# Title: Integrity check of Attach message
# Purpose:
# Verify that secure user identification by means of integrity check of Attach request works
# correctly.
#
# Execution Steps:
# ----------------
# The old MME receives an Identification Request message from the new MME with incorrect integrity
# protection.
#
# Expected Results:
# ----------------
# The old MME sends a response indicating that the user identity cannot be retrieved.


def test_33116_g10_4_2_2_2_3():
    skip('Missing test case name...')
