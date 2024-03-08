#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.3.3
# Title: NAS NULL integrity protection
# Purpose:
# Verify that NAS NULL integrity protection algorithm is used correctly.
#
# Execution Steps:
# ----------------
# The MME sends the SECURITY MODE COMMAND message after successful UE authentication.
#
# Expected Results:
# ----------------
# The selected integrity algorithm is different from EIA0.


def test_33116_g10_4_2_2_3_3():
    skip('Missing test case name...')
