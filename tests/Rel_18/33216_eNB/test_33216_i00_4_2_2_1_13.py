#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.13
# Title: Map a UE NR security capability
# Purpose:
#  To verify that the eNB creates mapped UE NR security capabilities.
#
# Execution Steps:
# ----------------
# 1. The MeNB does not receive UE NR security capabilities from S1 Initial Context Setup Request
# message.
# 2. The MeNB sends SN Addition Request Message to the SgNB.
# 3. The tester checkes if the NR security capabilities are included in SN Addition Request
# Message.
#
# Expected Results:
# ----------------
# The SN Addition Request Message contains UE NR security capabilities, i.e. NEA0, 128-NEA1,
# 128-NEA2, 128-NEA3, NIA0, 128-NIA1, 128-NIA2, 128-NIA3


def test_33216_i00__TC_MAP_NR_SEC_CAP():
    skip('Not implemented...')
