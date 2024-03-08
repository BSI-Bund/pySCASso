#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.3.4
# Title: NAS confidentiality protection
# Purpose:
# Verify that NAS confidentiality protection algorithm is applied correctly.
#
# Execution Steps:
# ----------------
# The MME receives the SECURITY MODE COMPLETE message without confidentiality protection.
#
# Expected Results:
# ----------------
# If a confidentiality algorithm different from EEA0 was selected the MME rejects the message.


def test_33116_g10_4_2_2_3_4():
    skip('Missing test case name...')
