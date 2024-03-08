#!/usr/bin/python3

from pytest import skip

# Function: gNB
# Source: 33511-g80.md
# Section: 4.2.2.1.4
# Title: RRC integrity check failure
# Purpose:
# Verify that RRC integrity check failure is handled correctly by the gNB.
#
# Execution Steps:
# ----------------
# 1a) The UE sends a RRC message to the gNB without MAC-I; or
# 1b) The UE sends a RRC message to the gNB with a wrong MAC-I.
# 2b) The gNB verifies the integrity of the RRC message from the UE.
#
# Expected Results:
# ----------------
# The RRC message is discarded by the gNB after step 1a) or after step 2b).


def test_33511_g80_4_2_2_1_4():
    skip('Missing test case name...')
