#!/usr/bin/python3

from pytest import skip

# Function: AMF
# Source: 33512-i10.md
# Section: 4.2.2.9.1
# Title: NSSAA revocation
# Purpose:
# Verify that AMF deregisters UE when, after slice specific authorization revocation, there is no
# allowed NSSAI or Default NSSAI that can be used by UE.
#
# Execution Steps:
# ----------------
# A message requesting the AMF under test to revoke the authorization of the S-NSSAI in the Allowed
# NSSAI is created simulated and sent to the AMF under test by the tester.
#
# Expected Results:
# ----------------
# The Deregistration Request message is sent by the AMF under test to the UE.
# The Deregistration Request message includes the list of rejected S-NSSAIs, each of them with the
# appropriate rejection cause value.


def test_33512_i10__TC_NSSAA_REVOCATION():
    skip('Not implemented...')
