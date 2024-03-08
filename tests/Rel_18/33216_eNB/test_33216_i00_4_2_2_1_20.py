#!/usr/bin/python3

from pytest import skip

# Function: eNB
# Source: 33216-i00.md
# Section: 4.2.2.1.20
# Title: Bidding down prevention for UP IP Policy
# Purpose:
# Verify that bidding down for UP IP policy is prevented in X2-handovers.
#
# Execution Steps:
# ----------------
# Test Case 1:
# - Source eNB sends EPS security capability with EIA7 indicating the UP IP is supported and
# UP IP policy with REQUIRED in Handover Request message to the target eNB.
# - eNB sends path-switch request message with UP IP policy with REQUIRED to the MME.
# Test Case 2:
# - Source eNB sends EPS security capability with EIA7 indicating the UP IP is supported in
# Handover Request message to the target eNB. The source eNB does not send UP IP policy in the
# Handover Request message.
# - eNB sends path-switch request message with UP IP policy with NOT NEEDED to the MME.
#
# Expected Results:
# ----------------
# For test case 1, the UP IP policy with REQUIRED is in the path-switch request message.
# For test case 2, the UP IP policy with NOT NEEDED is in the path-switch request message.


def test_33216_i00_4_2_2_1_20():
    skip('Missing test case name...')
