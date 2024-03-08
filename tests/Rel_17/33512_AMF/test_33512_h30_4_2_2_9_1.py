#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-h30.md
# Section: 4.2.2.9.1
# Title: NSSAA revocation
# Purpose:
# Verify that AMF deregisters UE when, after slice specific authorization revocation, there is no
# allowed NSSAI or Default NSSAI that can be used by UE.
#
# Execution Steps:
# ----------------
# A message requesting the AMF under test to revoke the authorization of the S-NSSAI in the Allowed
# NSSAI is simulated and sent the AMF under test.
#
# Expected Results:
# ----------------
# The Deregistration Request message is sent by the AMF under test to the UE.


def test_33512_h30_TC_NSSAA_REVOCATION():
    skip('Not implemented...')
