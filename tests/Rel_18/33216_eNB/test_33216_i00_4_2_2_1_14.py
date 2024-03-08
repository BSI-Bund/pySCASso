#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.14
# Title: UE NR security capability is only sent to a SgNB
# Purpose:
#  To verify that the UE NR security capabilities are only sent to a SgNB.
#
# Execution Steps:
# ----------------
# 1. The tester triggers MeNB to send SN addition Request message to a SgNB.
# 2. The tester triggers UE HO from MeNB to another eNB.
# 3. The tester checks if the UE NR security capabilities were sent in the X2 interface in
# both step 1 and step 2.
#
# Expected Results:
# ----------------
# The UE NR security capabilities are only sent to the SgNB.


def test_33216_i00__TC_NR_SEC_CAP_SENT():
    skip('Not implemented...')
