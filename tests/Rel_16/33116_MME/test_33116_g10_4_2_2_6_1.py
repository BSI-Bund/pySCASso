#!/usr/bin/python3

from pytest import skip

# Function: MME
# Source: 33116-g10.md
# Section: 4.2.2.6.1
# Title: Authentication failure for emergency bearers
# Purpose:
# Ensure that the MME enforces that only emergency bearers can be used without successful
# authentication.
#
# Execution Steps:
# ----------------
# The UE sends the initial attach request for EPS emergency bearer services, then the MME initiates
# an authentication, which fails. The UE attached for EPS emergency bearer services sends the
# PDN Connectivity request for EPS non-emergency bearer services.
#
# Expected Results:
# ----------------
# The MME allows to continue the set up of the emergency bearer, and will reject the
# PDN Connectivity request for EPS non-emergency bearer services.


def test_33116_g10_4_2_2_6_1():
    skip('Missing test case name...')
