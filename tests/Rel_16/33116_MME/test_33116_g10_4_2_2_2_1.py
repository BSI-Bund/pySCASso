#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.2.1
# Title: Access with 2G SIM forbidden
# Purpose:
# Verify that access to EPS with a 2G SIM is not possible.
#
# Execution Steps:
# ----------------
# Include 2G authentication vector in *authentication data response* from HSS.
#
# Expected Results:
# ----------------
# MME rejects UE authentication when receiving 2G authentication vector from HSS.
# NOTE: When both MME and HSS function correctly 2G authentication vector are never included in
# authentication data response from HSS to MME.


def test_33116_g10_4_2_2_2_1():
    skip('Missing test case name...')
