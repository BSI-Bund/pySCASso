#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.6.2
# Title: Correct transfer of UE security capabilities in AS security establishment
# Purpose:
# Verify that the UE security capabilities sent by the UE in the initial NAS registration request
# are the same UE security capabilities sent in the NGAP Context Setup Request message to establish
# AS security.
#
# Execution Steps:
# ----------------
# The tester triggers the initial NAS registration procedure with valid UE security capabilities.
#
# Expected Results:
# ----------------
# The NGAP Context Setup Request contains the same UE 5G security capabilities as sent in the
# initial NAS registration request.


def test_33512_i10__TC_UE_SEC_CAPS_AS_CONTEXT_SETUP():
    skip('Not implemented...')
