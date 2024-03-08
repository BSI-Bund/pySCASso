#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.3.2
# Title: NAS integrity algorithm selection and use
# Purpose:
# Verify that NAS integrity protection algorithm is selected and applied correctly.
#
# Execution Steps:
# ----------------
# The MME sends the SECURITY MODE COMMAND message. The UE replies with the
# SECURITY MODE COMPLETE message.
#
# Expected Results:
# ----------------
# 1. The MME has selected the integrity algorithm which has the highest priority according to the
# ordered lists and is contained in the UE EPS security capabilities. The MME checks the
# message authentication code on the SECURITY MODE COMPLETE message.
# 2. The MAC in the SECURITY MODE COMPLETE is verified, and the NAS integrity protection algorithm
# is selected and applied correctly.


def test_33116_g10_4_2_2_3_2():
    skip('Missing test case name...')
