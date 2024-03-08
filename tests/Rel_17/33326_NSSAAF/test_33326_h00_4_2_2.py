#!/usr/bin/python3

from pytest import skip

# Function: NSSAAF
# Source: 33326-h00.md
# Section: 4.2.2
# Title: AAA-S authorization in re-authentication and revocation scenarios
# Purpose:
# Verify that the AAA-S is authorized to send the re-authentication or revocation.
#
# Execution Steps:
# ----------------
# 1. The AAA-S sends Re-authentication or revocation message to the NSSAAF including the S-NSSAI
# and the GPSI.
# 2. The NSSAAF checks whether the AAA-S can be matched against with the S-NSSAI based on the
# mapping table.
#
# Expected Results:
# ----------------
# The NSSAAF rejects the re-authentication or revocation or pass the re-authentication or
# revocation.


def test_33326_h00_TC_NSSAAF_AAAS_AUTHORIZATION_REAUTH_REVOCATION():
    skip('Not implemented...')
